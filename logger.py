import os
import csv
from datetime import datetime

LOG_FILE = "chat_log.csv"

def log_chat(session_id: str, query: str, response: str, is_crisis: bool):
    file_exists = os.path.isfile(LOG_FILE)

    try:
        with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

            # Write header only once
            if not file_exists:
                writer.writerow(["timestamp", "session_id", "query", "response", "crisis_flag"])

            # Clean text (important for CSV safety)
            clean_query = query.replace("\n", " ").strip()
            clean_response = response.replace("\n", " ").strip()

            writer.writerow([
                datetime.now().isoformat(),
                session_id,
                clean_query,
                clean_response,
                int(is_crisis)  # better than string
            ])

    except Exception as e:
        print(f"Logging failed: {e}")