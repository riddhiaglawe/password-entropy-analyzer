# 🔐 Password Entropy Calculator  
### Cyber Security & Digital Forensic Analysis Tool

A web-based Password Entropy Analyzer designed for Cyber Security and Digital Forensics applications.  
The system evaluates password strength using entropy calculation, simulates brute-force attacks, generates secure passwords, and exports forensic reports in PDF format.

---

## 🚀 Features

- 🔍 Real-time Password Entropy Calculation
- 📊 Strength Classification (Very Weak → Very Strong)
- ⏳ Estimated Crack Time Calculation
- 🛡 Brute-Force Attack Simulation
- 💡 Intelligent Improvement Suggestions
- 🔑 Secure Password Generator
- 🌙 Dark / Light Mode Toggle
- 📄 Forensic PDF Report Generation
- 📈 Visual Entropy Meter

---

## 🧠 How It Works

The system calculates password entropy using:

Entropy = Length × log₂(Character Set Size)

Character set size depends on:
- Lowercase letters (26)
- Uppercase letters (26)
- Numbers (10)
- Special Symbols (~32)

Higher entropy means:
✔ Larger keyspace  
✔ More brute-force resistance  
✔ Higher security  

---

## 🔥 Attack Simulation

The tool simulates password cracking using an estimated:
10 Billion guesses per second (GPU attack model)

It calculates:
Estimated crack time (in years)

---

## 📄 Forensic Report Generation

The system can generate a downloadable PDF report containing:

- Entropy value
- Strength level
- Estimated crack time
- Attack comparison
- Forensic feasibility conclusion

This makes the project relevant for digital forensic investigations.

---

## 🛠 Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- PDF Engine: ReportLab
- Version Control: Git & GitHub

---

## 📂 Project Structure
password-entropy-analyzer/
│
├── app.py # Main Flask backend application
├── requirements.txt # Project dependencies
├── templates/
│ └── index.html # Frontend HTML file
├── static/
│ └── style.css # CSS styling file
├── README.md # Project documentation
└── .gitignore # Files ignored by Git
