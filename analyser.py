import sys
from suspicious import detect_suspicious
from visualiser import plot_requests_per_ip
import pandas as pd

from parsers.apacheParser import parse_apache_log
from parsers.logParser import parse_log
import re
from parsers.authParser import parse_auth_log

def detect_bruteforce(df: pd.DataFrame):
    """Detect brute force SSH attempts (too many failures from same IP)."""
    failed = df[df["status"] == "failed"]
    suspicious = failed["ip"].value_counts()
    return suspicious[suspicious > 5]  # threshold

def guess_log_type(filepath: str) -> str:
    with open(filepath, "r") as f:
        sample = f.read(500).lower()  # lowercase for matching
        if "sshd" in sample or "failed password" in sample or "accepted password" in sample:
            return "auth"
        if any(method in sample for method in ["get", "post", "head", "put", "delete", "http"]):
            return "apache"
    return "unknown"

def main(log_file):
    log_type = guess_log_type(log_file)
    print(f"🔍 Detected log type: {log_type}")

    if log_type == "apache":
        df = parse_apache_log(log_file)
    elif log_type == "auth":
        df = parse_auth_log(log_file)
    else:
        print("❌ Could not determine log type. Please check the file.")
        return

    if df.empty:
        print("❌ No valid log entries found.")
        return

    print("✅ Parsed log file successfully.")

    if log_type == "apache":
        alerts = detect_suspicious(df)
        if alerts:
            print("\n🚨 Suspicious Activity Detected (Apache logs):")
            for alert in alerts:
                print(alert)
        else:
            print("\n✅ No suspicious activity found in Apache logs.")
        plot_requests_per_ip(df)
        print("📊 Apache traffic report saved to output_reports/traffic.png")
    elif log_type == "auth":
        brute_ips = detect_bruteforce(df)
        if not brute_ips.empty:
            print("\n🚨 Possible brute force detected:")
            for ip, count in brute_ips.items():
                print(f"- {ip} → {count} failed attempts")
        else:
            print("\n✅ No brute force attempts detected in auth logs.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyser.py logs/sample.log")
    else:
        main(sys.argv[1])