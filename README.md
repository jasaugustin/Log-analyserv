# Log Analyser 

A Python project to analyse **web server (Apache)** and **Linux auth logs** for suspicious activity.
⚠️ Disclaimer: This tool is for educational and security research purposes only. Do not use it on systems without permission.

## Features
- Detects log type automatically (Apache vs Auth).
- Apache: flags high-traffic IPs and generates traffic graphs.
- Auth: detects brute force SSH attempts (>5 failed logins from same IP).
- Saves reports as `.png` charts in `output_reports/`.
---
## Installation
-Clone this repository:
```python
git clone https://github.com/jasaugustin/Log-analyserv.git
cd Log-analyserv
```
-Create virtual environment (Recommended) 
```python
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```
-Install Dependencies
```python
pip install -r requirements.txt
```
---
## Usage
```bash

# Analyse Apache log
python analyser.py logs/sample_apache.log

# Analyse Auth log
python analyser.py logs/sample_auth.log

#Generates A Random Sample Log
python generator.py
#Creates Logs/sample.log you can analyse
python analyser.py logs/sample.log
```
---
## Example Output

🔍 Detected log type: apache
✅ Parsed log file successfully.

🚨 Suspicious Activity Detected (Apache logs):
⚠️ IP 192.168.1.1 had 4 failed requests (possible scanning)
⚠️ IP 192.168.1.1 attempted 6 logins (possible brute force)

📊 Apache traffic report saved to output_reports/traffic.png

## Visual Reports
The tool generates a bar chart showing the Top 5 IPs by request count.
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/0de33af4-404a-4fba-9a6c-15ad18040790" />
