# Q-Slot Intelligent Ration Queue Management System
## Overview

The Q-Slot Intelligent Ration Queue Management System is a smart solution that automates ration distribution and queue management. It provides an efficient slot-booking mechanism to reduce waiting times, optimize resource allocation, and improve service quality in ration shops.


## Key Features

**Smart Slot Booking**: Allows customers to reserve ration collection slots online.

**Queue Optimization**:  Predicts and manages crowd flow using real-time data.

**Admin Dashboard**:  Helps ration shop managers monitor user activity and manage queues.

**Notifications**:  Sends SMS or email alerts for slot confirmations and updates.

**User Authentication**:  Secure login and registration for customers and admins.


##  How It Works
1.**User Registration & Login** – Users sign up through the web portal.
   
2.**Smart Slot Booking** – System analyzes queue data and predicts optimal time slots. 
 
3.**IoT Sensors** – Track queue length and update the dashboard in real time.  

4.**Admin Dashboard** – Allows staff to monitor queues, manage slots, and view analytics.

5.**Real-Time Notifications** – Users receive updates about their token status and slot timing.


## Tech Stack

**Frontend**: HTML, CSS, JavaScript

**Backend**: Python (Flask Framework)\Django

**Database**: MySQL

**Libraries/Tools**: Twilio API (for notifications), dotenv, smtplib


## Installation & Setup

1.**Clone the Repository**

git clone https://github.com/Sanjay9923/Q-Slot-Intelligent-Ration-Queue-Management-System.git
cd Q-Slot-Intelligent-Ration-Queue-Management-System


2.**Create a Virtual Environment**:

python -m venv venv
venv\Scripts\activate


3.**Install Required Packages**:

pip install -r requirements.txt


4.**Set Environment Variables**:
Create a .env file in the project root with:

TWILIO_ACCOUNT_SID=your_sid_here

TWILIO_AUTH_TOKEN=your_token_here

TWILIO_PHONE_NUMBER=your_twilio_number

GMAIL_USER=your_email

GMAIL_PASSWORD=your_app_password

FLASK_SECRET_KEY=your_secret_key


5.**Run the Application**:

python app.py


6.**Access the App**:
Open your browser and go to http://127.0.0.1:5000/


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


## System Architecture

User → Web Interface (Flask App)
        ↕
   MySQL Database
        ↕
IoT Sensors → Data → Flask Backend → Machine Learning Model


## Future Improvements

Develop a mobile app for users.

Integrate biometric verification for identity checks.

Enable multilingual support.

Add analytics dashboard for queue prediction trends.


## Project Contributor

**Sanjay.s** – Developer & Project Lead

Open for contributions! Feel free to submit pull requests or suggest improvements.

## License

This project is open-source and available under the MIT License.
