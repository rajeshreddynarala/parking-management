#  Parking Management System

A simple and user-friendly **web-based Parking Management System** developed as a **CRT project**. The system helps manage vehicle entry, parking slots, vehicle exit, parking fees, receipts, and parking history.
# Project Overview

The Parking Management System is designed to computerize the basic activities of a parking facility. It reduces manual work and makes it easier to track available parking slots, parked vehicles, parking duration, and revenue.

# Objectives

* Manage vehicle entry and exit efficiently.
* Track available and occupied parking slots.
* Automatically calculate parking fees.
* Generate parking receipts.
* Maintain vehicle parking history.
* Provide a simple dashboard for administrators.
* Store parking information securely using SQLite.

# Technologies Used

| Technology   | Purpose                |
| ------------ | ---------------------- |
| Python       | Backend programming    |
| Flask        | Web framework          |
| SQLite       | Database               |
| HTML5        | Web page structure     |
| CSS3         | User interface styling |
| JavaScript   | Frontend functionality |
| Git & GitHub | Version control        |

# Features

# Admin Login

Secure login page for accessing the parking management dashboard.

**Default credentials:**

```text
Username: admin
Password: admin123
```

# Dashboard

The dashboard displays:

* Total parking slots
* Occupied slots
* Available slots
* Today's vehicle count
* Total revenue
* Recent parking records

# Vehicle Entry

The administrator can enter:

* Vehicle number
* Owner name
* Vehicle type
* Parking slot

The system checks whether the selected slot is available before parking the vehicle.

# Parking Slot Management

Version 1 provides **20 parking slots**.

Each slot is displayed as:

```text
Available
Occupied
```

Occupied slots also display the parked vehicle information.

# Vehicle Exit

The administrator can search for an active vehicle using its vehicle number.

When the vehicle exits, the system records:

* Exit time
* Parking duration
* Parking fee

# Automatic Fee Calculation

The current hourly rates are:

| Vehicle Type |     Rate |
| ------------ | -------: |
| Bike         | ₹20/hour |
| Auto         | ₹30/hour |
| Car          | ₹40/hour |

The system charges a minimum of one hour.

# Receipt

After checkout, the system generates a parking receipt containing vehicle and payment information.

# Parking History

The system maintains previous parking records and allows administrators to search by:

* Vehicle number
* Owner name

# Project Structure

```text
parking-management-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── entry.html
│   ├── exit.html
│   ├── receipt.html
│   ├── slots.html
│   └── history.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── parking.db
```

> `parking.db` is automatically created when the application is started and should not be committed to GitHub.

# Installation
1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/parking-management-system.git
```

2. Open the project

```bash
cd parking-management-system
```

3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Run the application

```bash
python app.py
```

7. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

# Login

```text
Username: admin
Password: admin123
```

# System Workflow

```text
        ┌──────────────┐
        │ Admin Login  │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │  Dashboard   │
        └──────┬───────┘
               │
       ┌───────┴────────┐
       ▼                ▼
┌─────────────┐  ┌─────────────┐
│ Vehicle Entry│  │ Vehicle Exit│
└──────┬──────┘  └──────┬──────┘
       │                │
       ▼                ▼
┌─────────────┐  ┌─────────────┐
│ Assign Slot │  │ Calculate   │
│             │  │ Parking Fee │
└──────┬──────┘  └──────┬──────┘
       │                │
       └───────┬────────┘
               ▼
       ┌──────────────┐
       │    SQLite    │
       │   Database   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │    Receipt   │
       └──────────────┘
```

# Database

The application uses **SQLite**.

The main database tables are:

# `vehicles`

Stores:

* Vehicle ID
* Vehicle number
* Owner name
* Vehicle type
* Slot number
* Entry time
* Exit time
* Duration
* Parking fee

# `slots`

Stores:

* Slot number
* Slot status
* Vehicle ID

# Security Note

This is a **CRT/academic project Version 1**. The default administrator credentials are included for demonstration purposes.

For production use, authentication should be improved using:

* Password hashing
* Environment variables
* Secure session configuration
* Role-based access control

# Future Enhancements

The following features can be added in future versions:

* Automatic parking slot allocation
* Multiple administrator accounts
* User registration
* Password hashing
* Online payment integration
* QR-code parking receipts
* Parking reservations
* Daily/monthly reports
* Excel/PDF report generation
* Vehicle number validation
* Admin profile management
* REST API
* Cloud database
* Deployment to a cloud server
* Improved analytics dashboard

# Version

**Version:** 1.0
**Project:** Parking Management System
**Type:** CRT Academic Project
**Backend:** Python Flask
**Database:** SQLite

# Author

**Parking Management System – CRT Project**

# License

This project is created for **educational and academic purposes**.

