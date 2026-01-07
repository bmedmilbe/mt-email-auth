# Multi-Tenant Email Auth Backend

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-336791.svg)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust multi-tenant authentication system built with **Python**, **Django**, and **PostgreSQL**. This backend serves as a centralized hub for multiple web applications (tenants), providing secure, isolated data and authentication while sharing a single application instance.



## 🚀 Active Tenants
This backend currently orchestrates and serves data for:
## 🚀 Active Tenants
The system currently serves as the backend for:

* **Camara Mé-Zóchi:** The municipal government council for the Mé-Zóchi district of São Tomé and Príncipe.
* **CECAB-STP:** The Organic Cocoa Export Cooperative, a leading fair-trade organization for organic cocoa farmers in São Tomé and Príncipe.

## 🏗 Architecture
* **Framework:** Python / Django (REST Framework)
* **Database:** PostgreSQL (Native multi-tenant isolation)
* **Authentication:** JWT (JSON Web Tokens) for secure, stateless sessions
* **Deployment:** Bare metal / VM deployment (Non-Dockerized)



## ✨ Key Features
* **Shared Logic, Isolated Data:** Efficiently manages multiple tenants within a single database instance using PostgreSQL's native capabilities.
* **Domain-Based Routing:** Automatically identifies the tenant based on the incoming request domain to serve the correct branding and dataset.
* **Branding Management:** Centralized management for tenant-specific assets, including logos, site titles, and dedicated SMTP configurations.
* **Enhanced Security:** Hardened CORS and CSRF configurations specifically tailored for multi-domain production environments.

## 🛠 Setup & Installation

### Prerequisites
* Python 3.9+
* PostgreSQL 13+
* Virtualenv

### 1. Clone the repository
```bash
git clone [https://github.com/bmedmilbe/mt-email-auth.git](https://github.com/bmedmilbe/mt-email-auth.git)
cd mt-email-auth