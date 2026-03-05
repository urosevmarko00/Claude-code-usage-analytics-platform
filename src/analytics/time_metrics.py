import pandas as pd


def compute_time_metrics(df):
    api_df = df[df["event_type"] == "claude_code.api_request"]

    metrics = (
        api_df.groupby("hour").agg(
            total_requests=("event_type", "count"),
            total_input_tokens=("attr.input_tokens", "sum"),
            total_output_tokens=("attr.output_tokens", "sum"),
            total_cost=("attr.cost_usd", "sum")
        ).reset_index()
    )

    with pd.option_context('future.no_silent_downcasting', True):
        metrics = metrics.fillna(0).infer_objects(copy=False)

    return metrics
