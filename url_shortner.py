from fastapi import FastAPI
import hashlib
from file_storage import Short_url

app = FastAPI()


def generate_id(url):
    input_string = url
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    short_id = md5_hash[:8]  # First 8 characters
    return short_id


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/shorten/{url}")
async def shorten(url):
    short_id = generate_id(url)
    short_url = Short_url(short_id, url)
    url_dict = short_url.create_dict(short_id)
    short_url.save_file(url_dict)
    return 

app.get("/shorten/shortCode")
async def get_url(shortCode):
    pass
