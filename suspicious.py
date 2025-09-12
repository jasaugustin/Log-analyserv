def detect_suspicious(df):
    alerts = []

    # Rule 1: too many 404s
    failed_ips = df[df["status"] == "404"]["ip"].value_counts()
    for ip, count in failed_ips.items():
        if count > 3:
            alerts.append(f"⚠️ IP {ip} had {count} failed requests (possible scanning)")

    # Rule 2: too many login attempts
    login_attempts = df[df["endpoint"] == "/login"]["ip"].value_counts()
    for ip, count in login_attempts.items():
        if count > 5:
            alerts.append(f"⚠️ IP {ip} attempted {count} logins (possible brute force)")

    return alerts
