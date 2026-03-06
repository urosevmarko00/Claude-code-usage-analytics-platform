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

    print("Creating indexes...")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_event_type
        ON events(event_type)
        """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_user_email
        ON events("attr.user.email")
        """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_model
        ON events("attr.model")
        """)

    conn.commit()
    conn.close()

    print("Data loaded into SQLite successfully with indexes")


if __name__ == "__main__":
    load_processed_events()
