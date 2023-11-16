# Form Template Matcher

This Flask application processes submitted forms, matches them with existing form templates, and returns the template name if a match is found. If no matching template is found, it returns a set of field names along with their inferred types based on validation rules.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)


## Features

- Processes submitted forms and matches them with existing templates.
- Returns the template name if a match is found.
- If no match is found, returns a set of field names with inferred types based on validation rules (date, phone, email).

## Installation

#### Start the project without Docker:
1. The first thing to do is to clone the repository:
    ```bash
    git clone https://github.com/marik177/template_matcher.git

    ```
2. Create a virtual environment to install dependencies in and activate it:
    ```bash
    python3 -m venv venv
   
    source venv/bin/activate
    ```   
3. Then install the dependencies:
    ```bash
   (env)$ pip install -r requirements.txt
    ```
    &emsp; Note the (env) in front of the prompt.

    &emsp; This indicates that this terminal session operates in a virtual environment set.
## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. In new terminal run file test_requests.py to test application.
   ```bash
   python test_requests.py
   ```
3. In db.json stored some testing forms.

4. It is possible to load new form templates using load_db.py

## Endpoints
1. GET /
* Description: Retrieve all stored form data.
* Method: GET
* Response: JSON array containing all form data.
2. POST /get-form
* Description: Process a submitted form and return the matching template name or inferred field types.

* Method: POST

* Request Body: JSON object containing form data.

* Response:

  * If a matching template is found: JSON object with the template name.
  * If no match is found: JSON object with inferred field names and types.

  Example Response:
   ```json 
  {
    "template_name": "example_template"
    }
  ```
    Example Response (No Match):
    ```json 
  {
    "f_name1": "date_type",
    "f_name2": "phone_type"
    }
  ```
  