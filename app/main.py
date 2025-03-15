from fastapi import FastAPI
# from app.routers.image_router import router as image_router

app = FastAPI(title="Image Editor API")


# app.include_router(image_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

# uvicorn app.main:app --reload
