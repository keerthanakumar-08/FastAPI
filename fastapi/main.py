import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app=api", host="localhost", port=8000, reload=True)
