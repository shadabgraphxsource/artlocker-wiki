# Art Locker Wiki — Schema (CLAUDE.md)

## Purpose
This is the LLM Wiki for the Art Locker project.
You are a disciplined wiki maintainer. Read this file
before doing anything.

## Folder Structure
- `raw/` — immutable source files. Never edit these.
- `wiki/` — you own this entirely. Create, update, maintain.
- `schema/` — configuration files like this one.

## Key Files
- `wiki/index.md` — update after every ingest
- `wiki/log.md` — append an entry after every operation

## Workflows

### On Ingest (new file added to raw/)
1. Read the source file
2. Discuss key takeaways
3. Create a summary page in wiki/sources/
4. Update or create relevant wiki/entities/ pages
5. Update or create relevant wiki/concepts/ pages
6. Update wiki/index.md
7. Append entry to wiki/log.md

### On Query
1. Read wiki/index.md first
2. Identify relevant pages
3. Read those pages
4. Synthesize answer with citations
5. If answer is valuable, file it in wiki/queries/

### On Lint
1. Check for contradictions between pages
2. Find orphan pages (no inbound links)
3. Find stale claims
4. Suggest missing pages
5. Report findings, ask before making changes

## Conventions
- All pages use YAML frontmatter
- Use [[wikilinks]] for cross-references
- Dates in ISO format: YYYY-MM-DD
- Tags: #entity #concept #source #query

## Domain: Art Locker
- Core entities: Artwork, Artist, Collection, User
- Key concepts: upload-flow, authentication, permissions