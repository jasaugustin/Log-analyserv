import random
import time

ips = ["127.0.0.1", "192.168.0.45", "203.0.113.77", "10.0.0.22"]
endpoints = ["/", "/index.html", "/login", "/admin", "/dashboard"]
status_codes = [200, 403, 404, 500]

def generate_log_line():
    ip = random.choice(ips)
    endpoint = random.choice(endpoints)
    status = random.choice(status_codes)
    return f'{ip} - - [12/Sep/2025:10:0{random.randint(0,9)}:01] "GET {endpoint} HTTP/1.1" {status} {random.randint(64,2048)}'

with open("logs/sample.log", "w") as f:
    for _ in range(50):
        f.write(generate_log_line() + "\n")

print("✅ sample.log generated in logs/")
# Simulate real-time log generation