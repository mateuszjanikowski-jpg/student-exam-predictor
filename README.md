# Student Exam Success Predictor

Machine learning web application built with Streamlit, Docker, and cloud deployment tools.

---

## Project Overview

This project predicts whether a student is likely to pass an exam based on several input factors such as:

- study hours
- attendance
- previous scores
- sleep hours
- stress level

The application uses a Random Forest machine learning model trained on a generated dataset and provides predictions through an interactive Streamlit web interface.

---

## Features

- Predicts exam success probability
- Interactive Streamlit frontend
- Machine learning model using Scikit-learn
- Dataset generation and model training included
- Dockerized application
- Cloud deployment with Render
- Automated CI/CD pipeline with GitHub Actions
- Infrastructure as Code setup with Terraform
- Git hooks with pre-commit

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Docker
- Git & GitHub
- GitHub Actions (CI/CD)
- Render (Cloud Deployment)
- Terraform (Infrastructure as Code)
- pre-commit
- Black
- Flake8

---

## Live Demo

Application deployed on Render:

https://student-exam-predictor-v694.onrender.com

---

## Workflow

1. Generate the dataset and train the machine learning model using `train_model.py`
2. Save the trained model using Joblib
3. Run the Streamlit application locally
4. Containerize the application with Docker
5. Push the project to GitHub
6. Automatically run CI/CD checks with GitHub Actions
7. Deploy the application to the cloud using Render
8. Manage infrastructure configuration using Terraform

---

## CI/CD

GitHub Actions automatically:

- installs project dependencies
- checks Python syntax
- builds the Docker image

The workflow is triggered automatically after every push to the `main` branch.

Render automatically redeploys the application after changes are pushed to GitHub.

---

## Infrastructure as Code

Terraform configuration is located in the `terraform/` directory.

The project includes:

- `main.tf`
- `providers.tf`
- `variables.tf`

Terraform was initialized and tested using the Render provider.

---

## Project Structure

```text
student-exam-predictor/
├── .github/workflows/
│   └── ci.yml
├── terraform/
│   ├── main.tf
│   ├── providers.tf
│   └── variables.tf
├── data/
│   └── students.csv
├── models/
│   └── student_model.joblib
├── app.py
├── train_model.py
├── Dockerfile
├── requirements.txt
├── .pre-commit-config.yaml
├── .flake8
└── README.md
```
