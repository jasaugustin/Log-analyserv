import re
import pandas as pd

def parse_apache_log(filepath: str) -> pd.DataFrame:
    """Parse Apache log file into structured DataFrame."""
    log_pattern = re.compile(
        r'(?P<ip>\S+) - - \[(?P<date>.*?)\] "(?P<method>\S+) (?P<endpoint>\S+) (?P<protocol>[^"]+)" (?P<status>\d{3}) (?P<size>\d+)'
    )
    rows = []
    with open(filepath, "r") as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                rows.append(match.groupdict())

    df = pd.DataFrame(rows)
    if not df.empty:
        df["status"] = df["status"].astype(str)  # keep consistent with suspicious.py
    return df
