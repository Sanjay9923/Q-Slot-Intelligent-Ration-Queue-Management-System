# Q-Slot-Intelligent-Ration-Queue-Management-System

## Overview

The Q-Slot system is a smart, web-based queue and ration token management platform developed using Python (Flask) and Twilio SMS API. It aims to modernize the Public Distribution System (PDS) by digitizing the allocation of time slots for ration collection and reducing congestion, mismanagement, and inefficiencies at ration shops.


## Preview (Screenshot)

### **STEP 1**: Smart Ration Distribution Portal

![517208068-e4b65410-f27f-47b3-8fd4-9959cc52a776 (1)](https://github.com/user-attachments/assets/7329fbd6-ba3d-4f9c-84de-c04b236e2dc1)


### **STEP 2**: User Registration

 ![514876542-5a1adbd3-f22e-4d0f-a7e4-aa07f4f8c49b (2)](https://github.com/user-attachments/assets/c6d139ad-eed6-4742-bd8f-e33e5b31c276)


### **STEP 3**: User Login

![514876729-411ae516-5077-4d45-bca9-bdbb65bd62b8 (1)](https://github.com/user-attachments/assets/1a50c80c-d314-4f67-aa3c-b3393f627650)


### **STEP 4**: Available Inventory

![514890936-1080c20d-cbdc-40dc-baa0-44a1a92ee0ae (1)](https://github.com/user-attachments/assets/bddf904a-86bc-4827-a66d-cee41faf344e)


### **STEP 5**: Select Time Slot For Purchase

![514877170-147bbe43-bca2-47f3-93f9-33ed47dfb204 (1)](https://github.com/user-attachments/assets/4894fcc7-c0be-4a80-a942-f7687f3e4fde)


### **STEP 6**: Token Generation

![514877387-69f1c5b7-72ec-4adf-8345-0022837bb22f (1)](https://github.com/user-attachments/assets/7d946a47-a6bc-4fbe-a88e-c55e2922c5ec)


### **STEP 7**: Admin Dashboard

![514877614-1febb724-6c33-45af-b44e-588d4d5d9e01 (1)](https://github.com/user-attachments/assets/c1485293-f81b-486e-85a9-b11d6cbda91b)


### **STEP 8**: SMS From Your Twilio Account

![514890415-4a0749a6-9090-4e78-8eaa-980376976ce8 (1)](https://github.com/user-attachments/assets/dbe940df-9b86-4b4f-a87b-efa2c027e235)


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
```bash
Q-Slot Intelligent Ration Queue Management System/
│
├── app.py                # Main application file
├── initdb.py             # Database initialization script
├── templates/            # HTML templates
├── static/               # CSS, JS, and images
├── instance/             # Database files
├── requirements.txt      # Required Python libraries
└── .env (hidden)         # Environment variables
```


## Getting Started

1.**Open the Project Folder**

Launch Visual Studio Code (VS Code) and open the folder containing the following files and subfolders:

- app.py

- templates/ (HTML pages like register.html, login.html, dashboard.html)

- static/ (CSS/JS if present)

- Model files: queue_model.pkl, preprocessor.pkl, etc.

- Database files.

2.**Python (3.x Recommended)**

- Visit: https://www.python.org/downloads/

- Download and install Python 3.x.

- Check "Add Python to PATH" during setup.

3.**Install Required Python Libraries**

Open terminal in VS Code and run the following command:
```bash
pip install flask flask-login flask-mail numpy pandas tensorflow keras twilio mysql-connector-python
```
4.**Verify Required Files Are Present**

Ensure these core files and folders exist in your project:

- app.py (main server logic)

- HTML files (register.html, login.html, etc.)

- queue_model.pkl, preprocessor.pkl, priority_scheduler.py

- Firebase or MySQL config

- Twilio account setup (SID, Auth Token, phone number)

5.**Set Up Database**

- MySQL: Create tables for users, tokens, inventory using a provided SQL script.

- Or connect Firebase Realtime DB with credentials if using Firebase.

6.**Configure Twilio & Email**

In app.py, set up your Twilio credentials and configure SMTP for email alerts using flask_mail.

7.**Run the Application**

Start the Flask server by running this command in the terminal:
```bash
python app.py
```


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

Sanjay.s — Developer & Project Lead

This project was developed as part of our final-year college curriculum. Our team of three collaboratively worked on designing, developing, and completing this project.

Contributions from the open-source community are also welcome. Feel free to submit pull requests or suggest improvements.


### License

This project is **free to use** and does not contains any license.



