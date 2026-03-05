import pandas as pd
from src.ingestion.load_data import load_jsonl
from src.processing.parse_logs import extract_events, normalize_events, clean_dataset


def join_employees(events_df, employees_path):
    employees = pd.read_csv(employees_path)

    df = events_df.merge(employees, left_on="attr.user.email", right_on="email", how="left")

    return df


def build_dataset():
    records = load_jsonl("data/raw/telemetry_logs.jsonl")
    events_df = extract_events(records)
    events_df = normalize_events(events_df)
    events_df = clean_dataset(events_df)

    df = join_employees(events_df, "data/raw/employees.csv")

    df.to_csv("data/processed/processed_events.csv", index=False)

    print("Dataset built successfully")


if __name__ == "__main__":
    build_dataset()
