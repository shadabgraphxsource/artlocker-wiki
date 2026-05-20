# tools/search.py
# Art Locker LLM Wiki — Search Script
# Usage: python tools/search.py "search term"

import os
import sys
import re

WIKI_DIR = "wiki"

def search_wiki(query):
    """Search all wiki .md files for query"""
    results = []
    query_lower = query.lower()

    for root, dirs, files in os.walk(WIKI_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)

            # Try utf-8 first, fallback to cp1252 (Windows default)
            for encoding in ["utf-8", "cp1252", "latin-1"]:
                try:
                    with open(filepath, "r", encoding=encoding) as f:
                        lines = f.readlines()
                    break
                except (UnicodeDecodeError, Exception):
                    continue
            else:
                print(f"  ⚠️  Skipping unreadable file: {file}")
                continue

            matches = []
            for i, line in enumerate(lines):
                if query_lower in line.lower():
                    matches.append({
                        "line_num": i + 1,
                        "line": line.strip()
                    })

            if matches:
                results.append({
                    "file": filepath,
                    "match_count": len(matches),
                    "matches": matches[:3]
                })

    results.sort(key=lambda x: x["match_count"], reverse=True)
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/search.py \"your search term\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    print(f"\n🔍 Searching wiki for: '{query}'")
    print("=" * 40)

    results = search_wiki(query)

    if not results:
        print(f"No results found for '{query}'")
        return

    print(f"Found {len(results)} files with matches:\n")
    for r in results:
        print(f"📄 {r['file']} ({r['match_count']} matches)")
        for m in r["matches"]:
            print(f"   Line {m['line_num']}: {m['line'][:80]}")
        print()

if __name__ == "__main__":
    main()