# ✈️ Flight Booking System

A simple Flight Booking System built using **Python** and **MySQL** as a part of my Computer Science project.

## 📌 Features

* Add and manage flight bookings
* Search flights and passengers
* Cancel bookings
* User-friendly menu-driven interface
* MySQL database integration

## 🛠️ Technologies Used

* Python 3
* MySQL 8
* `mysql-connector-python`
* `tabulate` (for table formatting)

## 📸 Screenshots

> *In the main folder*

## 📂 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Flight-Booking-System.git
cd Flight-Booking-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup MySQL Database

1. Make sure your MySQL server is running.
2. Open MySQL client or shell.
3. Create the database and tables:

```sql
CREATE DATABASE airlines;
USE airlines;
```

Or use the file `flight_booking_schema.sql`.

### 4. Update `main.py` (if needed)

Make sure your credentials are correct:

```python
mycon = mys.connect(
    host="localhost",
    user="root",
    passwd="your-password",
    database="airlines"
)
```

### 5. Run the program

```bash
python main.py
```

---

## 📦 Requirements

```
mysql-connector-python
tabulate
```

You can install them using:

```bash
pip install mysql-connector-python tabulate
```

---

## 🙇‍♂️ Author

**Siddhant Wadher**
Student | Developer | Tech Enthusiast
