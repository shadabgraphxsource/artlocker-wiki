---
title: "Artwork"
type: entity
tags: [entity]
created: 2026-05-20
updated: 2026-05-20
sources: []
---

# Artwork

## Overview
Core entity representing a piece of art managed in Art Locker.

## Properties
| Field       | Type     | Description              |
|-------------|----------|--------------------------|
| id          | uuid     | Unique identifier        |
| title       | string   | Title of artwork         |
| artist_id   | uuid     | Reference to Artist      |
| media_type  | enum     | painting/digital/photo   |
| status      | enum     | draft/published/archived |
| created_at  | datetime | Upload timestamp         |

## Relationships
- **belongs to** → [[Artist]]
- **part of** → [[Collection]]
- **uploaded by** → [[User]]

## Open Questions
- [ ] What file formats are supported?
- [ ] Is there a file size limit?