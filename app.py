from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=os.environ["API_KEY"])

def call_gemini_ai(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text

@app.route('/generate-sql', methods=['POST'])
def generate_sql():
    data = request.json
    user_input = data.get('user_input', '')

    sql_code = call_gemini_ai(user_input)

    return jsonify({'sql_code': sql_code})

if __name__ == '__main__':
    app.run(debug=True)