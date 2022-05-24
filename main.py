import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import admin, auth, result, student

Base.metadata.create_all(bind=engine)


app = FastAPI(title="School-Management-System")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.admin_router)
app.include_router(auth.auth_router)
app.include_router(result.result_router)
app.include_router(student.std_router)


@app.get("/")
def root():
    return {"message": "Welcome to my School Management API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

