# IMPORTING NECESSARY LIBRARIES

import os

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from config import *
from extract import *


# RENDERING CONTENT
def render_content(src_path: Path):
    file_name = src_path.name[SRC_PREFIX:]
    path_data = extract_page_meta(src_path)
    diary = path_data["diary"]
    year = path_data["year"]

    if diary is not None:
        temp_path = OUTPUT_DIR / PAGE / str(diary)
        if year is not None:
            temp_path /= str(year)
        temp_path.mkdir(parents=True, exist_ok=True)
        output_path = temp_path / file_name
    else:
        output_path = OUTPUT_DIR / file_name

    rel_path = output_path.parent.relative_to(OUTPUT_DIR)
    nav_links = {
        category: Path(os.path.relpath(target, start=rel_path)).as_posix()
        for category, target in NAV_TARGETS.items()
    }

    # Initiate JinJa2 Environment to parse html data into template
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=False,  # main_body contains real HTML; we don't want it escaped
    )
    template = env.get_template(BASE_TEMPLATE)

    # Extract content to (1) update templates, and (2) generate dynamic paths
    page_data = extract_page_content(src_path)
    rendered_html = template.render(**page_data, nav_links=nav_links)

    output_path.write_text(rendered_html, encoding="utf-8")
