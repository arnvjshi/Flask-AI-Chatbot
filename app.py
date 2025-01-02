from flask import Flask, jsonify, request, render_template, send_from_directory
from langchain import HuggingFaceHub, LLMChain, PromptTemplate
import re

from langdetect import detect
import os

app = Flask(__name__, template_folder='.')

# HuggingFace API Key
api_key = "<--API key-->"
model = "HuggingFaceH4/starchat-beta"

# Create LLMChain
def create_llm_chain(api_key):
    llm = HuggingFaceHub(
        repo_id=model,
        huggingfacehub_api_token=api_key,
        model_kwargs={
            "min_length": 30,
            "max_new_tokens": 256,
            "temperature": 0.9,
            "top_k": 50,
            "top_p": 0.95,
            "eos_token_id": 49155
        }
    )
    prompt_template = PromptTemplate(
        input_variables=["user_input"],
        template="{user_input}"
    )
    return LLMChain(prompt=prompt_template, llm=llm)

llm_chain = create_llm_chain(api_key)

def extract_english(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    english_sentences = []
    for sentence in sentences:
        try:
            if detect(sentence) == 'en':
                english_sentences.append(sentence)
            else:
                break
        except:
            break
    return ' '.join(english_sentences).strip()

@app.route('/')
def index():
    return render_template('index.html')  # Flask will now look for `index.html` in the current directory.

@app.route('/script.js')
def serve_js():
    return send_from_directory(os.path.dirname(__file__), 'script.js')

@app.route('/api/generate', methods=['POST'])
def generate_response():
    data = request.json
    user_input = data.get("prompt", "")
    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400
    try:
        llm_reply = llm_chain.run(user_input)
        reply = llm_reply.split("AI:")[-1].strip()
        english_reply = extract_english(reply)
        return jsonify({"response": english_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8501, debug=True)
