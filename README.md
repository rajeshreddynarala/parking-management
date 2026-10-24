# Five-Floor Parking Management System

A student-friendly CRT project built with Python, Flask, SQLite, HTML and CSS.

## Features
- 5 floors and 10 slots per floor (50 parking spaces)
- Automatic slot allocation
- Dashboard showing free and occupied spaces
- Vehicle entry, checkout, parking history
- Parking fee: ₹20 per started hour
- SQLite database created automatically

## Run locally
1. Install Python 3.10 or later.
2. Install dependencies: `pip install -r requirements.txt`
3. Start the app: `python app.py`
4. Open `http://127.0.0.1:5000` in your browser.

## Deploy from a phone
This repository includes a `render.yaml` configuration for Render.
1. Sign in at https://render.com using your browser.
2. Choose **New +** → **Web Service**.
3. Connect GitHub and select `parking-management`.
4. If prompted, use these settings:
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Tap **Create Web Service** and wait for the deployment to finish.
6. Open the public URL Render gives you.

## Important
This is a learning/demo project, not a production parking service. The free hosting filesystem may be temporary, so SQLite records can be lost after redeploys or restarts. Do not enter real customer data. For a real service, use persistent managed database storage, authentication, CSRF protection and secure configuration.
