import sqlite3
import pandas as pd

DB_PATH = "data/analytics.db"


def query_db(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def user_usage():
    query = """
    SELECT
        "attr.user.email" AS user,
        COUNT(*) AS total_requests,
        SUM("attr.input_tokens") AS input_tokens,
        SUM("attr.output_tokens") AS output_tokens,
        SUM("attr.cost_usd") AS total_cost
    FROM events
    WHERE event_type = 'claude_code.api_request'
    GROUP BY user
    ORDER BY total_requests DESC
    """

    return query_db(query)


def practice_usage():
    query = """
    SELECT
        practice,
        SUM("attr.input_tokens" + "attr.output_tokens") AS total_tokens,
        SUM("attr.cost_usd") AS total_cost
    FROM events
    WHERE event_type = 'claude_code.api_request'
    GROUP BY practice
    ORDER BY total_tokens DESC
    """

    return query_db(query)


def model_usage():
    query = """
    SELECT
        "attr.model" AS model,
        COUNT(*) AS requests,
        SUM("attr.input_tokens" + "attr.output_tokens") AS tokens
    FROM events
    WHERE event_type = 'claude_code.api_request'
    GROUP BY model
    ORDER BY requests DESC
    """

    return query_db(query)


def hourly_usage():
    query = """
    SELECT
        hour,
        COUNT(*) AS requests,
        SUM("attr.input_tokens" + "attr.output_tokens") AS tokens
    FROM events
    WHERE event_type = 'claude_code.api_request'
    GROUP BY hour
    ORDER BY hour
    """

    return query_db(query)


def tool_usage():
    query = """
    SELECT
        "attr.tool_name" AS tool,
        COUNT(*) AS tool_calls,
        AVG("attr.tool_result_size_bytes") AS average_result_size_bytes,
        AVG("attr.success") AS success_rate
    FROM events
    WHERE event_type = 'claude_code.tool_result'
    GROUP BY tool
    ORDER BY tool_calls DESC
    """

    return query_db(query)


def error_rate():
    query = """
    SELECT
        COUNT(*) AS total_errors
    FROM events
    WHERE event_type = 'claude_code.api_error'
    """

    return query_db(query)


def top_expensive_users():
    query = """
    SELECT 
        "attr.user.email" AS user_email,
        SUM("attr.cost_usd") AS total_cost,
        SUM("attr.input_tokens" + "attr.output_tokens") AS total_tokens,
        COUNT(*) AS requests
    FROM events
    WHERE event_type = 'claude_code.api_request'
    GROUP BY user_email
    ORDER BY total_cost DESC
    LIMIT 10
    """

    return query_db(query)


def token_usage_trend():
    query = """
    SELECT
        DATE("attr.event.timestamp") AS date,
        SUM("attr.input_tokens" + "attr.output_tokens") AS tokens,
        SUM("attr.cost_usd") AS cost
    FROM events
    WHERE event_type = 'claude_code.api_request'
    GROUP BY date
    ORDER BY date
    """

    return query_db(query)


def model_efficiency():
    query = """
    SELECT
        "attr.model" AS model,
        SUM("attr.input_tokens" + "attr.output_tokens") AS tokens,
        SUM("attr.cost_usd") AS cost,
        SUM("attr.input_tokens" + "attr.output_tokens") / SUM("attr.cost_usd") AS tokens_per_dollar
    FROM events
    WHERE event_type = 'claude_code.api_request'
    GROUP BY model
    ORDER BY tokens_per_dollar DESC
    """

    return query_db(query)
