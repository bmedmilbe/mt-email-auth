# Multi-Tenant Email Auth Backend

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0+-092e20.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791.svg)](https://www.postgresql.org/)
[![AWS S3](https://img.shields.io/badge/AWS_S3-Managed-FF9900.svg)](https://aws.amazon.com/s3/)
[![CI/CD](https://img.shields.io/badge/GitHub_Actions-Automated-2088FF.svg)](https://github.com/features/actions)

A robust, production-grade multi-tenant authentication system built with **Python**, **Django**, and **PostgreSQL 17**. This backend serves as a centralized hub for multiple web applications (tenants), providing secure data isolation and cloud-native scalability.

## 🚀 Active Tenants
The system currently orchestrates and serves data for:
* **Camara Mé-Zóchi:** Municipal government council for the Mé-Zóchi district, STP.
* **CECAB-STP:** Organic Cocoa Export Cooperative (Fair-trade organization).

---

## 🏗️ Infrastructure & DevOps

### 🔐 Security & Identity Management
* **Principle of Least Privilege:** Implemented granular **AWS IAM Policies** to restrict application access to specific S3 buckets, preventing broad account exposure.
* **Environment Secret Management:** Sensitive credentials (DB strings, AWS keys) are managed via **GitHub Actions Secrets** and Railway Environment Variables, ensuring zero plain-text exposure in the codebase.

### 💾 Storage Strategy (Hybrid Architecture)
* **Stateless Design:** The application is fully stateless, utilizing **Django-Storages** to offload persistent media to **Amazon S3**.
* **Cost Optimization (S3 Lifecycle):** Implemented **S3 Lifecycle Policies** to transition aging media (90+ days) to **Glacier Instant Retrieval**, reducing storage overhead by ~60% while maintaining millisecond access latency.
* **Static Assets:** Optimized delivery using **WhiteNoise** with Brotli compression for high-performance frontend serving.

### 🤖 Automation & Reliability
* **Nightly Backups:** Integrated a **GitHub Actions** workflow that performs nightly logical dumps of the **Postgres 17** database.
* **Version Parity:** Engineered the CI/CD runner to maintain version parity between the local client and the PostgreSQL 17 server, ensuring reliable, non-breaking database backups.
* **Disaster Recovery:** Backups are stored in an encrypted S3 bucket with automated **Expiration Policies** (30-day retention) to manage costs and data compliance.

---

## ✨ Key Features
* **Shared Logic, Isolated Data:** Manages multiple tenants within a single database instance using native PostgreSQL isolation.
* **Domain-Based Routing:** Automatically identifies the tenant based on the incoming request domain to serve correct branding and datasets.
* **Branding Management:** Centralized management for tenant-specific assets, including logos and dedicated SMTP configurations.
* **Enhanced Security:** JWT (JSON Web Tokens) for stateless authentication and hardened CORS/CSRF configurations for multi-domain production.

---

## 🛠 Setup & Installation

### Prerequisites
* Python 3.11+
* PostgreSQL 17+
* AWS IAM Credentials (for S3)

### 1. Clone the repository
```bash
git clone [https://github.com/bmedmilbe/mt-email-auth.git](https://github.com/bmedmilbe/mt-email-auth.git)
cd mt-email-auth