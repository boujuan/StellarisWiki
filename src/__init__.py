"""Stellaris Wiki Scraper package."""

from pathlib import Path

# Single source of truth for all project paths.
# Every module imports these instead of computing its own paths.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
CONFIG_PATH = CONFIG_DIR / "config.yaml"
OUTPUT_DIR = PROJECT_ROOT / "output"
