---
title: "Collection"
type: entity
tags: [entity]
created: 2026-05-20
updated: 2026-05-20
sources: []
---

# Collection

## Overview
A curated group of artworks organized by an artist or curator.

## Properties
| Field       | Type     | Description           |
|-------------|----------|-----------------------|
| id          | uuid     | Unique identifier     |
| name        | string   | Collection name       |
| artist_id   | uuid     | Owner artist          |
| visibility  | enum     | public/private        |
| created_at  | datetime | Creation date         |

## Relationships
- **belongs to** → [[Artist]]
- **has many** → [[Artwork]]

## Open Questions
- [ ] Can collections be shared between artists?