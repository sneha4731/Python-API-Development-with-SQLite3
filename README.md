#Readme.md
# RESTful API with Flask and SQLite3

## Setup Instructions

1. **Create a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate # On Windows use `env\Scripts\activate`
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    python app.py
    ```

4. **Use the API Endpoints:**

    - **Create a Book:**
      - `POST /books`
    - **Get a Book by ID:**
      - `GET /books/<id>`
    - **Get Books with Filters:**
      - `GET /books`
    - **Update a Book:**
      - `PUT /books/<id>`
    - **Delete a Book:**
      - `DELETE /books/<id>`

5. **Test the Application:**
   - You can use tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) to test the API.