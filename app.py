import os
import logging
from flask import Flask, request, jsonify
from google import genai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gemini-flask")

# Load API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable not set.")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Create Flask app
app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate_text():
    try:
        # Get JSON body
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Call Gemini API
        response = client.models.generate_content(
            model="gemini-2.5-flash",   # or gemini-1.5-pro
            contents=prompt
        )

        # Log the request and response
        logger.info("Prompt: %s", prompt)
        logger.info("Gemini Response: %s", response.text)

        # Return response to client
        return jsonify({"result": response.text})

    except Exception as e:
        logger.error("Error calling Gemini API: %s", str(e))
        return jsonify({"error": "Gemini API call failed,Please try again"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)