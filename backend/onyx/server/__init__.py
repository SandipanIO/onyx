if __name__ == "__main__":
    import uvicorn
    import os

    uvicorn.run(
        "backend.onyx.server:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=False
    )
