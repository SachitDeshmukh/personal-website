# IMPORTING NECESSARY LIBRARIES

import shutil


# CONFIGURTION
from config import *
from extract import *
from render_content import render_content


# COPYING STATIC
def copy_static():
    """
    Copies static directories shared across all pages.
        - css: for all style sheets
        - js: for the scripts
        - resources: for all resources across pages
    """
    for dir in STATIC_DIRS:
        dir_path = REPO_ROOT / dir
        if dir_path.exists():
            shutil.copytree(dir_path, OUTPUT_DIR / dir, dirs_exist_ok=True)


# BUILDING PAGES
def build() -> None:
    # Create dist folder with statis content
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_static()

    # Extract all html source code
    src_files = sorted(SRC_DIR.glob("*.html"))
    if not src_files:
        print(f"No source files found in {SRC_DIR.resolve()}")
        return

    # Render pages
    for src_path in src_files:
        render_content(src_path)


if __name__ == "__main__":
    build()
