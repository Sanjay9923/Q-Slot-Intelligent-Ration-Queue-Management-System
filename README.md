# Q-Slot-Intelligent-Ration-Queue-Management-System

## Overview

The Q-Slot system is a smart, web-based queue and ration token management platform developed using Python (Flask) and Twilio SMS API. It aims to modernize the Public Distribution System (PDS) by digitizing the allocation of time slots for ration collection and reducing congestion, mismanagement, and inefficiencies at ration shops.


## Screenshot

### **STEP 1**: Smart Ration Distribution portal

<img width="1212" height="662" alt="image" src="https://github.com/user-attachments/assets/1cc81200-cc59-4d56-902e-58f7f429ed75" />


### **STEP 2**: User Registration

<img width="1248" height="701" alt="image" src="https://github.com/user-attachments/assets/5a1adbd3-f22e-4d0f-a7e4-aa07f4f8c49b" />


### **STEP 3**: User Login

<img width="1250" height="702" alt="image" src="https://github.com/user-attachments/assets/411ae516-5077-4d45-bca9-bdbb65bd62b8" />


### **STEP 4**: Available Inventory

<img width="1146" height="663" alt="image" src="https://github.com/user-attachments/assets/1080c20d-cbdc-40dc-baa0-44a1a92ee0ae" />


### **STEP 5**: Select Time Slot For Purchase

<img width="1244" height="700" alt="image" src="https://github.com/user-attachments/assets/147bbe43-bca2-47f3-93f9-33ed47dfb204" />


### **STEP 6**: Token Generation

<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/69f1c5b7-72ec-4adf-8345-0022837bb22f" />


### **STEP 7**: Admin Dashboard

<img width="1225" height="689" alt="image" src="https://github.com/user-attachments/assets/1febb724-6c33-45af-b44e-588d4d5d9e01" />


### **STEP 8**: SMS From Your Twilio Account

<img width="1009" height="807" alt="image" src="https://github.com/user-attachments/assets/4a0749a6-9090-4e78-8eaa-980376976ce8" />


## Features

- **Smart Slot Booking**: Allows customers to reserve ration collection slots online.

- **Queue Optimization**:  Predicts and manages crowd flow using real-time data.

- **Admin Dashboard**:  Helps ration shop managers monitor user activity and manage queues.

- **Notifications**:  Sends SMS or email alerts for slot confirmations and updates.

- **User Authentication**:  Secure login and registration for customers and admins.


##  How It Works

1.**User Registration & Login** – Users sign up through the web portal.
   
2.**Smart Slot Booking** – System analyzes queue data and predicts optimal time slots. 
 
3.**IoT Sensors** – Track queue length and update the dashboard in real time.  

4.**Admin Dashboard** – Allows staff to monitor queues, manage slots, and view analytics.

5.**Real-Time Notifications** – Users receive updates about their token status and slot timing.


## Project Structure

Q-Slot Intelligent Ration Queue Management System/
│

├── app.py                # Main application file

├── initdb.py             # Database initialization script

├── templates/            # HTML templates

├── static/               # CSS, JS, and images

├── instance/             # Database files

├── requirements.txt      # Required Python libraries

└── .env (hidden)         # Environment variables


## Getting Started

1.**Open the Project Folder**

Launch Visual Studio Code (VS Code) and open the folder containing the following files and subfolders:
•	app.py
•	templates/ (HTML pages like register.html, login.html, dashboard.html)
•	static/ (CSS/JS if present)
•	Model files: queue_model.pkl, preprocessor.pkl, etc.
•	Database files.

2.**Install Python (3.x Recommended)**

•	Visit: https://www.python.org/downloads/
•	Download and install Python 3.x
•	 Check "Add Python to PATH" during setup

3.**Install Required Python Libraries**

Open terminal in VS Code and run:
bash
CopyEdit
pip install flask flask-login flask-mail
numpy pandas
tensorflow keras
twilio mysql-connector-python
		
4.**Verify Required Files Are Present**

Ensure these core files and folders exist in your project:
•	 app.py (main server logic)
•	 HTML files (register.html, login.html, etc.)
•	 queue_model.pkl, preprocessor.pkl, priority_scheduler.py
•	 Firebase or MySQL config
•	 Twilio account setup (SID, Auth Token, phone number)

5.**Set Up Database**

•	MySQL: Create tables for users, tokens, inventory using a provided SQL script
•	Or connect Firebase Realtime DB with credentials if using Firebase

6.**Configure Twilio & Email**

In app.py, configure Twilio like:
python
CopyEdit
from twilio.rest import Client
client = Client(account_sid, auth_token)
client.messages.create(
    		body="Your token is: XYZ123",
    		from_='+1234567890',
  		to='+91XXXXXXXXXX'
)
Set up SMTP for email alerts using flask_mail.

7.**Run the Application**

Start the Flask server:
bash
CopyEdit
python app.py

8.**Access Web Interface**

Open your browser and visit:
http
CopyEdit
http://127.0.0.1:5000/
•	Register using your ration card number.
•	Enter OTP (if implemented).
•	Log in and proceed.

9.**Book Slot and Generate Token**

•	Select a time slot for ration pickup.
•	If users ≤ 30, token is generated and sent via SMS.
•	Elderly are auto-prioritized.
•	Token valid for 20 minutes only.

10.**Admin Dashboard**

Admin logs in separately to:
•	View and manage all bookings
•	Track inventory stock levels
•	Update available items
•	See active/inactive tokens

11.**Real-Time Notifications**

•	Users receive SMS/email when slot starts or their turn nears.
•	Uses Twilio API and Flask-Mail for alerts.

12.**AI-Powered Queue Optimization**

•	LSTM/RNN model in queue_model.pkl:
o	Predicts user traffic
o	Adjusts slot timing dynamically
o	Prioritizes elderly using priority_scheduler.py

13.**Execution Complete**

You’ve now run the full Q-Slot Intelligent Ration Queue Management System with:
•	Real-time token and SMS notifications
•	Admin dashboard
•	AI queue prediction
•	Priority scheduling for elderly


## Technologies Used

**Programming Languages**: Python, HTML, CSS, JavaScript, SQL

**Frameworks & Libraries**: Flask/Django, NumPy, Pandas, TensorFlow, Keras, Scikit-learn, Bootstrap

**Database**: SQLite / MySQL

**APIs**: Twilio API, SMTP (Flask-Mail)

**Notifications Tools**: Twilio (SMS), SMTP (Email)

**Deep Learning**: TensorFlow, Keras (LSTM/RNN models)


## Future Improvements

- Add a mobile app for easier token booking and queue tracking.

- Implement QR-code tokens for faster and secure user verification at ration shops.

- Integrate multi-language support to improve accessibility for all users.

- Enhance queue prediction using improved LSTM/RNN models for accurate wait-time forecasting.

- Develop an admin analytics dashboard to visualize queue trends, user flow, and inventory data.

- Enable automated SMS/email reminders to notify users before their slot time and reduce missed appointments.


## Author

Sanjay S. — Developer & Project Lead

This project was developed as part of our final-year college curriculum. Our team of three collaboratively worked on designing, developing, and completing this project.

Contributions from the open-source community are also welcome. Feel free to submit pull requests or suggest improvements.


### License

This project is **free to use** and does not contains any license.



