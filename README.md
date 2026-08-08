# Personal Website — README

A small static-site build repository that converts minimal per-page source files in src_code/ into full pages using Jinja2 templates and outputs a ready-to-serve site into dist/.

## Requirements

- Python 3.13+
- pip
- uv (astral-sh package manager) — optional but used in CI
- Dependencies are declared in pyproject.toml / uv.lock

## Project layout

- src_code/ — source snippets (each file must include a `<title>`, a `<link rel="stylesheet"...>` and a `<main>` block)
- templates/ — Jinja2 templates (base.html, blog_design.html)
- css/, js/, resources/ — static assets copied to dist/
- scripts/build.py — build script that renders templates into dist/
- dist/ — generated site (output)

## Quickstart (Windows)

1. Create & activate virtualenv:
   - PowerShell:
     - python -m venv .venv
     - .venv\Scripts\Activate.ps1
   - CMD:
     - python -m venv .venv
     - .venv\Scripts\activate
2. Install tooling:
   - pip install --upgrade pip
   - pip install uv jinja2 beautifulsoup4
3. Sync (if using uv):
   - uv sync
4. Run build:
   - uv run python scripts\build.py
   - or: python scripts\build.py
5. Preview locally:
   - cd dist
   - python -m http.server 8000
   - open http://localhost:8000

## How source files are transformed

- build.py extracts:
  - page_title from `<title>`
  - style_sheet from the first `<link>` tag
  - main_body from `<main>`
- Output file names drop the numeric prefix set by SRC_PREFIX (see scripts/build.py).

## Adding / editing pages

- Add a file to src_code/ following the existing pattern (`<title>`, `<link>`, `<main>`).
- Update templates/ or css/ as needed.
- Re-run the build script using `uv run python scripts\build.py`.

## Deployment

- A GitHub Actions workflow (.github/workflows/deploy.yml) builds and deploys to GitHub Pages when code is pushed to the `release` branch. The workflow uses `uv sync` and runs the same build script, then uploads dist/ to Pages.

## Notes / troubleshooting

- build.py raises an error if a source file is missing `<title>`, `<link>`, or `<main>`.
- Adjust SRC_PREFIX in scripts/build.py if your filename prefix length changes.
- If using uv in CI, keep uv.lock in repo to pin dependencies.
