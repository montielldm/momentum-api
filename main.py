from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Call routers
from app.auth.router import auth
from app.groups.router import groups

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

# include routers
app.include_router(auth)
app.include_router(groups)