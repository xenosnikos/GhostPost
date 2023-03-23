from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from article_generator import generate_article

app = FastAPI()

origins = [
    "https://goldfish-app-y5srr.ondigitalocean.app/",
    "http://localhost:3000",
    "http://localhost:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/api/get-article")
def get_article(address: str = Body(embed=True), title: str = Body(embed=True), description: str = Body(embed=True)):
    return generate_article(address, title, description)
