# tools/ingest.py
# Art Locker LLM Wiki — Ingest Script
# Usage: python tools/ingest.py

import os
import json
from datetime import datetime

RAW_DIR = "raw"
WIKI_DIR = "wiki"
LOG_FILE = "wiki/log.md"
INDEX_FILE = "wiki/index.md"

def get_raw_files():
    """Scan all files in raw/ directory"""
    raw_files = []
    for root, dirs, files in os.walk(RAW_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            stat = os.stat(filepath)
            raw_files.append({
                "path": filepath,
                "name": file,
                "folder": os.path.relpath(root, RAW_DIR),
                "size_kb": round(stat.st_size / 1024, 2),
                "modified": datetime.fromtimestamp(
                    stat.st_mtime
                ).strftime("%Y-%m-%d %H:%M")
            })
    return raw_files

def get_wiki_sources():
    """Get already ingested sources from wiki/sources/"""
    sources_dir = os.path.join(WIKI_DIR, "sources")
    if not os.path.exists(sources_dir):
        return []
    return [
        f.replace(".md", "")
        for f in os.listdir(sources_dir)
        if f.endswith(".md")
    ]

def find_new_files(raw_files, ingested):
    """Find raw files not yet in wiki/sources/"""
    new_files = []
    for f in raw_files:
        name_clean = f["name"].replace(" ", "-").lower()
        name_no_ext = os.path.splitext(name_clean)[0]
        if name_no_ext not in ingested:
            new_files.append(f)
    return new_files

def append_log(entry):
    """Append entry to wiki/log.md"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    log_entry = f"\n## [{timestamp}] ingest | {entry}\n"
    log_entry += f"- Status: pending LLM processing\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    print(f"  📝 Log updated")

def main():
    print("\n🔍 Art Locker Wiki — Ingest Scanner")
    print("=" * 40)

    raw_files = get_raw_files()
    ingested = get_wiki_sources()

    print(f"📁 Raw files found     : {len(raw_files)}")
    print(f"✅ Already ingested    : {len(ingested)}")

    new_files = find_new_files(raw_files, ingested)
    print(f"🆕 New files to ingest : {len(new_files)}")
    print()

    if not new_files:
        print("Nothing new to ingest. Add files to raw/ first.")
        return

    print("Files ready for LLM ingestion:")
    print("-" * 40)
    for i, f in enumerate(new_files, 1):
        print(f"{i}. {f['name']}")
        print(f"   📂 Folder : {f['folder']}")
        print(f"   📦 Size   : {f['size_kb']} KB")
        print(f"   🕐 Modified: {f['modified']}")
        print()

    # Save report for LLM
    report = {
        "generated": datetime.now().isoformat(),
        "new_files": new_files,
        "total_raw": len(raw_files),
        "total_ingested": len(ingested)
    }
    with open("tools/ingest-report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("📄 Report saved to tools/ingest-report.json")

    # Log each new file
    for f in new_files:
        append_log(f["name"])

    print("\n✅ Done! Share ingest-report.json with Claude to process.")

if __name__ == "__main__":
    main()