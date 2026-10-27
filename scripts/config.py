"""
Stores configuration variables for the build script.
"""

from pathlib import Path

# Since build.py is in scripts/, resolve paths relative to the repo root
REPO_ROOT = Path(__file__).resolve().parent.parent

SRC_DIR = REPO_ROOT / "src_code"
SRC_PREFIX = 6  # How many characters of string value should be removed from start?

TEMPLATE_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "dist"

BASE_TEMPLATE = "base.html"
STATIC_DIRS = ["css", "js", "resources"]  # copied into dist/ as-is

PAGE = "pages"
NAV_TARGETS = {
    "creative": Path(f"{PAGE}/creative/creative-index.html"),
    "technical": Path(f"{PAGE}/technical/technical-index.html"),
    "professional": Path(f"{PAGE}/professional/professional-index.html"),
    "personal": Path(f"{PAGE}/personal/personal-index.html"),
}
