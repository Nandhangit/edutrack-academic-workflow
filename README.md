
# 🎓 EduTrack – Academic Records & Role-Based Workflow System

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/REST_API-000000?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

EduTrack is a *Django REST Framework backend application* designed to manage academic workflows using *Role-Based Access Control (RBAC)*.  
It models a real-world education system where *Students, **Faculty, and **Admins* have clearly defined responsibilities and permissions.

This project focuses on *secure APIs, **proper authorization, and **clean workflow enforcement*.

---

## 📌 Problem Statement

In academic systems:
- Students should not edit marks
- Faculty should not approve records
- Only Admins should finalize results

EduTrack solves this by enforcing *strict role-based permissions* at the API level.

---

## 🎯 Project Objectives

- Implement JWT-based authentication
- Enforce role-based authorization
- Design a real academic workflow
- Prevent unauthorized access
- Maintain clean separation of responsibilities

---

## 🧩 System Roles & Responsibilities

### 👨‍🎓 Student
- Enroll in courses
- View *only approved* academic results
- Cannot enter or modify marks

### 👩‍🏫 Faculty
- Enter marks & grades
- Create academic records
- Cannot approve records

### 👨‍💼 Admin
- Create users & courses
- Approve academic records
- Full system control

---

## 🛠️ Technology Stack

| Category | Technology |
|-------|------------|
| Language | Python |
| Framework | Django |
| API Framework | Django REST Framework |
| Authentication | JWT (SimpleJWT) |
| Database | SQLite (Development) |
| Testing | Postman |
| Version Control | Git & GitHub |

---

## 🔐 Authentication & Authorization

### Authentication
- JWT (JSON Web Tokens)
- Token sent via request headers


## SCREENSHOTS
![Image](https://github.com/user-attachments/assets/8b025b81-65b6-428f-9582-12b6680e3e6f)

