# 🛒 Walmart Data Pipeline using Python & SQLite

## 📌 Overview

This project demonstrates an **ETL (Extract, Transform, Load)** pipeline developed as part of the **Walmart USA Software Engineering Virtual Experience Program (Forage)**.

The application reads shipping data from multiple CSV spreadsheets, transforms the information into a normalized structure, and loads it into an SQLite relational database.

---

# 🚀 Features

- Read multiple CSV files using Pandas
- Merge shipment datasets
- Transform raw shipment data
- Calculate product quantities
- Populate an SQLite database
- Apply database normalization concepts
- Automate the complete ETL workflow

---

# 🛠 Technologies Used

- Python 3
- Pandas
- SQLite3
- SQL
- Git & GitHub

---

# 📂 Project Structure

```
data/
database/
screenshots/
populate_database.py
requirements.txt
README.md
```

---

# ⚙️ Workflow

```text
CSV Files
     │
     ▼
Read using Pandas
     │
     ▼
Merge Datasets
     │
     ▼
Transform Data
     │
     ▼
Calculate Product Quantities
     │
     ▼
Insert into SQLite Database
```

---

# 🗄 Database Schema

## Product

| Column |
|---------|
| Product ID |
| Product Name |

---

## Shipment

| Column |
|---------|
| Product ID |
| Quantity |
| Origin |
| Destination |

---

# 📈 Skills Demonstrated

- ETL Pipeline Development
- Data Processing
- Database Normalization
- SQL
- SQLite
- Python Automation
- Data Transformation
- Relational Database Design

---

# ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/walmart-data-pipeline-sqlite.git
```

Install dependencies

```bash
pip install pandas
```

Run

```bash
python populate_database.py
```

---

# 📷 Screenshots

-workflow diagram 
<img width="240" height="732" alt="workflow drawio" src="https://github.com/user-attachments/assets/e6f0f92f-88d8-49ad-8406-3c2b05aea492" />

- ERD
- <img width="202" height="452" alt="erd drawio" src="https://github.com/user-attachments/assets/65742171-38d5-4a8a-8191-2a0bdfae1540" />

-Database Tables

- Terminal Output
<img width="1600" height="1049" alt="output" src="https://github.com/user-attachments/assets/02c59992-84ab-4a8a-80cf-1130590b01a5" />

---

# 👩‍💻 Author

**Puppala Sanjana**

B.Tech Computer Science Engineering

Data Analytics | Python | SQL basics | Power BI | AI

LinkedIn:
(https://www.linkedin.com/in/puppalasanjana)

GitHub:
(https://www.github.com/in/PuppalaSanjana)
