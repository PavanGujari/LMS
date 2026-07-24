# 🎓 Learning Management System (LMS)

## 📌 Project Overview
This is a Learning Management System (LMS) developed using Python Flask. The application allows users to log in, view courses, and add new courses. It is containerized using Docker and can be deployed on AWS EC2 with GitHub Actions for CI/CD.

---

## 🚀 Features

- User Login
- Dashboard
- View Courses
- Add New Course
- SQLite Database
- Dockerized Application
- GitHub Repository
- AWS EC2 Deployment
- GitHub Actions CI/CD

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- SQLite
- Docker
- Docker Compose
- Git
- GitHub
- AWS EC2
- GitHub Actions

---

## 📁 Project Structure

```
lms/
│── .github/
│── static/
│── templates/
│── app.py
│── Dockerfile
│── docker-compose.yaml
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd lms
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t lms:v1 .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name lms-container lms:v1
```

---

## ☁️ AWS Deployment

1. Launch an EC2 instance.
2. Install Docker.
3. Pull the Docker image from Docker Hub.
4. Run the container.
5. Access the application using the EC2 Public IP.

---

## 🔄 CI/CD

GitHub Actions automatically:

- Builds the Docker image
- Pushes it to Docker Hub
- Connects to AWS EC2
- Pulls the latest image
- Restarts the container..

---

  ## 👨‍💻 Author

**Pavan Gujari**