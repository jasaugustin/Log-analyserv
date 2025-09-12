import sys
from logParser import parse_log
from suspicious import detect_suspicious
from visualiser import plot_requests_per_ip

def main(log_file):
    df = parse_log(log_file)
    if df.empty:
        print("❌ No valid log entries found.")
        return

    print("✅ Parsed log file successfully.")
    alerts = detect_suspicious(df)

    if alerts:
        print("\n🚨 Suspicious Activity Detected:")
        for alert in alerts:
            print(alert)
    else:
        print("\n✅ No suspicious activity found.")

    plot_requests_per_ip(df)
    print("📊 Report saved to output_reports/traffic.png")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py logs/sample.log")
    else:
        main(sys.argv[1])
