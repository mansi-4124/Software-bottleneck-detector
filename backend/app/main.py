from fastapi import FastAPI

app = FastAPI(
    title="Software Bottleneck Detector",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "message": "Software Bottleneck Detector API"
    }