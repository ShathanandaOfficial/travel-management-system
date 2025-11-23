```markdown
# 🌍 Travel Management System

A complete full-stack web application for managing travel bookings built with **React**, **Tailwind CSS**, **Python Flask**, and **MySQL**. Perfect for DBMS academic projects demonstrating real-world web development.

## ✨ Features

- **👤 User Authentication** - Secure registration and login system
- **🎒 Travel Packages** - Browse and view available travel packages
- **📅 Booking System** - Book packages with dynamic pricing calculation
- **👨‍💼 Admin Dashboard** - Manage packages and view all bookings
- **📱 Responsive Design** - Mobile-friendly UI with Tailwind CSS
- **🔒 Secure Sessions** - Flask session-based authentication
- **🗄️ Database Relationships** - Proper MySQL foreign key relationships

## 🛠️ Tech Stack

**Frontend:** React, Tailwind CSS, Vite, Axios  
**Backend:** Python Flask, Flask-CORS, Flask-Bcrypt  
**Database:** MySQL  
**Authentication:** Session-based with Bcrypt hashing

---

## 📁 Project Structure

```
travel-management-system/
│
├── 📂 backend/
│   ├── 🐍 app.py                 # Main Flask application
│   ├── ⚙️ config.py              # Configuration settings
│   ├── 📋 requirements.txt       # Python dependencies
│   ├── 🔐 .env                   # Environment variables
│   ├── 📂 routes/
│   │   ├── 🔑 auth_routes.py     # Authentication endpoints
│   │   ├── 🎒 package_routes.py  # Package management endpoints
│   │   └── 📅 booking_routes.py  # Booking endpoints
│   ├── 📂 models/
│   │   ├── 👤 user_model.py      # User data operations
│   │   ├── 🎒 package_model.py   # Package data operations
│   │   └── 📅 booking_model.py   # Booking data operations
│   └── 📂 database/
│       └── 🔗 connection.py      # Database connection setup
│
└── 📂 frontend/
    ├── 🏠 index.html
    ├── 📦 package.json
    ├── ⚡ vite.config.js
    ├── 🎨 tailwind.config.js
    ├── 📂 src/
    │   ├── 🎯 App.jsx            # Main React component
    │   ├── 🔥 main.jsx           # React DOM entry point
    │   ├── 📂 pages/
    │   │   ├── 🏠 Home.jsx
    │   │   ├── 🎒 Packages.jsx
    │   │   ├── 🔑 Login.jsx
    │   │   ├── 📝 Register.jsx
    │   │   ├── 📅 BookPackage.jsx
    │   │   └── 👨‍💼 AdminDashboard.jsx
    │   ├── 📂 components/
    │   │   ├── 🧭 Navbar.jsx
    │   │   ├── 🎴 PackageCard.jsx
    │   │   └── 🦶 Footer.jsx
    │   ├── 📂 utils/
    │   │   └── 🌐 api.js         # API service functions
    │   └── 📂 styles/
    │       └── 🌍 global.css     # Global styles
```

---

## 🚀 Installation & Setup

### Prerequisites
- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **MySQL** Server
- **Git**

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/travel-management-system.git
cd travel-management-system
```

### Step 2: Backend Setup

#### Navigate to backend folder:
```bash
cd backend
```

#### Install Python dependencies:
```bash
pip install -r requirements.txt
```

#### Create `.env` file:
```bash
# Create .env file in backend folder
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=travel_db
SECRET_KEY=your-secret-key-here
```

#### Start the backend server:
```bash
python app.py
```

**✅ Expected Output:**
```
✅ Database tables created successfully!
🚀 Starting Travel Management System Backend...
📊 Database initialization completed!
🌐 Server running on http://localhost:5000
```

### Step 3: Frontend Setup

#### Open new terminal and navigate to frontend:
```bash
cd frontend
```

#### Install Node.js dependencies:
```bash
npm install
```

#### Start the frontend development server:
```bash
npm run dev
```

**✅ Expected Output:**
```
  Vite dev server running at:
  ➜  Local:   http://localhost:3000/
```

### Step 4: Database Setup

