"""
Reads simple per-page source files from "src_code/", each containing just
a <title> tag and a <main> tag. Extracts both, then renders them into the
shared "templates/base.html" template. Output is written to "dist/".

Usage:
    python build.py
"""

# IMPORTING NECESSARY LIBRARIES

from pathlib import Path

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader


# CONFIGURTION

# Since build.py is in scripts/, resolve paths relative to the repo root
REPO_ROOT = Path(__file__).resolve().parent.parent

SRC_DIR = REPO_ROOT / "src_code"
SRC_PREFIX = 6  # How many characters of string value should be removed from start?

TEMPLATE_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "dist"

BASE_TEMPLATE = "base.html"
STATIC_DIRS = ["css", "js", "resources"]  # copied into dist/ as-is


# EXTRACTION


def extract_page_data(src_path: Path) -> dict:
    """
    Parse a single source file and pull out:
      - page_title: plain text from <title>
      - main_body: the inner HTML of <main>, as a raw string

    Raises ValueError if either tag is missing, so a malformed src file
    fails the build loudly instead of silently producing a broken page.
    """
    soup = BeautifulSoup(src_path.read_text(encoding="utf-8"), "html.parser")

    title_tag = soup.find("title")
    link_tag_stylesheet = soup.find("link")
    main_tag = soup.find("main")

    if title_tag is None or link_tag_stylesheet is None or main_tag is None:
        raise ValueError(f"{src_path.name} is missing a <title>,<link> or <main> tag")

    page_title = title_tag.get_text(strip=True)
    style_sheet = link_tag_stylesheet.decode().strip()
    main_body = main_tag.decode().strip()

    return {
        "page_title": page_title,
        "style_sheet": style_sheet,
        "main_body": main_body,
    }


# RENDERING


def build() -> None:
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=False,  # main_body contains real HTML; we don't want it escaped
    )
    template = env.get_template(BASE_TEMPLATE)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    src_files = sorted(SRC_DIR.glob("*.html"))
    if not src_files:
        print(f"No source files found in {SRC_DIR.resolve()}")
        return

    for src_path in src_files:
        page_data = extract_page_data(src_path)
        rendered_html = template.render(**page_data)

        output_path = OUTPUT_DIR / src_path.name[SRC_PREFIX:]

        output_path.write_text(rendered_html, encoding="utf-8")


if __name__ == "__main__":
    build()
