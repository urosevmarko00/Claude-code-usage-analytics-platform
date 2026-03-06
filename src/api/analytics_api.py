from fastapi import FastAPI
from src.analytics.sql_queries import (
    user_usage,
    model_usage,
    practice_usage,
    hourly_usage,
    top_expensive_users
)

app = FastAPI(
    title="LLM Usage Analytics API",
    description="API access to Claude Code telemetry analytics",
    version="1.0"
)


@app.get("/")
def root():
    return {"message": "LLM Analytics API running"}


@app.get("/users")
def users():
    return user_usage().to_dict(orient="records")


@app.get("/models")
def models():
    return model_usage().to_dict(orient="records")


@app.get("/practices")
def practices():
    return practice_usage().to_dict(orient="records")


@app.get("/hourly")
def hourly():
    return hourly_usage().to_dict(orient="records")


@app.get("/top-users")
def top_users():
    return top_expensive_users().to_dict(orient="records")
