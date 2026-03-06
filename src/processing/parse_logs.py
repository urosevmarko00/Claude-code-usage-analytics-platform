import json
import pandas as pd


def extract_events(records):
    allowed_events = {
        "claude_code.api_request",
        "claude_code.api_error",
        "claude_code.tool_result"
    }
    events = []

    for record in records:

        log_events = record.get("logEvents", [])

        for event in log_events:
            try:
                message_json = json.loads(event["message"])
            except json.JSONDecodeError:
                continue

            event_type = message_json.get("body")
            if event_type not in allowed_events:
                continue

            event_data = {
                "timestamp": event["timestamp"],
                "event_type": message_json.get("body"),
                "attributes": message_json.get("attributes", {}),
                "resource": message_json.get("resource", {})
            }

            events.append(event_data)

    return pd.DataFrame(events)


def normalize_events(df):
    attributes_df = pd.json_normalize(df["attributes"]).add_prefix("attr.")
    resource_df = pd.json_normalize(df["resource"]).add_prefix("res.")

    df = pd.concat(
        [
            df.drop(columns=["attributes", "resource"]),
            attributes_df,
            resource_df
        ],
        axis=1
    )

    return df


def clean_dataset(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["hour"] = df["timestamp"].dt.hour

    numeric_cols = [
        "attr.input_tokens",
        "attr.output_tokens",
        "attr.duration_ms",
        "attr.cost_usd"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df[numeric_cols] = df[numeric_cols].fillna(0)

    return df
