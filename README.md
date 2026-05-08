# Honeypot System

A cybersecurity project that simulates vulnerable network services to capture attacker activity, monitor intrusion attempts, and analyze malicious behavior through a SOC-style monitoring dashboard.

---

# Project Overview

The Honeypot System is designed to demonstrate practical cybersecurity monitoring and threat intelligence concepts using Python-based socket programming and web technologies.

This project simulates a fake vulnerable service that attracts attackers and records malicious login attempts. The captured attack data is stored in a database and visualized through an interactive dashboard for monitoring and analysis.

The project demonstrates concepts commonly used in:
- Security Operations Centers (SOC)
- Threat Hunting
- Intrusion Detection
- Security Monitoring
- Incident Response

---

# Key Features

## Honeypot Server
- Fake SSH/Telnet-style login service
- Simulates vulnerable network behavior
- Captures unauthorized login attempts
- Stores attacker credentials safely for analysis

## Intrusion Monitoring
- Logs attacker IP addresses
- Captures usernames and passwords
- Records timestamps of attacks
- Monitors repeated intrusion attempts

## Dashboard & Visualization
- SOC-style monitoring dashboard
- Displays attack statistics
- Visualizes intrusion activity
- Shows captured attack logs in real time

## Database Integration
- SQLite database storage
- Structured attack logging
- Efficient data retrieval system

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Backend Development |
| Flask | Web Dashboard Framework |
| SQLite | Database Management |
| Socket Programming | Honeypot Server |
| HTML/CSS | Frontend Interface |

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/advanced-honeypot-system.git
```

## Install Dependencies

```bash
pip install flask
```

---

# Running the Project

## Step 1 — Start the Honeypot Server

```bash
python honeypot.py
```

## Step 2 — Start the Dashboard

Open another terminal and run:

```bash
python dashboard.py
```

---

# Access the Dashboard

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Testing the Honeypot

Use Telnet to simulate attacks:

```bash
telnet 127.0.0.1 9999
```

Enter fake usernames and passwords.

The attack attempt will automatically appear in the dashboard.

---

# Attack Data Captured

The system records:

* Attacker IP Address
* Username Attempts
* Password Attempts
* Attack Timestamp

---

# Dashboard Features

* Total Attack Count
* Captured Credentials Table
* Attack Monitoring Logs
* Intrusion History Tracking
* Real-Time Attack Visualization

---

# Sample Attack Scenarios

The Honeypot can simulate monitoring for:

* Unauthorized Login Attempts
* Brute Force Attacks
* Credential Stuffing
* Suspicious Remote Access
* Repeated Authentication Failures

---

# Author

Y. Venkata Sai Rama Koteswara Rao

---

# License

This project is created for educational and portfolio purposes.

```
```
