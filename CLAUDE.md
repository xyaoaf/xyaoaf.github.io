# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based academic personal website for Xihan Yao (姚希翰), a PhD student at UT Austin, hosted on GitHub Pages at https://xyaoaf.github.io. It is based on the [AcademicPages](https://academicpages.github.io/) template (forked from Minimal Mistakes Jekyll theme).

## Local Development

```bash
bundle clean              # Clean build directory
bundle install            # Install Ruby dependencies
bundle exec jekyll liveserve  # Serve at localhost:4000 with live reload
```

Pushing to `master` triggers automatic deployment via GitHub Pages — no manual build step needed.

## Generating Content

Publications and talks can be generated from TSV source files:

```bash
cd markdown_generator
python publications.py   # Generates _publications/*.md from publications.tsv
python talks.py          # Generates _talks/*.md from talks.tsv
python pubsFromBib.py    # Alternative: generate from .bib file
```

The interactive journey map is generated separately:

```bash
python files/journey_map_folium.py   # Outputs files/journey_map.html
```

Location data lives in `files/journey_locations.py`.

## Architecture

**Content collections** (`_posts/`, `_publications/`, `_talks/`, `_teaching/`, `_portfolio/`) hold Markdown files with YAML front matter. Jekyll builds them into static HTML using layouts in `_layouts/` and partials in `_includes/`.

**Key config files:**
- `_config.yml` — site-wide settings (author info, URL, collections, plugins, analytics)
- `_config.dev.yml` — development overrides
- `_data/navigation.yml` — site navigation menu
- `_data/authors.yml` — author profile data

**Content source of truth:**
- `markdown_generator/publications.tsv` → `_publications/` (via `publications.py`)
- `markdown_generator/talks.tsv` → `_talks/` (via `talks.py`)
- `files/journey_locations.py` → `files/journey_map.html` (via `journey_map_folium.py`)

**Pages** live in `_pages/`. Active pages (all linked from navigation or serving a clear purpose):

| File | Permalink | Purpose |
|------|-----------|---------|
| `Home.md` | `/` | Landing page with news feed |
| `About-Me.md` | `/self-intro/` | Research bio |
| `News-Posts.html` | `/News-Posts/` | Posts grouped by year |
| `publications.md` | `/publications/` | Publications list |
| `teaching.md` | `/teaching/` | Teaching experience |
| `connecting-the-dots.md` | `/connecting-the-dots/` | Three.js knowledge web — nav entry "Connecting the Dots" |
| `journey.md` | `/journey/` | Embeds the Folium journey map (not in nav; linked internally) |
| `cv.md` | `/cv/` | CV page (nav links to PDF instead) |
| `404.md` | `/404.html` | Custom 404 page |

## Publication Conventions

Publications are numbered in reverse chronological order (newest = highest number). Current count: 5 publications (next would be [6]).

File naming: `YYYY-MM-DD-paper-N-short-title.md`

Front matter template:
```yaml
---
title: "[N] Paper Title"
collection: publications
permalink: /publication/YYYY-short-title
excerpt: 'Brief description.'
date: YYYY-MM-DD
venue: 'Journal or Conference Name'
paperurl: 'DOI or Google Scholar link'
citation: 'APA format citation'
---
```

## Maintenance Workflows

### Adding a blog post
Create `_posts/YYYY-MM-DD-short-title.md` with front matter:
```yaml
---
title: "Post Title"
date: YYYY-MM-DD
permalink: /posts/YYYY/MM/short-title/
tags:
  - tag1
---
```

### Adding a publication
1. Add a row to `markdown_generator/publications.tsv`
2. Run `cd markdown_generator && python publications.py`
3. Or manually create `_publications/YYYY-MM-DD-paper-N-short-title.md` (next number is [6])

### Adding a talk
1. Add a row to `markdown_generator/talks.tsv`
2. Run `cd markdown_generator && python talks.py`
3. Or manually create `_talks/YYYY-MM-DD-talk-short-title.md`

### Updating the journey map
1. Edit location data in `files/journey_locations.py`
2. Run `python files/journey_map_folium.py` — this overwrites `files/journey_map.html`
3. Commit both the updated `.py` and `.html` files

### Adding a teaching entry
Create `_teaching/YYYY-MM-DD-course-name.md` — it will auto-appear on the Teaching page and CV.

### Updating navigation
Edit `_data/navigation.yml`. Each entry needs `title:` and `url:`.

## Styling

SASS source is in `_sass/`. Compiled CSS lives in `assets/css/`. JavaScript is in `assets/js/`. To minify JS:

```bash
npm run build:js    # Minify assets/js/
npm run watch:js    # Watch for changes
```
