import streamlit as st
from src.analytics.sql_queries import user_usage, hourly_usage, tool_usage, practice_usage, error_rate, model_usage

st.title("LLM Usage Analytics Dashboard")

st.header("User Usage")

users = user_usage()
st.dataframe(users)


st.header("Practice Usage")

practice = practice_usage()
st.bar_chart(practice.set_index("practice")["total_tokens"])


st.header("Model Usage")

model = model_usage()
st.dataframe(model)


st.header("Hourly Usage")

hourly = hourly_usage()
st.line_chart(hourly.set_index("hour")["tokens"])


st.header("Tool Usage")

tools = tool_usage()
st.dataframe(tools)


st.header("Errors")

errors = error_rate()
st.write(errors)
