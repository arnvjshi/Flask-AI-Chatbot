# AI ChatBOT

An interactive AI-powered chatbot application built using Flask as the backend framework. It leverages HuggingFace's `HuggingFaceHub` API to generate responses to user prompts, with a focus on extracting English responses.

## Features

- **Interactive Frontend**: Simple and clean HTML interface.
- **AI-Powered Backend**: Uses HuggingFace's `starchat-beta` model for generating responses.
- **Bidirectional Communication**: JavaScript communicates with the Python backend.

## Project Structure

project/ │ ├── app.py # Python Backend ├── index.html # HTML Frontend ├── script.js # JavaScript for Frontend

diff
Copy code

## Requirements

- Python 3.x
- Flask
- langchain
- huggingface_hub
- langdetect

## Installation

1. Clone the repository or download the project folder.
2. Install required Python dependencies:
   ```bash
   pip install flask langchain huggingface_hub langdetect
Ensure you have a valid HuggingFace API key for the HuggingFaceHub model. Replace the API key in the app.py file.

Run the Flask app:
python app.py
Open your browser and navigate to http://127.0.0.1:8501.

How It Works
Frontend: The HTML file provides a basic UI where users can enter a prompt.
JavaScript: The script.js handles communication with the Flask backend via AJAX (fetch).
Backend: The Python Flask server processes the input using the HuggingFace model, extracts the English portion of the AI response, and sends it back to the frontend.
Troubleshooting
If you see the error jinja2.exceptions.TemplateNotFound: index.html, ensure that the index.html file is in the same directory as app.py, and make sure Flask is configured to look for templates in the current directory.

If you encounter any issues with generating responses, check that your HuggingFace API token is valid and set in app.py.

License
This project is open-source and available under the MIT License. See the LICENSE file for more information.

This is the full content of the `README.md` file in markdown format, which includes all relevant sections for your project. You can copy and paste this into a `README.md` file in your project directory.
