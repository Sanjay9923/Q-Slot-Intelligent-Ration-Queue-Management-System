import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")


from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from threading import Timer
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

# Load environment variables (set these in your shell or .env file)
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecret')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    ration_card = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

class TokenQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    token_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Active')  # Active, Expired
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    slot = db.Column(db.String(20), nullable=False)  # e.g., "10-11", "11-1"

class PasswordResetToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(100), nullable=False, unique=True)
    expiration_time = db.Column(db.DateTime, nullable=False)


# Utility: send SMS via Twilio
def send_sms(to_number, body):
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
        print("Twilio credentials not set, skipping SMS.")
        return
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"Sent SMS: {message.sid}")
    except Exception as e:
        print(f"SMS send failed: {e}")

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print("Received form data:", request.form)  # Debug print
        name = request.form.get('name')
        phone = request.form.get('phone')
        ration_card = request.form.get('ration_card')
        email = request.form.get('email')
        raw_pw = request.form.get('password')

        if not email:
            flash("Email is required but was not received.", 'danger')
            return redirect(url_for('register'))

        # Check if ration card or email already exists
        if User.query.filter_by(ration_card=ration_card).first():
            flash("Ration card already registered.", 'warning')
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", 'warning')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(raw_pw)
        user = User(name=name, phone=phone, ration_card=ration_card, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully. Please log in.", 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ration_card = request.form['ration_card']
        raw_pw = request.form['password']
        user = User.query.filter_by(ration_card=ration_card).first()
        if user and check_password_hash(user.password, raw_pw):
            session['user_id'] = user.id
            session['is_admin'] = False
            return redirect(url_for('dashboard'))
        flash("Invalid credentials.", 'danger')
    return render_template('login.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        raw_pw = request.form['password']
        # Simple hardcoded admin
        if username == 'admin' and raw_pw == 'admin123':
            session['is_admin'] = True
            return redirect(url_for('admin_dashboard'))
        flash("Invalid admin credentials.", 'danger')
    return render_template('admin_login.html')

from datetime import datetime, timedelta

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session or session.get('is_admin'):
        return redirect(url_for('login'))

    user_id = session['user_id']

    # Expire tokens older than 25 minutes
    expiry_threshold = datetime.utcnow() - timedelta(minutes=2)
    expired_tokens = TokenQueue.query.filter(
        TokenQueue.status == 'Active',
        TokenQueue.timestamp < expiry_threshold
    ).all()

    for token in expired_tokens:
        token.status = 'Expired'

    if expired_tokens:
        db.session.commit()

    # Fetch inventory and user's active token
    inventory = Inventory.query.all()
    user_token = TokenQueue.query.filter_by(user_id=user_id, status='Active').first()

    return render_template('inventory.html', inventory=inventory, user_token=user_token)


# Admin Dashboard Route
@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        item = request.form['item']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        db.session.add(Inventory(item=item, quantity=quantity, price=price))
        db.session.commit()
        flash("Inventory updated.", 'success')

    inventory = Inventory.query.all()
    tokens = TokenQueue.query.filter(TokenQueue.status == "Active").order_by(TokenQueue.slot).all()

    return render_template('admin.html', inventory=inventory, tokens=tokens)

# Edit Item Route
@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    
    # Retrieve the item from the database
    item = Inventory.query.get_or_404(item_id)

    if request.method == 'POST':
        try:
            # Get the updated details from the form
            item.item = request.form['item']
            item.quantity = int(request.form['quantity'])
            item.price = float(request.form['price'])

            if item.quantity <= 0 or item.price <= 0:
                flash("Quantity and Price must be positive values.", 'warning')
            else:
                # Commit the updated details to the database
                db.session.commit()
                flash("Item updated successfully.", 'success')
                return redirect(url_for('admin_dashboard'))

        except ValueError:
            flash("Please enter valid numeric values for quantity and price.", 'danger')

    return render_template('edit_item.html', item=item)

@app.route('/request_purchase', methods=['GET', 'POST'])
def request_purchase():
    if 'user_id' not in session or session.get('is_admin'):
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('request_purchase.html')  # We’ll define this HTML below

    slot = request.form['slot']  # Selected slot by the user
    user_id = session['user_id']

    # Predefined slots (Assumed 5 slots in total)
    slots = ["10-11", "11-1",  "1-2", "3-4", "4-5"]

    # Check if the selected slot is valid
    if slot not in slots:
        flash("Invalid slot selection.", "danger")
        return redirect(url_for('request_purchase'))

    # Check if the user already has an active token
    existing_token = TokenQueue.query.filter_by(user_id=user_id, status='Active').first()

    if existing_token:
        flash(f"You already have an active token #{existing_token.token_number} for slot {existing_token.slot}.", "warning")
        return redirect(url_for('dashboard'))

    # Count current users in that slot
    #slot_user_count = TokenQueue.query.filter_by(slot=slot, status='Active').count()
    slot_user_count = 10
    # Check if the slot is full or underfilled
    if slot_user_count >= 30:
        flash("Slot is full. Please select another slot.", "danger")
        return redirect(url_for('request_purchase'))

    if slot_user_count < 10:
        flash("Proceed to purchase without token. Slot hasn't reached minimum for token allocation.", "info")
        return redirect(url_for('dashboard'))

    # Assign token
    last_token = db.session.query(db.func.max(TokenQueue.token_number)).scalar() or 0
    token_number = last_token + 1
    new_token = TokenQueue(user_id=user_id, token_number=token_number, slot=slot, status='Active')
    db.session.add(new_token)
    db.session.commit()

    user = User.query.get(user_id)

    send_sms(user.phone, f"Your token #{token_number} is confirmed for slot {slot}.")

    # Schedule alert after 10 minutes
    Timer(60, lambda: send_sms('+918200827307', f"Reminder: Your token #{token_number} was allocated 10 minutes ago for slot {slot}.")).start()

    # Schedule expiration after 25 minutes
    Timer(120, lambda: expire_token(new_token.id)).start()

    flash(f"Token #{token_number} allocated for slot {slot}.", 'success')
    return redirect(url_for('dashboard'))




def expire_old_tokens():
    expiry_threshold = datetime.utcnow() - timedelta(minutes=2)
    expired_tokens = TokenQueue.query.filter(
        TokenQueue.status == 'Active',
        TokenQueue.timestamp < expiry_threshold
    ).all()
    
    for token in expired_tokens:
        token.status = 'Expired'

    if expired_tokens:
        db.session.commit()



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/chat', methods=['GET', 'POST'])
def chatbot():
    response = None
    if request.method == 'POST':
        query = request.form['query'].lower()
        if "token" in query and 'user_id' in session:
            token = TokenQueue.query.filter_by(user_id=session['user_id'], status='Active').first()
            response = f"Your active token number is {token.token_number}." if token else "You do not currently have a token."
        elif any(k in query for k in ["rice", "inventory"]):
            items = Inventory.query.all()
            response = "Current inventory:\n" + "\n".join([f"{i.item}: {i.quantity}kg" for i in items])
        elif "collect" in query:
            response = "Token holders will be notified by SMS 20 minutes before their slot."
        else:
            response = "Sorry, I didn't understand that."
    return render_template('chatbot.html', response=response)

import secrets
from datetime import timedelta
from flask import flash, redirect, render_template, url_for
from email.message import EmailMessage
import smtplib

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            # Generate a unique token
            token = secrets.token_urlsafe(16)  # Generate a secure token
            expiration_time = datetime.utcnow() + timedelta(minutes=30)  # Set expiry for 30 minutes
            reset_token = PasswordResetToken(user_id=user.id, token=token, expiration_time=expiration_time)
            db.session.add(reset_token)
            db.session.commit()

            # Create reset password link
            reset_link = url_for('reset_password', token=token, _external=True)

            msg = EmailMessage()
            msg['Subject'] = 'Password Reset Request - Ration System'
            msg['From'] = GMAIL_USER
            msg['To'] = email
            msg.set_content(
                f"Dear {user.name},\n\n"
                f"To reset your password, click the following link:\n{reset_link}\n\n"
                "The link will expire in 30 minutes.\n\n- Ration System"
            )
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(GMAIL_USER, GMAIL_PASSWORD)
                    smtp.send_message(msg)
                flash("A password reset link has been sent to your email.", "success")
            except Exception as e:
                flash("Failed to send recovery email. Please try again later.", "danger")
        else:
            flash("No account found with that email.", "warning")
        return redirect(url_for('forgot_password'))

    return render_template('forgot_password.html')


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    reset_token = PasswordResetToken.query.filter_by(token=token).first()
    if not reset_token or reset_token.expiration_time < datetime.utcnow():
        flash("Invalid or expired reset link.", "danger")
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        new_password = request.form['new_password']
        user = User.query.get(reset_token.user_id)
        user.password = generate_password_hash(new_password)
        db.session.commit()

        # Remove the reset token
        db.session.delete(reset_token)
        db.session.commit()

        flash("Your password has been successfully reset!", "success")
        return redirect(url_for('login'))

    return render_template('reset_password.html', token=token)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
