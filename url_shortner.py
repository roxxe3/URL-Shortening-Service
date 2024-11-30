from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import hashlib
from file_storage import Short_url
import json
import urllib.parse
from pydantic import BaseModel


class URLRequest(BaseModel):
    url: str

app = FastAPI()

def get_short_url(shortcode):
    with open("data.json", "r") as file:
        dict = json.load(file)
    for url in dict:
        if url['id'] == shortcode:
            return url["url"]
    return None
    

def generate_id(url):
    input_string = url
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    short_id = md5_hash[:8]
    return short_id


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/shorten")
async def shorten(request: URLRequest):
    decoded_url = urllib.parse.unquote(request.url)
    short_id = generate_id(decoded_url)
    short_url = Short_url(short_id, decoded_url)
    url_dict = short_url.create_dict()
    short_url.save_file(url_dict)
    return {"message": short_id}

@app.get("/shorten/{shortCode}")
async def get_url(shortCode: str):
    url = get_short_url(shortCode)
    return RedirectResponse(url=url, status_code=302)

