"""
Stellaris Wiki Scraper — CLI entry point.

Provides the ``stellariswiki`` command with three subcommands:

    stellariswiki fetch      Fetch wiki pages and convert to Markdown
    stellariswiki analyze    Analyze wiki coverage and generate dashboard
    stellariswiki serve      Start MCP server for Claude Desktop
"""

import argparse
import sys
import textwrap

from src import __version__


# -- Epilog text (shown after --help) ----------------------------------------

_EXAMPLES = textwrap.dedent("""\
    examples:
      Fetch all pages (4 parallel workers):
        %(prog)s fetch

      Test a single page (prints first 2000 chars):
        %(prog)s fetch --page "Technology" --test

      Gentle sequential fetching:
        %(prog)s fetch --workers 1 --delay 1.0

      Fetch to a custom directory:
        %(prog)s fetch --output my_data

      Generate interactive HTML dashboard:
        %(prog)s analyze

      Generate dashboard and open in browser:
        %(prog)s analyze --open

      Generate Markdown report instead:
        %(prog)s analyze --format md

      Open existing dashboard in browser:
        %(prog)s dashboard

      Start MCP server for Claude Desktop:
        %(prog)s serve
""")

_FETCH_EXAMPLES = textwrap.dedent("""\
    examples:
      Fetch all 101 configured pages (parallel):
        %(prog)s

      Test a single page (shows first 2000 chars):
        %(prog)s --page "Machine_traits" --test

      Fetch a composite page (main + all sub-pages):
        %(prog)s --page "Astral rift"

      Sequential fetching (1 worker, gentler on wiki):
        %(prog)s --workers 1 --delay 1.0

      Custom output directory:
        %(prog)s --output my_wiki_data
""")

_ANALYZE_EXAMPLES = textwrap.dedent("""\
    examples:
      Generate interactive HTML dashboard:
        %(prog)s

      Generate and open in browser:
        %(prog)s --open

      Generate Markdown report:
        %(prog)s --format md

      Custom output path:
        %(prog)s --output reports/analysis.html

      Skip all_pages.md generation:
        %(prog)s --no-all-pages
""")

_DASHBOARD_EXAMPLES = textwrap.dedent("""\
    examples:
      Open the dashboard in the default browser:
        %(prog)s
""")

_SERVE_EXAMPLES = textwrap.dedent("""\
    examples:
      Start MCP server (stdio, default):
        %(prog)s

      Start with SSE transport:
        %(prog)s --transport sse
""")


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="stellariswiki",
        description="Stellaris Wiki Scraper: fetch, analyze, and serve Stellaris wiki data.",
        epilog=_EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    sub = parser.add_subparsers(dest="command", help="command to run")

    # -- fetch ----------------------------------------------------------------
    fetch_p = sub.add_parser(
        "fetch",
        help="Fetch wiki pages and convert to Markdown",
        description="Fetch Stellaris Wiki pages via MediaWiki API and convert to clean Markdown.",
        epilog=_FETCH_EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    fetch_p.add_argument(
        "--page", type=str, metavar="TITLE",
        help="Process a single page by title (e.g. \"Technology\", \"Astral rift\")",
    )
    fetch_p.add_argument(
        "--test", action="store_true",
        help="Test mode: print first 2000 chars of output (use with --page)",
    )
    fetch_p.add_argument(
        "--output", type=str, metavar="DIR", default=None,
        help="Output directory (default: output/)",
    )
    fetch_p.add_argument(
        "--delay", type=float, metavar="SEC", default=None,
        help="Delay between API requests in seconds (default: 0.5, sequential mode)",
    )
    fetch_p.add_argument(
        "--workers", type=int, metavar="N", default=None,
        help="Number of parallel workers (default: 4)",
    )

    # -- analyze --------------------------------------------------------------
    analyze_p = sub.add_parser(
        "analyze",
        help="Analyze wiki coverage and generate interactive report",
        description=(
            "Fetch the full wiki page inventory, classify pages, and generate "
            "an interactive HTML dashboard or Markdown report."
        ),
        epilog=_ANALYZE_EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    analyze_p.add_argument(
        "--format", choices=["html", "md"], default="html",
        help="Output format (default: html)",
    )
    analyze_p.add_argument(
        "--workers", type=int, metavar="N", default=None,
        help="Number of parallel workers for API calls (default: 4)",
    )
    analyze_p.add_argument(
        "--output", type=str, metavar="PATH", default=None,
        help="Output file path (default: output/wiki_analysis.{html|md})",
    )
    analyze_p.add_argument(
        "--no-all-pages", action="store_true",
        help="Skip generating all_pages.md",
    )
    analyze_p.add_argument(
        "--open", action="store_true",
        help="Open the dashboard in the default browser after generation",
    )

    # -- dashboard ------------------------------------------------------------
    sub.add_parser(
        "dashboard",
        help="Open the analysis dashboard in the default browser",
        description="Open the previously generated wiki analysis dashboard in the default browser.",
        epilog=_DASHBOARD_EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # -- serve ----------------------------------------------------------------
    serve_p = sub.add_parser(
        "serve",
        help="Start MCP server for Claude Desktop integration",
        description=(
            "Launch a Model Context Protocol (MCP) server that exposes "
            "wiki data to Claude Desktop (list_pages, get_page, search_wiki)."
        ),
        epilog=_SERVE_EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    serve_p.add_argument(
        "--transport", default="stdio", choices=["stdio", "sse"],
        help="MCP transport protocol (default: stdio)",
    )

    return parser


def main(argv: list[str] | None = None):
    """CLI entry point — called by ``stellariswiki`` console script and ``python stellariswiki.py``."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "fetch":
        from src.fetcher import main as fetch_main
        fetch_main(args)

    elif args.command == "analyze":
        from src.analyzer import main as analyze_main
        output_path = analyze_main(args)
        if getattr(args, "open", False) and output_path and output_path.exists():
            import webbrowser
            webbrowser.open(output_path.as_uri())

    elif args.command == "dashboard":
        _open_dashboard()

    elif args.command == "serve":
        from src.mcp_server import mcp
        mcp.run(transport=args.transport)


def _open_dashboard():
    """Open the analysis dashboard in the default browser."""
    import webbrowser
    from src import OUTPUT_DIR

    dashboard = OUTPUT_DIR / "wiki_analysis.html"
    if not dashboard.exists():
        print(f"Dashboard not found: {dashboard}")
        print("Run 'stellariswiki analyze' first to generate it.")
        sys.exit(1)

    print(f"Opening {dashboard}")
    webbrowser.open(dashboard.as_uri())
