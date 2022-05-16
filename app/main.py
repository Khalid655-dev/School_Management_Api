from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from . database import engine
from . routers import student, admin, auth, result
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student.router)
app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(result.router)




@app.get("/")
def root():
    return {"message": "Welcome to my Api"}









    

