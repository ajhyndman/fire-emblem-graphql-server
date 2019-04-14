import uvicorn


def main():
    # START SERVER
    uvicorn.run(
        "src.app:app",
        host="localhost",
        port=8888,
        access_log=False,
        reload=True,
        reload_dirs=["src"],
    )
