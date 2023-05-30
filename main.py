from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn

app = FastAPI()
app.mount("/", StaticFiles(directory="content", html=True), name="static")

# @app.get("/")
# async def root_url():
#    return HTMLResponse(content=open("index.html", "r", encoding="utf-8").read(), status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
