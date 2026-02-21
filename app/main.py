from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

# إنشاء التطبيق
app = FastAPI(title="SAIS - Smart Export Intelligence System")

# إنشاء الجداول تلقائيًا عند تشغيل التطبيق
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "SAIS Core Running with Database"}
