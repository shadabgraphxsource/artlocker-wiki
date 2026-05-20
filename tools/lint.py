# tools/lint.py
# Art Locker LLM Wiki — Lint / Health Check
# Usage: python tools/lint.py

import os
import re
from datetime import datetime

WIKI_DIR = "wiki"

def get_all_wiki_pages():
    """Get all wiki page names"""
    pages = {}
    for root, dirs, files in os.walk(WIKI_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                name = file.replace(".md", "")
                pages[name] = filepath
    return pages

def get_wikilinks(filepath):
    """Extract all [[wikilinks]] from a file"""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return re.findall(r'\[\[([^\]]+)\]\]', content)

def check_orphans(pages):
    """Find pages with no inbound links"""
    inbound = {name: 0 for name in pages}
    for name, filepath in pages.items():
        links = get_wikilinks(filepath)
        for link in links:
            if link in inbound:
                inbound[link] += 1
    return [
        name for name, count in inbound.items()
        if count == 0 and name not in ["index", "log"]
    ]

def check_broken_links(pages):
    """Find [[links]] that point to non-existent pages"""
    broken = []
    for name, filepath in pages.items():
        links = get_wikilinks(filepath)
        for link in links:
            if link not in pages:
                broken.append({
                    "in_file": name,
                    "broken_link": link
                })
    return broken

def check_empty_sections(pages):
    """Find pages with placeholder content"""
    placeholders = ["Rule 1", "Takeaway 1", "Question 1", "One paragraph"]
    flagged = []
    for name, filepath in pages.items():
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        found = [p for p in placeholders if p in content]
        if found:
            flagged.append({
                "file": name,
                "placeholders": found
            })
    return flagged

def main():
    print("\n🏥 Art Locker Wiki — Lint Report")
    print("=" * 40)
    print(f"🕐 Run at: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    pages = get_all_wiki_pages()
    print(f"📄 Total wiki pages : {len(pages)}")

    # Orphan pages
    orphans = check_orphans(pages)
    print(f"\n⚠️  Orphan pages ({len(orphans)}):")
    if orphans:
        for o in orphans:
            print(f"   - {o}")
    else:
        print("   ✅ None found")

    # Broken links
    broken = check_broken_links(pages)
    print(f"\n🔗 Broken links ({len(broken)}):")
    if broken:
        for b in broken:
            print(f"   - [[{b['broken_link']}]] in {b['in_file']}")
    else:
        print("   ✅ None found")

    # Placeholder content
    flagged = check_empty_sections(pages)
    print(f"\n📝 Pages with placeholders ({len(flagged)}):")
    if flagged:
        for f in flagged:
            print(f"   - {f['file']}: {', '.join(f['placeholders'])}")
    else:
        print("   ✅ None found")

    print("\n✅ Lint complete!")

if __name__ == "__main__":
    main()