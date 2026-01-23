
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
| Database | MySQL |
| Testing | Postman |
| Version Control | Git & GitHub |

---

## 🔐 Authentication & Authorization

### Authentication
- JWT (JSON Web Tokens)
- Token sent via request headers

## Screenshots 🖥️
## Admin Access🎟️

![Image](https://github.com/user-attachments/assets/d98ca2a8-3c3f-4f7d-8827-33073cfbc7af)

## Faculty Access 👤

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/a68506b7-717c-40f0-b834-ba1ddd919944" />

## Student Course Enrollment 📒
![Image](https://github.com/user-attachments/assets/e741d036-1a08-48c8-a10f-9c690c40a004)


## Student Access and Show our Marks 💯

![Image](https://github.com/user-attachments/assets/5b651f1a-d60d-4ab3-886d-02803a7d0ab7)

## Student Only Access for Get our Marks ..✔️
## Don't Access Other students Marks, Don't changes in Our Marks.. ❌

![Image](https://github.com/user-attachments/assets/b35685b5-e4cb-46d6-9898-45aab875062b)
