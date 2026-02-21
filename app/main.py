from fastapi import FastAPI

app = FastAPI(title="SAIS - Smart Export Intelligence System")

@app.get("/")
def root():
    return {"message": "SAIS is running"}
