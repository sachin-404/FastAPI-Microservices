from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki, wiki, phrase, parts_of_speech_tags


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to Wikipedia API. Call /search or /summary"}


@app.get("/search/{name}")
async def search(name: str):
    """Page to search in Wikipedia"""

    result = search_wiki(name)
    return {"result": result}


@app.get("/summary/{name}")
async def wiki_summary(name: str):
    """Get summary from Wikipedia"""

    result = wiki(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def noun_phrases(name: str):
    """Retrieve Wikipedia page and return phrases"""

    result = phrase(name)
    return {"result": result}


@app.get("/pos/{name}")
async def part_of_speech(name: str):
    """Retrieve Wikipedia page and return Part-of-speech tags"""

    result = parts_of_speech_tags(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
