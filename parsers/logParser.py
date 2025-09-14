import re
import pandas as pd

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>.*?)\] "(?P<method>\w+) (?P<endpoint>\S+) HTTP.*" (?P<status>\d+) (?P<size>\d+)'
)

def parse_log(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                data.append(match.groupdict())
    df = pd.DataFrame(data)
    df["size"] = df["size"].astype(int)
    df["status"] = df["status"].astype(int)
    return df
