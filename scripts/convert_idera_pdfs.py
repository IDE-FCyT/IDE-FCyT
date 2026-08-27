#!/usr/bin/env python3
"""Render the original IDERA poster PDFs as PNG images."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("Falta PyMuPDF. Instalelo con: python -m pip install PyMuPDF")


PROJECT_ROOT = Path(__file__).resolve().parents[1]
POSTER_DIRECTORIES = (
    PROJECT_ROOT / "Idera 2025",
    PROJECT_ROOT / "Idera 2026",
)


def output_path(pdf_path: Path, page_count: int, page_number: int) -> Path:
    if page_count == 1:
        return pdf_path.with_suffix(".png")
    return pdf_path.with_name(f"{pdf_path.stem}-page-{page_number}.png")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convierte los PDF de posters IDERA 2025 y 2026 a PNG."
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=200,
        help="Resolucion de salida en DPI (predeterminado: 200).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Regenera los PNG que ya existen.",
    )
    args = parser.parse_args()

    if args.dpi <= 0:
        parser.error("--dpi debe ser mayor que cero.")

    pdf_paths = sorted(
        pdf_path
        for directory in POSTER_DIRECTORIES
        if directory.is_dir()
        for pdf_path in directory.glob("*.pdf")
    )
    if not pdf_paths:
        sys.exit("No se encontraron PDF en Idera 2025 ni Idera 2026.")

    converted = 0
    skipped = 0
    for pdf_path in pdf_paths:
        with pymupdf.open(pdf_path) as document:
            for page_number, page in enumerate(document, start=1):
                png_path = output_path(pdf_path, len(document), page_number)
                if png_path.exists() and not args.overwrite:
                    print(f"Omitido: {png_path.relative_to(PROJECT_ROOT)}")
                    skipped += 1
                    continue

                pixmap = page.get_pixmap(dpi=args.dpi, alpha=False)
                pixmap.save(png_path)
                print(f"Generado: {png_path.relative_to(PROJECT_ROOT)}")
                converted += 1

    print(f"Finalizado: {converted} PNG generados, {skipped} omitidos.")


if __name__ == "__main__":
    main()
