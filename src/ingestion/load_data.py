import json


def load_jsonl(file_path):
    records = []

    with open(file_path, "r") as f:
        for line in f:
            records.append(json.loads(line))

    return records
