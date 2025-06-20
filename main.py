from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/generate', methods=['POST'])
def generate():
    # LLM to get name of an e-commerce store from a product name
    prompt = PromptTemplate.from_template("Act as an Digital Content cretaer and SEO specilist, Please create an Blog on the topic : {title}?")
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.3)
    chain = LLMChain(llm=llm, prompt=prompt)
    data = request.get_json()  # Reading JSON data from frontend
    title = data.get('prompt')
    output = chain.run(title)

    # Dummy response for now
    return jsonify({"output": output})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
