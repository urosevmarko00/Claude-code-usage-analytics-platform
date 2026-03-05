def compute_practice_metrics(df):
    api_df = df[df["event_type"] == "claude_code.api_request"]

    metrics = (
        api_df.groupby("practice").agg(
            total_requests=("event_type", "count"),
            total_input_tokens=("attr.input_tokens", "sum"),
            total_output_tokens=("attr.output_tokens", "sum"),
            total_cost=("attr.cost_usd", "sum"),
            avg_duration_ms=("attr.duration_ms", "mean")
        ).reset_index()
    )

    metrics["total_tokens"] = (metrics["total_input_tokens"] + metrics["total_output_tokens"])

    metrics = metrics.fillna(0)

    return metrics
