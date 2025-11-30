from flask import Blueprint, request, jsonify
from Service import call_gemini

gemini_bp = Blueprint("gemini", __name__)

@gemini_bp.route("/ask", methods=["POST"])
def ask_gemini():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = call_gemini(prompt)
    return jsonify({"response": response})