from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def summarize_excel_file(file_path: Path) -> dict[str, Any]:
    workbook = pd.ExcelFile(file_path)
    sheets_summary: list[dict[str, Any]] = []

    for sheet_name in workbook.sheet_names:
        frame = workbook.parse(sheet_name)
        frame.columns = [str(col).strip() for col in frame.columns]
        sheets_summary.append(
            {
                "sheet": sheet_name,
                "rows": int(len(frame)),
                "columns": list(frame.columns),
            }
        )

    return {
        "file_name": file_path.name,
        "sheets": sheets_summary,
    }
