from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.programs.router import programs
from app.instructors.router import instructors
from app.apprentices.router import apprentices
from app.groups.router import groups
from app.auth.router import auth

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(programs)
app.include_router(instructors)
app.include_router(apprentices)
app.include_router(groups)