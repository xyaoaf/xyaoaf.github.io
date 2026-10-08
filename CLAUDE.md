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
| `connecting-the-dots.md` | `/connecting-the-dots/` | Three.js knowledge web. Unpublished since 2026-10-08 (`published: false`, notebook excluded in `_config.yml`), kept for a later redesign |
| `journey.md` | `/journey/` | Embeds the Folium journey map (not in nav; linked internally) |
| `404.md` | `/404.html` | Custom 404 page |

The only CV on this site is `files/XihanYao_CV.pdf`, the de-sensitized public CV,
linked from the navigation. It is built from `cv_public.tex` in the private repository
xyaoaf/XihanYao_CV; replace the PDF from there, keeping the file name so the link
stays stable. Never publish the full CV or the resume here: both are private and
sent directly to people. There is deliberately no /cv/ page.

## Publication Conventions

Publications must match the CV: the same titles, authors, years, volumes, pages
and DOIs as the publication list in the private CV repository (xyaoaf/XihanYao_CV,
`cv.tex`). Check a new entry against the journal's record (Crossref) before adding
it. For an article first published online and later placed in an issue, use the
issue's year once volume and pages are cited.

`markdown_generator/publications.tsv` is the source of truth. Edit it and run
`python publications.py` rather than editing `_publications/` by hand. Columns:

- `citation`: the APA reference from the CV, with `**Yao, X.**` in bold and the
  journal name and volume in `*italics*`. The templates add the DOI from `paper_url`.
- `pubtype`: `journal` or `proceedings`. The Publications page lists the two
  separately, as the CV does.
- `highlighted`: `true` puts the paper under Highlighted Research on the home page.
  Keep three, the strongest: currently the 2026 Annals article, the 2025
  microclimate article and the 2024 light-pollution article. The 2022 coastal
  water-quality article and the 2023 IGARSS paper are on the Publications page only.
- `paper_number`: permanent; 3 is unused. The next new publication is 7.

Generated file names are `YYYY-MM-DD-paper-N-short-title.md`.

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
1. Add a row to `markdown_generator/publications.tsv` with the CV's wording (see Publication Conventions)
2. Run `cd markdown_generator && python publications.py`

### Adding a talk
1. Add a row to `markdown_generator/talks.tsv`
2. Run `cd markdown_generator && python talks.py`
3. Or manually create `_talks/YYYY-MM-DD-talk-short-title.md`

### Updating the journey map
1. Edit location data in `files/journey_locations.py`
2. Run `python files/journey_map_folium.py` — this overwrites `files/journey_map.html`
3. Commit both the updated `.py` and `.html` files

### Adding a teaching entry
Create `_teaching/YYYY-MM-DD-course-name.md` — it will auto-appear on the Teaching page.

### Updating navigation
Edit `_data/navigation.yml`. Each entry needs `title:` and `url:`.

## Styling

The site's own look is set in two small files on top of the theme; change it
there rather than in the theme partials:

- `_sass/_tokens.scss`: every colour, font and size (text colours, the dark blue
  accent shared with the CV, the system font stack, five type sizes, two line
  heights, the reading width). It is imported right after `_variables.scss` and
  also sets the theme's own colour and font variables.
- `_sass/_custom.scss`: typography and spacing rules that the theme variables do
  not reach, imported last in `assets/css/main.scss`.

Fonts are the system stack, so there are no web fonts to load or update.

SASS source is in `_sass/`. Compiled CSS lives in `assets/css/`. JavaScript is in `assets/js/`. To minify JS:

```bash
npm run build:js    # Minify assets/js/
npm run watch:js    # Watch for changes
```
