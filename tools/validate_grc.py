#!/opt/local/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9
"""Validate GRC files with the installed GNU Radio Companion core."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from gnuradio import gr
from gnuradio.grc.core.platform import Platform


def validate_one(platform: Platform, path: Path) -> tuple[bool, list[str]]:
    flow_graph = platform.make_flow_graph()
    flow_graph.grc_file_path = str(path)
    flow_graph.import_data(platform.parse_flow_graph(str(path)))
    flow_graph.rewrite()
    flow_graph.validate()
    return flow_graph.is_valid(), flow_graph.get_error_messages()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)

    platform = Platform(
        name="GNU Radio Companion Validator",
        prefs=gr.prefs(),
        version=gr.version(),
        version_parts=(gr.major_version(), gr.api_version(), gr.minor_version()),
    )
    platform.build_library()

    lines = ["# GNU Radio Validation Report", "", f"GNU Radio: {gr.version()}", ""]
    failed = False
    for path in args.paths:
        ok, errors = validate_one(platform, path)
        lines.append(f"## {path}")
        lines.append("")
        lines.append(f"- Result: {'OK' if ok else 'FAILED'}")
        if errors:
            lines.append("- Errors:")
            lines.extend(f"  - {error}" for error in errors)
        lines.append("")
        failed = failed or not ok

    text = "\n".join(lines)
    if args.report:
        args.report.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
