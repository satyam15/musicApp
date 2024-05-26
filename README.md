# musicApp

This project is a Flask-based application that processes and normalizes a dataset of song playlists from a JSON file, and provides a RESTful API to interact with the normalized data.

## Features

- Load and normalize song data from a JSON file.
- Provide API endpoints to:
  - Fetch all songs.
  - Fetch song details by title.
  - Rate a song.

## Tech Stack

- Python
- Flask
- Flask-RESTful
- Pandas

## Usage

1. **Place your JSON file in the project directory.**

2. **Modify the `dataNorm.py` file to point to your JSON file:**

3. **Run the Flask application:**

    ```sh
    python app.py
    ```

4. **Access the API endpoints:**

    - Fetch all songs: `GET /songs`
    - Fetch song by title: `GET /songs/<title>`
    - Rate a song: `POST /songs/<title>/rate`

### Example Requests

- **Fetch all songs:**

    ```sh
    curl http://127.0.0.1:5000/songs
    ```

- **Fetch song by title:**

    ```sh
    curl http://127.0.0.1:5000/songs/3AM
    ```

- **Rate a song:**

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"rating": 5}' http://127.0.0.1:5000/songs/3AM/rate
    ```

## Running Tests

1. **Run the unit tests:**

    ```sh
    python test.py
    ```

## Project Structure


