---

# 🌍 Travel Management System

A full-stack web application for managing travel bookings built with **React**, **Tailwind CSS**, **Python Flask**, and **MySQL**.
Perfect for DBMS academic projects showcasing real-world development.

---

# ✨ Features

* **User Authentication** – Secure login & registration
* **Travel Packages** – Browse travel packages with descriptions
* **Booking System** – Book packages with total price calculation
* **Admin Dashboard** – Manage packages & view user bookings
* **Responsive UI** – Tailwind CSS for clean and modern design
* **Secure Sessions** – Flask-based session authentication
* **Proper DBMS Concepts** – Relationships, joins, foreign keys

---

# 🛠️ Tech Stack

**Frontend:** React, Vite, Tailwind CSS, Axios
**Backend:** Python Flask, Flask-CORS, Flask-Bcrypt
**Database:** MySQL
**Auth:** Session-based with hashed passwords

---

# 📁 Project Structure

```
travel-management-system/
│
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Configuration settings
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment variables
│   ├── routes/
│   │   ├── auth_routes.py     # Authentication APIs
│   │   ├── package_routes.py  # Package APIs
│   │   └── booking_routes.py  # Booking APIs
│   ├── models/
│   │   ├── user_model.py      # User data operations
│   │   ├── package_model.py   # Package data operations
│   │   └── booking_model.py   # Booking data operations
│   └── database/
│       └── connection.py      # MySQL connection setup
│
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    ├── src/
    │   ├── App.jsx
    │   ├── main.jsx
    │   ├── pages/
    │   │   ├── Home.jsx
    │   │   ├── Packages.jsx
    │   │   ├── Login.jsx
    │   │   ├── Register.jsx
    │   │   ├── BookPackage.jsx
    │   │   └── AdminDashboard.jsx
    │   ├── components/
    │   │   ├── Navbar.jsx
    │   │   ├── PackageCard.jsx
    │   │   └── Footer.jsx
    │   ├── utils/
    │   │   └── api.js
    │   └── styles/
    │       └── global.css
```

---

# 🚀 Installation & Setup

## 1️⃣ Prerequisites

Install the following:

* Node.js (v14+)
* Python (v3.8+)
* MySQL Server
* Git

---

# 2️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/travel-management-system.git
cd travel-management-system
```

---

# 3️⃣ Backend Setup

### Navigate to backend folder:

```bash
cd backend
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Create `.env` file:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=travel_db
SECRET_KEY=your_secret_key
```

### Start backend:

```bash
python app.py
```

**Expected Output:**

```
Database tables created successfully
Server running on http://localhost:5000
```

---

# 4️⃣ Frontend Setup

### Navigate to frontend:

```bash
cd frontend
```

### Install dependencies:

```bash
npm install
```

### Run development server:

```bash
npm run dev
```

Local server:
➡️ [http://localhost:3000/](http://localhost:3000/)

---

# 5️⃣ Database Setup

### Using MySQL CLI:

```bash
mysql -u root -p
CREATE DATABASE travel_db;
SHOW DATABASES;
```

### Using MySQL Workbench:

1. Open Workbench
2. Connect to MySQL instance
3. Run:

   ```sql
   CREATE DATABASE travel_db;
   ```

Backend will auto-create tables.

---

# 🔑 Default Credentials

### Admin:

* Email: **[admin@travel.com](mailto:admin@travel.com)**
* Password: **admin123**

### Users:

* Register from the frontend

---

# 🗄️ Database Schema

## customers

```sql
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## travel_packages

```sql
CREATE TABLE travel_packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    package_name VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## bookings

```sql
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    package_id INT,
    travellers INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id)
);
```

---

# 🌐 API Endpoints

## Authentication (`/auth`)

* POST `/auth/register`
* POST `/auth/login`
* POST `/auth/logout`

## Packages (`/api`)

* GET `/api/packages`
* POST `/api/packages`
* GET `/api/packages/<id>`

## Bookings (`/api`)

* POST `/api/bookings`
* GET `/api/bookings`

---

# 🐛 Troubleshooting

### MySQL not running:

```bash
sudo service mysql start
```

### Port already in use:

```bash
sudo lsof -t -i tcp:5000 | xargs kill -9
```

### Python module errors:

```bash
pip install -r requirements.txt
```

### Frontend build errors:

```bash
rm -rf node_modules package-lock.json
npm install
```

---

# 📊 DBMS Concepts Covered

* CRUD operations
* Relationships (1-to-many)
* Foreign keys
* SQL joins
* Authentication system
* Data validation
* Transactions

---

# 🖥️ Running the Application

```bash
# Backend
cd backend
python app.py

# Frontend
cd frontend
npm run dev
```

---

# 👥 Contributing

1. Fork the repo
2. Create a branch
3. Commit changes
4. Push and submit PR

---

# 📄 License

MIT License

---

# 🙏 Acknowledgments

* Built for DBMS Academic Activity
* React & Flask documentation
* Tailwind CSS
* MySQL

---

# 🎉 Happy Coding & Happy Travels!

---
