# 🎓 Learning Management System (LMS)

An End-to-End DevOps project demonstrating application development, Docker containerization, CI/CD automation, and deployment on AWS EC2.

---

## 🚀 Project Overview

This project is a Flask-based Learning Management System (LMS) that allows users to:

- Login
- View Dashboard
- View Courses
- Add Courses

The application is containerized using Docker and automatically deployed to AWS EC2 using GitHub Actions.

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Docker
- Docker Hub
- Git
- GitHub
- GitHub Actions
- AWS EC2
- Linux

---

## 📁 Project Structure

```
LMS/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── static/
│
├── templates/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
```

---

## ✨ Features

- User Login
- Dashboard
- Course Management
- SQLite Database
- Dockerized Application
- GitHub Actions CI/CD
- AWS EC2 Deployment

---

# ⚙️ Local Installation

Clone the repository

```bash
git clone https://github.com/PavanGujari/LMS.git
```

Go to project folder

```bash
cd LMS
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://localhost:5000
```

---

# 🐳 Docker Deployment

Build Docker Image

```bash
docker build -t lms .
```

Run Container

```bash
docker run -d --name lms-container -p 5000:5000 lms
```

Open

```
http://localhost:5000
```

---

# ☁️ AWS EC2 Deployment

1. Launch Ubuntu EC2 Instance
2. Install Docker
3. Login to Docker Hub
4. Pull Docker Image
5. Run Docker Container

```bash
docker pull pavangujari/lms:latest

docker run -d --name lms-container -p 80:5000 pavangujari/lms:latest
```

Open

```
http://<EC2-PUBLIC-IP>
```

---

# 🔄 CI/CD Pipeline

Whenever code is pushed to the **main** branch:

- GitHub Actions starts automatically.
- Builds Docker Image.
- Pushes Image to Docker Hub.
- Connects to AWS EC2 using SSH.
- Pulls Latest Docker Image.
- Stops Old Container.
- Starts Updated Container.

---

# 📊 CI/CD Workflow

```
Developer
    │
git push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
Build Docker Image
    │
    ▼
Push Docker Image
    │
    ▼
Docker Hub
    │
    ▼
AWS EC2
    │
    ▼
Updated LMS Application
```

---

# 👨‍💻 Author

**Pavan Gujari**

DevOps Engineer | AWS | Docker | Kubernetes | Linux | CI/CD | Terraform