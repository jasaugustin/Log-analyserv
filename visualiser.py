import matplotlib.pyplot as plt

def plot_requests_per_ip(df, output_path="output_reports/traffic.png"):
    counts = df["ip"].value_counts().head(5)
    counts.plot(kind="bar", title="Top 5 IPs by Request Count")
    plt.ylabel("Requests")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
