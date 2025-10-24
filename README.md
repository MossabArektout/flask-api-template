# Flask REST API Template (JWT + CRUD)

A ready-to-use **Flask REST API template** with authentication (JWT), database models, and CRUD operations.  
Perfect as a starter project for backend development, APIs, or learning Flask with JWT authentication.

---

## 🌟 Features

- Flask app structured with **Blueprints** (modular design)  
- JWT authentication (register/login)  
- User and Item models using **SQLAlchemy ORM**  
- CRUD endpoints for the `Item` resource  
- CORS enabled for frontend integration  
- Environment variables support for secrets and configuration  
- SQLite database for development simplicity  

---

## 🛠️ Installation

1. Clone the repository:

```bash
git https://github.com/MossabArektout/flask-api-template.git
cd flask-api-template
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

###### Windows :
```bash
venv\Scripts\activate
```
###### Linux/Mac :
```bash 
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a .env file with the following variables:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///data.db
JWT_SECRET_KEY=your_jwt_secret
```

6. Run the Flask server :
```bash
python run.py
```

## 🔑 Key Concepts Explained
- **Flask** : Lightweight Python web framework for building APIs or web apps.

- **Blueprints** : Organize routes into modular components (auth, api).

- **SQLAlchemy** : ORM to interact with databases using Python objects.

- **JWT (JSON Web Token)** : Token-based authentication for stateless security.

- **Werkzeug Security** : Secure password hashing and verification.

- **Environment Variables (.env)**: Store secrets and config outside code.

- **App Factory Pattern** : Dynamically create Flask app instances for better testing and modularity.

- **CORS** : Allows your API to accept requests from other domains (useful for frontend apps).

- **CRUD Operations** : Create, Read, Update, Delete actions for resources.

- **HTTP Methods** : GET, POST, PUT, DELETE corresponding to CRUD actions.

## 📦 Project Structure
```bash
flask-api-template/
│
├── app/
│   ├── __init__.py      # App factory
│   ├── models.py        # Database models
│   ├── routes.py        # CRUD endpoints
│   ├── auth.py          # Authentication endpoints
│   ├── utils.py         # Helper functions (optional)
│   └── config.py        # App configuration
│
├── venv/                # Virtual environment (ignored)
├── requirements.txt
├── .env                 # Environment variables (ignored)
├── .gitignore
└── run.py               # Entry point
```

## ⚡ Example Requests
#### Register User
```bash 
curl -X POST http://127.0.0.1:5000/auth/register \
-H "Content-Type: application/json" \
-d '{"username":"test","password":"1234"}'
```
#### Login User
```bash
curl -X POST http://127.0.0.1:5000/auth/login \
-H "Content-Type: application/json" \
-d '{"username":"test","password":"1234"}'
```
#### Use the returned token to access CRUD endpoints:
```bash
curl -X GET http://127.0.0.1:5000/api/items \
-H "Authorization: Bearer <YOUR_TOKEN>"
```

## 🌱 How to Extend
- Replace SQLite with PostgreSQL or MySQL

- Add more resources and CRUD routes

- Implement token refresh and logout

- Add role-based access control (RBAC)

- Add automated tests using ```pytest```

## ⭐ Support
If you find this repository useful or it has helped you,
please don't forget to leave a ⭐️, or even follow my GitHub account.
Your support motivates me to continue providing helpful resources.

## 👥 Credits
- Created by [**Mossab Arektout**](https://github.com/MossabArektout)

- Inspired by Flask official documentation and common REST API best practices

## 📄 License
This project is licensed under the **MIT License**