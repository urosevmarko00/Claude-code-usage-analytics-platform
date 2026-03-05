def compute_tool_metrics(df):
    api_df = df[df["event_type"] == "claude_code.tool_result"]

    metrics = (
        api_df.groupby("attr.tool_name").agg(
            tool_calls=("event_type", "count"),
            avg_result_size=("attr.tool_result_size_bytes", "mean"),
            success_rate=("attr.success", "mean")
        ).reset_index()
    )

    metrics = metrics.fillna(0)

    return metrics
