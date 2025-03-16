from fastapi import FastAPI
from app.routers.user_router import router as user_router

app = FastAPI(title="Image Editor API")


app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
