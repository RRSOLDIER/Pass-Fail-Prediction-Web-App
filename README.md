# Pass/Fail Prediction Web App

This is a simple Django web application that predicts whether a student will **pass or fail** based on their:

- Marks
- Attendance (%)
- Study hours per day

The prediction uses a **Logistic Regression machine learning model** trained on a small dataset.

---

## Features

- User-friendly form to enter marks, attendance, and study hours
- Instant prediction of pass/fail
- Bootstrap UI for clean interface
- ML model saved using `joblib` to avoid retraining every time

---

## How to Run
1. Clone repo
2. Install dependencies
3. Run server: python manage.py runserver
4. Open browser at http://127.0.0.1:8000

