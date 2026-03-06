import streamlit as st
from src.utils.helpers import format_currency, format_tokens, format_rate
from src.analytics.forecasting import forecast_tokens
from src.analytics.sql_queries import user_usage, hourly_usage, tool_usage, practice_usage, error_rate, model_usage, \
    top_expensive_users, token_usage_trend, model_efficiency, cost_per_request


st.set_page_config(
    page_title="LLM Usage Analytics",
    layout="wide"
)

st.title("LLM Usage Analytics Dashboard")

# ---------------------------
# KPI METRICS
# ---------------------------

users = user_usage()
errors = error_rate()

total_requests = users["total_requests"].sum()
total_cost = users["total_cost"].sum()
total_tokens = users["input_tokens"].sum() + users["output_tokens"].sum()

total_tokens = format_tokens(total_tokens)
total_cost = format_currency(total_cost)
total_requests = format_tokens(total_requests)

errors["total_errors"] = errors["total_errors"].apply(format_tokens)

users["total_requests"] = users["total_requests"].apply(format_tokens)
users["input_tokens"] = users["input_tokens"].apply(format_tokens)
users["output_tokens"] = users["output_tokens"].apply(format_tokens)
users["total_cost"] = users["total_cost"].apply(format_currency)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Requests", total_requests)
col2.metric("Total Tokens", total_tokens)
col3.metric("Total Cost ($)", total_cost)
col4.metric("Total Errors", errors["total_errors"][0])

st.divider()

# ---------------------------
# USER ANALYTICS
# ---------------------------

st.header("User Analytics")

top_10 = top_expensive_users()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Most Expensive Users")
    st.bar_chart(top_10.set_index("user_email")["total_cost"])

with col2:
    st.subheader("User Request Table")
    st.dataframe(users)

st.divider()

# ---------------------------
# USAGE TREND
# ---------------------------

st.header("Usage Trend")

trend = token_usage_trend()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Token usage by date")
    st.line_chart(trend.set_index("date")["tokens"])
with col2:
    st.subheader("Costs by date")
    st.line_chart(trend.set_index("date")["cost"])

st.divider()

# ---------------------------
# FORECAST USAGE
# ---------------------------

st.header("Token Usage Forecast")

forecast = forecast_tokens()

st.dataframe(forecast)
st.line_chart(forecast.set_index("date")["predicted_tokens"])

st.divider()

# ---------------------------
# MODEL ANALYTICS
# ---------------------------

st.header("Model Analytics")

efficiency = model_efficiency()

cost_req = cost_per_request()
cost_req["total_requests"] = cost_req["total_requests"].apply(format_tokens)
cost_req["total_cost"] = cost_req["total_cost"].apply(format_currency)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Model Efficiency (tokens per $)")
    st.bar_chart(efficiency.set_index("model")["tokens_per_dollar"])
    st.subheader("Model Efficiency (cost per request)")
    st.bar_chart(cost_req.set_index("model")["cost_per_request"])

with col2:
    st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    st.subheader("Model Usage")
    model = model_usage()
    model["requests"] = model["requests"].apply(format_tokens)
    model["tokens"] = model["tokens"].apply(format_tokens)
    st.dataframe(model)

st.divider()

# ---------------------------
# PRACTICE ANALYTICS
# ---------------------------

st.header("Practice Analytics")

practice = practice_usage()

st.bar_chart(practice.set_index("practice")["total_tokens"])

st.divider()

# ---------------------------
# TOOL ANALYTICS
# ---------------------------

st.header("Tool Analytics")

tools = tool_usage()

tools["tool_calls"] = tools["tool_calls"].apply(format_tokens)
tools["average_result_size_bytes"] = tools["average_result_size_bytes"].apply(format_tokens)
tools["success_rate"] = tools["success_rate"].apply(format_rate)

st.dataframe(tools)

st.divider()

# ---------------------------
# HOURLY USAGE
# ---------------------------

st.header("Hourly Usage")

hourly = hourly_usage()

st.line_chart(hourly.set_index("hour")["tokens"])
