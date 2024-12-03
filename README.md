# URL-Shortening-Service

A simple RESTful API that allows users to shorten long URLs.

project_url = `https://roadmap.sh/projects/url-shortening-service`

## Features

- Shorten long URLs
- Retrieve original URLs using shortcodes
- Update existing short URLs
- Delete short URLs
- Track access count for each short URL

## Project Structure

URL-Shortening-Service/ ├── pycache/ ├── data.json ├── db_storage.py ├── file_storage.py ├── README.md ├── templates/ │ └── form.html └── url_shortner.py


## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/URL-Shortening-Service.git
    cd URL-Shortening-Service
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Start the MongoDB server locally:

    ```sh
    mongod --dbpath /path/to/your/db
    ```

4. Run the FastAPI application:

    ```sh
    uvicorn url_shortner:app --reload
    ```

## API Endpoints

### Shorten URL

- **Endpoint**: `/shorten`
- **Method**: `POST`
- **Parameters**: `url` (form data)
- **Response**: JSON with the shortened URL ID

### Retrieve URL

- **Endpoint**: `/shorten/{shortCode}`
- **Method**: `GET`
- **Response**: Redirects to the original URL

### Update URL

- **Endpoint**: `/shorten/{shortCode}`
- **Method**: `PUT`
- **Parameters**: `url` (form data)
- **Response**: JSON with a success message and updated URL data

### Get URL Stats

- **Endpoint**: `/shorten/{shortCode}/stats`
- **Method**: `GET`
- **Response**: JSON with URL statistics

### Delete URL

- **Endpoint**: `/shorten/{shortCode}`
- **Method**: `DELETE`
- **Response**: JSON with a success message

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/` to access the URL submission form.
2. Submit a URL to get a shortened URL ID.
3. Use the API endpoints to manage and retrieve your shortened URLs.
