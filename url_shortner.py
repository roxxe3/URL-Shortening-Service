from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
import hashlib
from file_storage import Short_url
import json
import urllib.parse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


class URLRequest(BaseModel):
    url: str

app = FastAPI()
templates = Jinja2Templates(directory="templates")

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


@app.get("/", response_class=HTMLResponse)
async def render_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/shorten")
async def shorten(url: str = Form(...)):
    short_id = generate_id(url)
    short_url = Short_url(short_id, url)
    url_dict = short_url.create_dict()
    short_url.save_file(url_dict)
    return {"message": short_id}

@app.get("/{shortCode}")
async def get_url(shortCode: str):
    url = get_short_url(shortCode)
    return RedirectResponse(url=url, status_code=302)

