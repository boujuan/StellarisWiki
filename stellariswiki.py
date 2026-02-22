#!/usr/bin/env python3
"""
Stellaris Wiki Scraper — unified CLI entry point.

Usage:
    python stellariswiki.py fetch               Fetch wiki pages → Markdown
    python stellariswiki.py fetch --page X --test   Test a single page
    python stellariswiki.py analyze             Analyze wiki + generate dashboard
    python stellariswiki.py analyze --format md Markdown report instead of HTML
    python stellariswiki.py serve               Start MCP server (stdio)
"""

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stellariswiki",
        description="Stellaris Wiki Scraper: fetch, analyze, and serve wiki data.",
    )
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # --- fetch ---
    fetch_p = sub.add_parser("fetch", help="Fetch wiki pages and convert to Markdown")
    fetch_p.add_argument("--page", type=str, help="Process a single page (for testing)")
    fetch_p.add_argument("--test", action="store_true", help="Test mode (with --page)")
    fetch_p.add_argument("--output", type=str, default=None, help="Output directory")
    fetch_p.add_argument("--delay", type=float, default=None,
                         help="Delay between requests (seconds)")
    fetch_p.add_argument("--workers", type=int, default=None,
                         help="Number of parallel workers")

    # --- analyze ---
    analyze_p = sub.add_parser("analyze", help="Analyze wiki coverage and generate report")
    analyze_p.add_argument("--format", choices=["html", "md"], default="html",
                           help="Output format (default: html)")
    analyze_p.add_argument("--workers", type=int, default=None,
                           help="Number of parallel workers")
    analyze_p.add_argument("--output", type=str, default=None, help="Output file path")
    analyze_p.add_argument("--no-all-pages", action="store_true",
                           help="Skip generating all_pages.md")

    # --- serve ---
    serve_p = sub.add_parser("serve", help="Start MCP server for Claude Desktop")
    serve_p.add_argument("--transport", default="stdio", choices=["stdio", "sse"],
                         help="MCP transport (default: stdio)")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "fetch":
        from src.fetcher import main as fetch_main
        fetch_main(args)

    elif args.command == "analyze":
        from src.analyzer import main as analyze_main
        analyze_main(args)

    elif args.command == "serve":
        from src.mcp_server import mcp
        mcp.run(transport=args.transport)


if __name__ == "__main__":
    main()
