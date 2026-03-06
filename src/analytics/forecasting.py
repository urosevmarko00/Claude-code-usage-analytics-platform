import pandas as pd
from sklearn.linear_model import LinearRegression
from src.analytics.sql_queries import token_usage_trend


def forecast_tokens(days_ahead=7):

    df = token_usage_trend()

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    df["day_index"] = range(len(df))

    X = df[["day_index"]]
    y = df["tokens"]

    model = LinearRegression()

    model.fit(X, y)

    future_days = pd.DataFrame({
        "day_index": range(len(df), len(df) + days_ahead)
    })

    predictions = model.predict(future_days)

    future_dates = pd.date_range(
        start=df["date"].max(),
        periods=days_ahead+1,
        inclusive="right"
    )

    forecast_df = pd.DataFrame({
        "date": future_dates,
        "predicted_tokens": predictions
    })

    return forecast_df
