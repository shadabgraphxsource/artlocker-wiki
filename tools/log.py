# tools/log.py
# Art Locker LLM Wiki — Log Entry
# Usage: python tools/log.py "ingest" "Meeting Notes Jan 2026"

import sys
from datetime import datetime

LOG_FILE = "wiki/log.md"

def append_log(operation, title):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    entry = f"\n## [{timestamp}] {operation} | {title}\n"
    entry += f"- Added: {datetime.now().strftime('%H:%M')}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"✅ Log updated: [{timestamp}] {operation} | {title}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python tools/log.py \"operation\" \"title\"")
        print("Example: python tools/log.py \"ingest\" \"Meeting Notes\"")
        sys.exit(1)
    append_log(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()