import pandas as pd
from src.analytics.time_metrics import compute_time_metrics
from src.analytics.tool_metrics import compute_tool_metrics
from src.analytics.usage_metrics import compute_user_metrics
from src.analytics.model_metrics import compute_model_metrics
from src.analytics.practice_metrics import compute_practice_metrics


def generate_metrics():

    print("Loading processed dataset...")

    df = pd.read_csv("data/processed/processed_events.csv")

    print("Computing user metrics...")
    user_metrics = compute_user_metrics(df)

    print("Computing model metrics...")
    model_metrics = compute_model_metrics(df)

    print("Computing practice metrics...")
    practice_metrics = compute_practice_metrics(df)

    print("Computing tool metrics...")
    tool_metrics = compute_tool_metrics(df)

    print("Computing time metrics...")
    time_metrics = compute_time_metrics(df)

    print("Saving metrics...")

    user_metrics.to_csv("data/metrics/user_metrics.csv", index=False)
    model_metrics.to_csv("data/metrics/model_metrics.csv", index=False)
    practice_metrics.to_csv("data/metrics/practice_metrics.csv", index=False)
    tool_metrics.to_csv("data/metrics/tool_metrics.csv", index=False)
    time_metrics.to_csv("data/metrics/time_metrics.csv", index=False)

    print("Metrics generated successfully!")


if __name__ == "__main__":
    generate_metrics()
