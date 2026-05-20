---
title: "Artist"
type: entity
tags: [entity]
created: 2026-05-20
updated: 2026-05-20
sources: []
---

# Artist

## Overview
Represents a creator/artist who owns and manages artworks in Art Locker.

## Properties
| Field      | Type     | Description           |
|------------|----------|-----------------------|
| id         | uuid     | Unique identifier     |
| name       | string   | Full name             |
| email      | string   | Contact email         |
| bio        | text     | Artist biography      |
| created_at | datetime | Registration date     |

## Relationships
- **has many** → [[Artwork]]
- **has many** → [[Collection]]
- **is a** → [[User]]

## Open Questions
- [ ] Can one user have multiple artist profiles?