from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
import hashlib
from db_storage import Short_url
import json
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import db_storage
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",  # You can add more origins here
    "http://127.0.0.1",
]



class URLRequest(BaseModel):
    url: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    short_url = db_storage.Short_url(short_id, url)
    url_dict = short_url.create_dict()
    short_url.save_file(url_dict)
    short_url.save_to_db(url_dict)
    return {"message": short_id}

@app.get("/shorten/{shortCode}")
async def get_url(shortCode: str):
    data=Short_url.find_url(shortCode)
    return RedirectResponse(url=data["url"], status_code=302)

@app.put("/shorten/{shortCode}")
async def update_url(shortCode, url):
    db_storage.Short_url.update_url(shortCode, url)
    data=Short_url.find_url(shortCode)
    return {"message": "URL updated successfully", "result": data}

@app.get("/shorten/{shortCode}/stats")
async def get_stats(shortCode):
    data=Short_url.find_url(shortCode)
    return data

@app.delete("/shorten/{shortCode}")
async def delete_url(shortCode):
    Short_url.delete_url(shortCode)
    return {"message": "URL deleted successfully"}