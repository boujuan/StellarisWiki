"""
Shared configuration loader for the Stellaris Wiki scraper.

Loads config.yaml from the project root and provides typed access
to all configuration values. Used by fetch_and_parse.py,
analyze_wiki_pages.py, and stellaris_mcp_server.py.
"""

import yaml
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
_CONFIG_PATH = PROJECT_ROOT / "config.yaml"


@dataclass
class WikiConfig:
    api_url: str


@dataclass
class DefaultsConfig:
    output_dir: str
    workers: int
    delay: float
    request_delay: float
    max_retries: int
    generate_all_pages: bool


@dataclass
class CompositePageConfig:
    extractor: str
    extra_subpages: list[str]


@dataclass
class ClassificationConfig:
    mod_prefixes: list[str]
    mod_categories: set[str]
    dlc_titles: set[str]
    wiki_maintenance_categories: set[str]
    wiki_maintenance_prefixes: list[str]
    disambiguation_categories: set[str]


@dataclass
class Config:
    game_version: str
    wiki: WikiConfig
    defaults: DefaultsConfig
    pages_to_fetch: list[str]
    composite_pages: dict[str, CompositePageConfig]
    classification: ClassificationConfig

    @property
    def combined_filename(self) -> str:
        return f"stellaris_{self.game_version}_combined.md"

    @property
    def output_path(self) -> Path:
        return PROJECT_ROOT / self.defaults.output_dir


def load_config(config_path: Path | None = None) -> Config:
    """Load configuration from YAML file.

    Args:
        config_path: Optional override path. Defaults to config.yaml
                     in the project root.

    Returns:
        Populated Config dataclass instance.
    """
    path = config_path or _CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {path}\n"
            f"Expected config.yaml in the project root."
        )

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    # Parse composite_pages: values are dicts with extractor + extra_subpages
    composite_pages = {}
    for title, val in raw.get("composite_pages", {}).items():
        composite_pages[title] = CompositePageConfig(
            extractor=val["extractor"],
            extra_subpages=val.get("extra_subpages") or [],
        )

    cls_raw = raw["classification"]

    return Config(
        game_version=raw["game_version"],
        wiki=WikiConfig(
            api_url=raw["wiki"]["api_url"],
        ),
        defaults=DefaultsConfig(
            output_dir=raw["defaults"]["output_dir"],
            workers=raw["defaults"]["workers"],
            delay=raw["defaults"]["delay"],
            request_delay=raw["defaults"]["request_delay"],
            max_retries=raw["defaults"]["max_retries"],
            generate_all_pages=raw["defaults"].get("generate_all_pages", True),
        ),
        pages_to_fetch=raw["pages_to_fetch"],
        composite_pages=composite_pages,
        classification=ClassificationConfig(
            mod_prefixes=cls_raw["mod_prefixes"],
            mod_categories=set(cls_raw.get("mod_categories") or []),
            dlc_titles=set(cls_raw["dlc_titles"]),
            wiki_maintenance_categories=set(
                cls_raw["wiki_maintenance_categories"]
            ),
            wiki_maintenance_prefixes=cls_raw.get("wiki_maintenance_prefixes") or [],
            disambiguation_categories=set(
                cls_raw.get("disambiguation_categories") or []
            ),
        ),
    )


# Module-level singleton: loaded once, imported everywhere.
cfg = load_config()
