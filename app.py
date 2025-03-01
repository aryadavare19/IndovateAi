# import os
# import google.generativeai as genai
# from flask import Flask, request, jsonify, render_template
# from dotenv import load_dotenv

# # Load environment variables from the correct directory
# dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
# load_dotenv(dotenv_path)

# # Get API Key
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if not GEMINI_API_KEY:
#     raise ValueError("API key not found. Set GEMINI_API_KEY in the .env file.")

# # Configure Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# # Initialize Flask app
# app = Flask(__name__, template_folder="templates")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get_advice", methods=["POST"])
# def get_advice():
#     try:
#         data = request.json
#         user_input = data.get("symptoms", "")

#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(f"I have {user_input}. What could it be and what should I do?")

#         return jsonify({"advice": response.text})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
# import os
# import google.generativeai as genai
# from flask import Flask, request, jsonify
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Get API Key
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if not GEMINI_API_KEY:
#     raise ValueError("API key not found. Set GEMINI_API_KEY in the .env file.")

# # Configure Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# # Initialize Flask app
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return jsonify({"message": "Welcome to the AI Health Assistant API!"})

# @app.route("/get_advice", methods=["POST"])
# @app.route("/get_advice", methods=["POST"])
# def get_advice():
#     try:
#         data = request.json
#         print("Received data:", data)  # Debugging

#         user_input = data.get("symptoms", "")
#         if not user_input:
#             return jsonify({"error": "No symptoms provided"}), 400

#         model = genai.GenerativeModel("gemini-2.0")
#         response = model.generate_content(f"I have {user_input}. What could it be and what should I do?")

#         print("API Response:", response)  # Debugging

#         return jsonify({"advice": response.text})

#     except Exception as e:
#         print("Error:", str(e))  # Debugging
#         return jsonify({"error": str(e)}), 500
# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=8000)


# from flask import Flask, request, jsonify
# import requests
# import os

# app = Flask(__name__)

# API_KEY = os.getenv("GEMINI_API_KEY")  # Load API key from environment variable
# API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"


# @app.route("/get_advice", methods=["POST"])
# def get_advice():
#     data = request.json
#     user_input = data["symptoms"]

#     payload = {
#         "contents": [{"parts": [{"text": f"I have {user_input}. What could it be and what should I do?"}]}]
#     }
#     headers = {"Content-Type": "application/json"}

#     response = requests.post(API_URL, json=payload, headers=headers)
    
#     if response.status_code == 200:
#         return jsonify({"advice": response.json()})
#     else:
#         return jsonify({"error": "Failed to get response"}), response.status_code

# if __name__ == "__main__":
#     app.run(debug=True)
#     """_summary_
#     Invoke-RestMethod -Uri "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=YOUR_API_KEY" `
# -Method POST `
# -Headers @{"Content-Type"="application/json"} `
# -Body '{"contents": [{"parts":[{"text": "Explain how AI works"}]}]}'

#     """
from flask import Flask, jsonify, request
from flask_cors import CORS  # Allow API requests from Streamlit

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests

@app.route('/api/get_data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/send_data', methods=['POST'])
def send_data():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid data"}), 400
    return jsonify({"response": f"Received: {data['message']}"})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=8000)  # Use a different port
