import re 
import pandas as pd 

def parse_auth_log(filepath: str) -> pd.DataFrame:
    """Parse Linux auth.log for SSH activity."""
    pattern = re.compile(
        r'(?P<month>\w{3})\s+(?P<day>\d{1,2})\s+(?P<time>\d{2}:\d{2}:\d{2}) '
        r'(?P<host>\S+) sshd\[\d+\]: (?P<message>.+)'
    )

    rows = []
    with open(filepath, "r") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                rows.append(match.groupdict())

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    # Extract IPs and status
    df["ip"] = df["message"].str.extract(r'from (\d+\.\d+\.\d+\.\d+)')
    df["status"] = df["message"].apply(
        lambda x: "failed" if "Failed password" in x else
                  "accepted" if "Accepted password" in x else "other"
    )
    return df