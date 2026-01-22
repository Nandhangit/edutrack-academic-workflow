<!-- # edutrack-academic-workflow
EduTrack is a role-based academic records management system built with Django and Django REST Framework, implementing secure workflows for students, faculty, and administrators. -->

# 🎓 EduTrack – Academic Records & Workflow Engine

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/REST_API-000000?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

<!-- <p align="center">
  <b>A role-based academic management backend implementing real-world workflows using Django REST Framework</b>
</p>

---
**EAGLE**
![Image](https://github.com/user-attachments/assets/d15a5687-2d91-4eb7-af84-6db6e95c5619)

## 🚀 Project Overview

*EduTrack* is a backend-focused academic records management system that demonstrates  
*Role-Based Access Control (RBAC), **secure authentication, and **approval workflows*  
commonly used in real-world education platforms.

This project strictly separates responsibilities between *Students, **Faculty, and **Admins*  
and enforces access rules at the API level.

---

## 🧠 Core Concept

> 🔐 Authentication identifies the user  
> 🎭 Authorization (role) decides what the user can do

---

## 🧑‍🤝‍🧑 User Roles & Capabilities

| Role | Capabilities |
|---|---|
🎓 *Student* | View enrolled courses and approved results |
🧑‍🏫 *Faculty* | Enter marks and create academic records |
🛡 *Admin* | Approve records and manage the system |

---
## 🔁 System Workflow

```text
Admin creates users & courses
        ↓
Student enrolls in courses
        ↓
Faculty enters marks
        ↓
Admin approves records
        ↓
Student views final results -->

# 🎓 EduTrack – Academic Records & Role-Based Workflow System

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

```http
Authorization: Bearer <access_token>

