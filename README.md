# 🔍 Log Analyser 

A Python project to analyse **web server (Apache)** and **Linux auth logs** for suspicious activity.

## Features
- Detects log type automatically (Apache vs Auth).
- Apache: flags high-traffic IPs and generates traffic graphs.
- Auth: detects brute force SSH attempts (>5 failed logins from same IP).
- Saves reports as `.png` charts in `output_reports/`.

## Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Analyse Apache log
python analyser.py logs/sample_apache.log

# Analyse Auth log
python analyser.py logs/sample_auth.log

#Generates A Random Sample Log
python generator.py
#Creates Logs/sample.log you can analyse
python analyser.py logs/sample.log
