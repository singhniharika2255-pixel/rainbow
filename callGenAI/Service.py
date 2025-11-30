import google.generativeai as genai
import os
#import logger
from datetime import datetime

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(prompt: str) -> str:
    """Call Gemini AI with a prompt and log the response."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    # Extract text
    result_text = response.text

    # Log the request and response
    #logger.info("Prompt: %s", prompt)
    #logger.info("Gemini Response: %s", result_text)

    # Log response
    with open("result.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - PROMPT: {prompt}\n")
        log_file.write(f"{datetime.now()} - RESPONSE: {result_text}\n\n")




    return result_text