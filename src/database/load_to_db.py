import pandas as pd
from src.database.db_manager import get_connection


def load_processed_events():
    print("Loading dataset...")

    df = pd.read_csv("data/processed/processed_events.csv")

    conn = get_connection()

    df.to_sql(
        "events",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Data loaded into SQLite successfully")


if __name__ == "__main__":
    load_processed_events()
