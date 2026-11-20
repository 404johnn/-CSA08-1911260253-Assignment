from pathlib import Path

def read_records(folder):
    records = []
    for path in sorted(Path(folder).glob("*.txt")):
        with path.open(encoding="utf-8") as f:
            records.extend(line.strip().split(",") for line in f if line.strip())
    return records