#### Using MySQL Command Line:
```bash
mysql -u root -p

# Create database
CREATE DATABASE travel_db;

# Verify database
SHOW DATABASES;
```

#### Using MySQL Workbench:
1. Open MySQL Workbench
2. Connect to your MySQL instance
3. Create new database:
   ```sql
   CREATE DATABASE travel_db;
   ```
4. The backend will automatically create tables on first run

---

## 🔑 Default Login Credentials

### Admin Account:
- **Email:** `admin@travel.com`
- **Password:** `admin123`

### Regular User:
- Register any new account through the registration page

---

## 🗄️ Database Schema

### Tables Structure:

#### `customers` Table:
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

#### `travel_packages` Table:
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

#### `bookings` Table:
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

## 🌐 API Endpoints

### Authentication Routes (`/auth`)
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Package Routes (`/api`)
- `GET /api/packages` - Get all packages
- `POST /api/packages` - Create new package (Admin only)
- `GET /api/packages/<id>` - Get specific package

### Booking Routes (`/api`)
- `POST /api/bookings` - Create new booking
- `GET /api/bookings` - Get all bookings (Admin only)

---

## 🎯 Usage Guide

### For Users:
1. **Browse Packages:** Visit Packages page to see available trips
2. **Register/Login:** Create account or login with existing credentials
3. **Book Package:** Click "Book Now" on any package
4. **Select Travelers:** Choose number of travelers and confirm booking

### For Admins:
1. **Login** with admin credentials
2. **Access Admin Dashboard** from navigation
3. **Add New Packages** using the form
4. **View All Bookings** in the bookings tab

---

## 🐛 Troubleshooting

### Common Issues & Solutions:

#### 1. MySQL Connection Error
```bash
# Check if MySQL service is running
sudo service mysql status

# Start MySQL service
sudo service mysql start
```

#### 2. Port Already in Use
```bash
# Kill process using port 5000
sudo lsof -t -i tcp:5000 | xargs kill -9

# Or change port in app.py
app.run(debug=True, port=5001)
```

#### 3. Module Not Found (Python)
```bash
# Reinstall requirements
pip install -r requirements.txt

# If using virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

#### 4. Frontend Build Issues
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

#### 5. Database Tables Not Created
- Check MySQL credentials in `.env` file
- Ensure database `travel_db` exists
- Check backend logs for error messages

---

## 📊 DBMS Concepts Demonstrated

- ✅ **CRUD Operations** - Create, Read, Update, Delete
- ✅ **Foreign Keys & Relationships** - Customer → Bookings → Packages
- ✅ **SQL Joins** - Multi-table queries for booking data
- ✅ **Database Authentication** - Secure user login system
- ✅ **Data Integrity** - Constraints and validations
- ✅ **Transaction Management** - Atomic booking operations

---

## 🖥️ Running the Application

### Quick Start Commands:
```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend  
cd frontend
npm run dev
```

### Access Points:
- **Frontend Application:** http://localhost:3000
- **Backend API:** http://localhost:5000
- **API Test:** http://localhost:5000/api/packages

---

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built as a DBMS Academic Project
- React & Flask documentation
- Tailwind CSS for styling
- MySQL for database management

---

## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact the development team.

---

**Happy Travels! 🌎✈️**
```

---

## 🎯 **Additional Files to Create:**

### **1. .gitignore** (in project root)
```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
.env

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
dist/
build/

# Database
*.db
*.sqlite3

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### **2. LICENSE** (in project root - optional)
```text
MIT License

Copyright (c) 2024 Travel Management System

Permission is hereby granted...
```

---

## 🚀 **Final Push to GitHub:**

```bash
# Initialize git
git init

# Add all files
git add .

# Initial commit
git commit -m "feat: Complete Travel Management System

- Frontend: React + Tailwind CSS with Vite
- Backend: Python Flask with MySQL
- Features: User authentication, package booking, admin dashboard
- Database: MySQL with proper relationships and CRUD operations
- Responsive design and RESTful APIs"

# Connect to GitHub (create repo first)
git remote add origin https://github.com/your-username/travel-management-system.git

# Push to main branch
git branch -M main
git push -u origin main
```
