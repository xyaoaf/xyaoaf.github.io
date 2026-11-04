# Publication Management Guide

## Current Publication Numbering System

Publications are numbered in reverse chronological order (most recent = highest number).

**Current Publications:**
- [6] 2026 - Big Five personality and built environment (Annals of the AAG)
- [5] 2025 - Community-scale microclimate simulation (Landscape and Urban Planning) — code: https://github.com/xyaoaf/UrbanTreeStudywithLidar
- [4] 2024 - Light pollution assessment Hong Kong (Energy & Environment) 
- [3] retired — Authorea preprint of [5], removed from the site after the journal version was published
- [2] 2023 - Urban forests microclimates Portland (IGARSS)
- [1] 2022 - Coastal chlorophyll-a UAV mapping (Journal of Hydro-Environment Research)

## Adding New Publications

When you publish new papers:

1. **Create new publication file**: Copy the template format from existing files
2. **Update numbering**: New paper gets the next number (currently [7]); retired entries do not cause later papers to be renumbered
3. **Update this documentation**: Add the new paper to the list above
4. **Follow APA format**: Maintain consistent citation style
5. **Include all required fields**: title, venue, date, citation, excerpt

## Template for New Publications

```markdown
---
title: "[NUMBER] Paper Title Here"
collection: publications
permalink: /publication/YYYY-short-title
excerpt: 'Brief description of the paper and its contributions.'
date: YYYY-MM-DD
venue: 'Journal or Conference Name'
paperurl: 'Google Scholar or DOI link'
citation: 'APA format citation'
---

Full description with abstract, key contributions, and research impact.

[View on Google Scholar](link)

**Recommended citation**: APA format citation.
```

## Google Scholar Integration

While automatic synchronization with Google Scholar isn't directly supported by Jekyll, you can:

1. **Manual Updates**: Check Google Scholar quarterly and update manually
2. **Citation Counts**: Link to Google Scholar for live citation metrics
3. **Profile Link**: Direct readers to Google Scholar for most current information

## File Naming Convention

Format: `YYYY-MM-DD-paper-N-short-title.md`
- YYYY-MM-DD: Publication date
- N: Publication number
- short-title: Abbreviated paper title

## Maintenance Schedule

Recommended: Update publication list every 3-6 months or when new papers are published.
