# IMPORTING NECESSARY LIBRARIES

from pathlib import Path
from bs4 import BeautifulSoup

from config import *


def extract_page_content(src_path: Path) -> dict:
    """
    Parse a single source file and pull out:
      - page_title: plain text from <title>
      - style_sheet: all <link> elements as HTML
      - main_body: the inner HTML of <main>, as a raw string

    Raises ValueError if a required element is missing, so a malformed src file
    fails the build loudly instead of silently producing a broken page.
    """
    soup = BeautifulSoup(src_path.read_text(encoding="utf-8"), "html.parser")

    title_tag = soup.find("title")
    link_tags_stylesheet = soup.find_all("link")
    main_tag = soup.find("main")

    if title_tag is None or not link_tags_stylesheet or main_tag is None:
        raise ValueError(f"{src_path.name} is missing a <title>,<link> or <main> tag")

    page_title = title_tag.get_text(strip=True)
    style_sheet = "\n".join(link.decode().strip() for link in link_tags_stylesheet)
    main_body = main_tag.decode().strip()

    return {
        "page_title": page_title,
        "style_sheet": style_sheet,
        "main_body": main_body,
    }


def extract_page_meta(src_path: Path) -> dict:
    """
    Parse a single source fill and pull out:
        - class of main: to determine which diary does the page belong to
        - year: to determine the year of publication

    Raises ValueError if a required element is missing, so a malformed src file
    fails the build loudly instead of silently producing a broken page.
    """

    soup = BeautifulSoup(src_path.read_text(encoding="utf-8"), "html.parser")

    # Find the relevant tags and attributes
    meta_tag = soup.find("meta")
    main_tag = soup.find("main")

    if meta_tag is None or main_tag is None:
        raise ValueError(f"{src_path.name} is missing a <meta> or <main> tag")

    # Obtain relevant values
    main_category = main_tag.get("data-cat")
    meta_attrs = meta_tag.attrs
    meta_year = (
        meta_attrs["year"] if main_category != None and "year" in meta_attrs else None
    )

    return {
        "diary": main_category,
        "year": meta_year,
    }
