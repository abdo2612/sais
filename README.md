# sais
SAIS - Smart Export Intelligence System (MVP Core Platform)

## What is ready now?
The project now includes a working FastAPI backend with:
- default database fallback (`sqlite:///./sais.db`) so it runs immediately,
- an Excel ingestion endpoint to accept multiple files,
- automatic sheet/column/row summarization for each uploaded file.

هذه التعديلات تهدف إلى تحسين أداء منصة SAIS للتصدير، مع تجهيز خطوة أولى عملية لتحويل ملفات الإكسل إلى بيانات قابلة للتحليل داخل المنصة.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API
### `GET /`
Health response for core service.

### `POST /ingest/excel`
Upload one or more `.xlsx` / `.xls` files as `files` form-data.

Example response:
```json
{
  "message": "Excel files were uploaded and analyzed successfully.",
  "files_count": 2,
  "files": [
    {
      "file_name": "customers.xlsx",
      "sheets": [
        {
          "sheet": "Sheet1",
          "rows": 120,
          "columns": ["id", "name", "country"]
        }
      ]
    }
  ]
}
```
