import pandas as pd


def format_currency(value):
    """
    Format numeric value as USD currency string.
    """
    if pd.isna(value):
        return "$0.00"

    return f"${value:,.2f}"


def format_tokens(value):
    """
    Format token counts with thousands separator.
    """
    if pd.isna(value):
        return "0"

    return f"{float(value):,.2f}"


def safe_divide(a, b):
    """
    Avoid division by zero.
    """
    if b == 0 or pd.isna(b):
        return 0

    return a / b


def preview_df(df, rows=5):
    """
    Quick dataframe preview for debugging.
    """
    print(df.head(rows))
    print("\nShape:", df.shape)