from __future__ import annotations

from pathlib import Path
import shutil

from fastapi import FastAPI, File, HTTPException, UploadFile

from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.services.excel_ingestion import summarize_excel_file

app = FastAPI(title="SAIS - Smart Export Intelligence System")

Base.metadata.create_all(bind=engine)

storage_dir = Path(settings.STORAGE_DIR)
uploads_dir = storage_dir / "uploads"
uploads_dir.mkdir(parents=True, exist_ok=True)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "SAIS Core Running with Database",
        "project": settings.PROJECT_NAME,
    }


@app.post("/ingest/excel")
async def ingest_excel(files: list[UploadFile] = File(...)) -> dict[str, object]:
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    processed: list[dict[str, object]] = []

    for file in files:
        suffix = Path(file.filename or "").suffix.lower()
        if suffix not in {".xlsx", ".xls"}:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type for '{file.filename}'. Please upload Excel files.",
            )

        destination = uploads_dir / (file.filename or "uploaded.xlsx")
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        processed.append(summarize_excel_file(destination))

    return {
        "message": "Excel files were uploaded and analyzed successfully.",
        "files_count": len(processed),
        "files": processed,
    }
