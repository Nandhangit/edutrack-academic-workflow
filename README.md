<!-- # edutrack-academic-workflow
EduTrack is a role-based academic records management system built with Django and Django REST Framework, implementing secure workflows for students, faculty, and administrators. -->

# 🎓 EduTrack – Academic Records & Workflow Engine

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/REST_API-000000?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

<p align="center">
  <b>A role-based academic management backend implementing real-world workflows using Django REST Framework</b>
</p>

---

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
Student views final results


