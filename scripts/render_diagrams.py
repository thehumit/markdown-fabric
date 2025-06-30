#!/usr/bin/env python3
"""Render PlantUML and Mermaid diagrams.

This script recursively scans the given input directory for ``.puml`` and
``.mmd`` files and renders them as PNG images. PlantUML diagrams are
processed with the ``plantuml`` command, while Mermaid diagrams are
rendered using ``mmdc``.

Usage:
    python render_diagrams.py [input_dir] [output_dir]

If paths are not provided, ``docs/diagrams`` is used as the input
and ``docs/generated`` as the output directory.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def run_command(cmd: list[str]) -> None:
    """Run a command and raise ``RuntimeError`` if it fails."""
    try:
        subprocess.run(cmd, check=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}") from exc


def render_plantuml(files: list[Path], output_dir: Path) -> None:
    for file in files:
        run_command(
            [
                "plantuml",
                "-tpng",
                str(file),
                "-o",
                str(output_dir.resolve()),
            ]
        )


def render_mermaid(files: list[Path], output_dir: Path) -> None:
    config = Path(__file__).with_name("puppeteer.json")
    for file in files:
        output_file = output_dir / f"{file.stem}.png"
        run_command(
            [
                "mmdc",
                "-i",
                str(file),
                "-o",
                str(output_file),
                "--puppeteerConfigFile",
                str(config),
            ]
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Render diagrams")
    parser.add_argument(
        "input_dir",
        nargs="?",
        default="docs/diagrams",
        help="Directory with source diagrams",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="docs/generated",
        help="Where to place generated PNG files",
    )

    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    plantuml_files = list(input_dir.rglob("*.puml"))
    mermaid_files = list(input_dir.rglob("*.mmd"))

    if plantuml_files:
        render_plantuml(plantuml_files, output_dir)
    if mermaid_files:
        render_mermaid(mermaid_files, output_dir)

    print(f"Diagrams generated in {output_dir}")


if __name__ == "__main__":
    main()
