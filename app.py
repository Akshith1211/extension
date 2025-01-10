# import os
# import io
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from PIL import Image
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# app = Flask(__name__)
# CORS(app)

# # Function to interact with Gemini API
# def get_gemini_response(input_text, input_image=None):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         # Process image and text for the API
#         response = model.generate_content([input_text, input_image])
#         return response.text
#     except Exception as e:
#         return f"Error communicating with Gemini API: {str(e)}"


# @app.route('/analyze', methods=['POST'])
# def analyze_image():
#     try:
#         # Get the image data from the raw request body (binary data)
#         img_data = request.data

#         if not img_data:
#             return jsonify({"error": "No image data provided"}), 400

#         # Open the image using PIL from binary data
#         image = Image.open(io.BytesIO(img_data))

#         # Prepare input for Gemini API
#         input_text = "Analyze the error in this image:"
#         response_text = get_gemini_response(input_text, image)

#         # Format the response
#         response_format = {
#             "Explanation": response_text,
#         }

#         return jsonify(response_format)

#     except Exception as e:
#         return jsonify({"error": f"Failed to process image: {str(e)}"}), 500



# if __name__ == '__main__':
#     app.run(debug=True)

# ------------------------



# import os
# import io
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from PIL import Image
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# app = Flask(__name__)
# CORS(app)

# # Function to interact with Gemini API
# def get_gemini_response(input_text, input_image=None):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         # Process image and text for the API
#         response = model.generate_content([input_text, input_image])
#         return response.text
#     except Exception as e:
#         return f"Error communicating with Gemini API: {str(e)}"


# @app.route('/analyze', methods=['POST'])
# def analyze_image():
#     try:
#         # Get the image data from the raw request body (binary data)
#         img_data = request.data

#         if not img_data:
#             return jsonify({"error": "No image data provided"}), 400

#         # Open the image using PIL from binary data
#         image = Image.open(io.BytesIO(img_data))

#         # Prepare input for Gemini API
#         input_text = "Analyze the error in this image:"
#         response_text = get_gemini_response(input_text, image)

#         # Format the response
#         response_format = {
#             "Explanation": response_text,
#         }

#         return jsonify(response_format)

#     except Exception as e:
#         return jsonify({"error": f"Failed to process image: {str(e)}"}), 500



# if __name__ == '__main__':
#     app.run(debug=True)


# ---------------

# import os
# import io
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from PIL import Image
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# app = Flask(__name__)
# CORS(app)

# # Function to interact with Gemini API
# def get_gemini_response(input_text, input_image=None):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         # Process image and text for the API
#         response = model.generate_content([input_text, input_image])
#         return response.text
#     except Exception as e:
#         return f"Error communicating with Gemini API: {str(e)}"

# @app.route('/analyze', methods=['POST'])
# def analyze_image():
#     try:
#         img_data = request.data

#         if not img_data:
#             return jsonify({"error": "No image data provided"}), 400

#         # Open the image using PIL
#         image = Image.open(io.BytesIO(img_data))

#         # Call the Gemini API to get the analysis
#         input_text = "Analyze the error in this image:"
#         response_text = get_gemini_response(input_text, image)

#         if response_text:
#             # Split the response text into individual sentences
#             sentences = response_text.split(".")
            
#             # Clean up and enumerate sentences
#             formatted_sentences = []
#             for i, sentence in enumerate(sentences, start=1):
#                 sentence = sentence.strip()
#                 if sentence:  # Exclude empty sentences
#                     formatted_sentences.append(f"{i}. {sentence}")

#             # Join the sentences with newlines for JSON response
#             formatted_response = "\n".join(formatted_sentences)
#         else:
#             formatted_response = "No response from Gemini API."

#         return jsonify({"Explanation": formatted_response})

#     except Exception as e:
#         return jsonify({"error": f"Failed to process image: {str(e)}"}), 500


# # @app.route('/analyze', methods=['POST'])
# # def analyze_image():
# #     try:
# #         img_data = request.data

# #         if not img_data:
# #             return jsonify({"error": "No image data provided"}), 400

# #         # Open the image using PIL
# #         image = Image.open(io.BytesIO(img_data))

# #         # Call the Gemini API to get the analysis
# #         input_text = "Analyze the error in this image:"
# #         response_text = get_gemini_response(input_text, image)

# #         if response_text:
# #             # Split the response text into individual sentences
# #             sentences = response_text.split(".")

# #             # Clean up sentences and join with line breaks
# #             formatted_sentences = [
# #                 f"{i}. {sentence.strip()}" for i, sentence in enumerate(sentences, start=1) if sentence.strip()
# #             ]

# #             # Join the sentences with newlines for JSON response
# #             formatted_response = "\n".join(formatted_sentences)
# #         else:
# #             formatted_response = "No response from Gemini API."

# #         return jsonify({"Explanation": formatted_response})

# #     except Exception as e:
# #         return jsonify({"error": f"Failed to process image: {str(e)}"}), 500


# if __name__ == '__main__':
#     app.run(debug=True)

# --------------------

# import os
# import io
# import openai
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from PIL import Image
# import pytesseract

# # Load environment variables
# load_dotenv()

# # Configure OpenAI API key
# openai.api_key = os.getenv("CHATGPT_API_KEY")

# app = Flask(__name__)
# CORS(app)

# # Function to interact with ChatGPT API (v1.0.0+)
# def get_chatgpt_response(input_text):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are an assistant that analyzes text from images and provides explanations."},
#                 {"role": "user", "content": input_text}
#             ]
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         return f"Error communicating with ChatGPT API: {str(e)}"

# @app.route('/analyze', methods=['POST'])
# def analyze_image():
#     try:
#         img_data = request.data

#         if not img_data:
#             return jsonify({"error": "No image data provided"}), 400

#         # Open the image using PIL
#         image = Image.open(io.BytesIO(img_data))

#         # Extract text from the image using pytesseract
#         extracted_text = pytesseract.image_to_string(image)

#         if not extracted_text.strip():
#             return jsonify({"error": "No text found in the image"}), 400

#         # Pass the extracted text to ChatGPT for analysis
#         input_text = f"The following text was extracted from an image:\n\n{extracted_text}\n\nAnalyze this text and provide an explanation."
#         response_text = get_chatgpt_response(input_text)

#         if response_text:
#             return jsonify({"Explanation": response_text})
#         else:
#             return jsonify({"Explanation": "No response from ChatGPT API."})

#     except Exception as e:
#         return jsonify({"error": f"Failed to process image: {str(e)}"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# -------------------

# import os
# import io
# import openai
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from PIL import Image
# import pytesseract

# # Load environment variables
# load_dotenv()

# # Configure OpenAI API key
# openai.api_key = os.getenv("CHATGPT_API_KEY")

# app = Flask(__name__)
# CORS(app)

# # Function to interact with ChatGPT API (v1.0.0+)
# def get_chatgpt_response(input_text):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are an assistant that analyzes text from images and provides explanations."},
#                 {"role": "user", "content": input_text}
#             ]
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         return f"Error communicating with ChatGPT API: {str(e)}"

# @app.route('/analyze', methods=['POST'])
# def analyze_image():
#     try:
#         img_data = request.data

#         if not img_data:
#             return jsonify({"error": "No image data provided"}), 400

#         # Open the image using PIL
#         image = Image.open(io.BytesIO(img_data))

#         # Extract text from the image using pytesseract
#         extracted_text = pytesseract.image_to_string(image)

#         if not extracted_text.strip():
#             return jsonify({"error": "No text found in the image"}), 400


#         # input_text = (
#         #     f"The following text was extracted from an image:\n\n{extracted_text}\n\n"
#         #     "As an expert in API troubleshooting and code debugging, your role is to analyze errors, "
#         #     "diagnose their root causes, and provide clear explanations and solutions. When presented with an error:\n\n"
#         #     "1. Carefully examine the error message, status code (if applicable), and any additional context provided.\n"
#         #     "2. Identify the type of error (e.g., API-related, syntax error, runtime error, logical error).\n"
#         #     "3. Explain the error in simple terms, avoiding overly technical jargon.\n"
#         #     "4. Suggest potential causes for the error, considering common pitfalls and best practices.\n"
#         #     "5. Provide step-by-step troubleshooting instructions, including how to:\n"
#         #     "   - Verify API credentials and authentication (if applicable)\n"
#         #     "   - Check request formatting and parameters (for API errors)\n"
#         #     "   - Validate data being sent or processed\n"
#         #     "   - Test API endpoints or specific code sections\n"
#         #     "   - Review logs or error messages\n"
#         #     "6. Recommend tools or techniques for debugging (e.g., API testing tools, logging, debuggers, print statements).\n"
#         #     "7. Offer potential solutions or workarounds for the error.\n"
#         #     "8. If relevant, suggest preventive measures to avoid similar errors in the future.\n"
#         #     "9. Be prepared to explain API concepts, HTTP methods, status codes, and common programming concepts as needed.\n"
#         #     "10. If the error seems unique or complex, provide resources for further research or suggest escalation paths."
#         # )

#         input_text = (
#     f"The following text was extracted from an image:\n\n{extracted_text}\n\n"
#     "As an expert in API troubleshooting and code debugging, analyze the errors and provide an explanation in a structured manner. "
#     "Please ensure each point is listed on a new line, formatted like this:\n"
#     "1. Explanation point one.\n"
#     "2. Explanation point two.\n"
#     "3. Explanation point three.\n\n"
#     "When diagnosing the error, follow these steps:\n\n"
#     "1. Carefully examine the error message, status code (if applicable), and any additional context provided.\n"
#     "2. Identify the type of error (e.g., API-related, syntax error, runtime error, logical error).\n"
#     "3. Explain the error in simple terms, avoiding overly technical jargon.\n"
#     "4. Suggest potential causes for the error, considering common pitfalls and best practices.\n"
#     "5. Provide step-by-step troubleshooting instructions, including how to:\n"
#     "   - Verify API credentials and authentication (if applicable)\n"
#     "   - Check request formatting and parameters (for API errors)\n"
#     "   - Validate data being sent or processed\n"
#     "   - Test API endpoints or specific code sections\n"
#     "   - Review logs or error messages\n"
#     "6. Recommend tools or techniques for debugging (e.g., API testing tools, logging, debuggers, print statements).\n"
#     "7. Offer potential solutions or workarounds for the error.\n"
#     "8. If relevant, suggest preventive measures to avoid similar errors in the future.\n"
#     "9. Be prepared to explain API concepts, HTTP methods, status codes, and common programming concepts as needed.\n"
#     "10. If the error seems unique or complex, provide resources for further research or suggest escalation paths."
# )



#         response_text = get_chatgpt_response(input_text)

#         if response_text:
#             return jsonify({"Explanation": response_text})
#         else:
#             return jsonify({"Explanation": "No response from ChatGPT API."})

#     except Exception as e:
#         return jsonify({"error": f"Failed to process image: {str(e)}"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


# ----------

import os
import io
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract

# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv("CHATGPT_API_KEY")

app = Flask(__name__)
CORS(app)

def get_chatgpt_response(input_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that analyzes text from images and user prompts."},
                {"role": "user", "content": input_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with ChatGPT API: {str(e)}"

@app.route('/analyze', methods=['POST'])
def analyze_image():
    try:
        if 'image' not in request.files or 'prompt' not in request.form:
            return jsonify({"error": "Image or prompt missing."}), 400

        img_file = request.files['image']
        user_prompt = request.form['prompt']

        # Open the image
        image = Image.open(img_file.stream)

        # Extract text using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        # Combine extracted text with user prompt
        input_text = f"""
        Extracted text from the image:
        {extracted_text.strip()}

        User prompt:
        {user_prompt.strip()}

        "As an expert in API troubleshooting and code debugging, analyze the errors and provide an explanation in a structured manner. "
    "Please ensure each point is listed on a new line, formatted like this:\n"
    "1. Explanation point one.\n"
    "2. Explanation point two.\n"
    "3. Explanation point three.\n\n"
    "When diagnosing the error, follow these steps:\n\n"
    "1. Carefully examine the error message, status code (if applicable), and any additional context provided.\n"
    "2. Identify the type of error (e.g., API-related, syntax error, runtime error, logical error).\n"
    "3. Explain the error in simple terms, avoiding overly technical jargon.\n"
    "4. Suggest potential causes for the error, considering common pitfalls and best practices.\n"
    "5. Provide step-by-step troubleshooting instructions, including how to:\n"
    "   - Verify API credentials and authentication (if applicable)\n"
    "   - Check request formatting and parameters (for API errors)\n"
    "   - Validate data being sent or processed\n"
    "   - Test API endpoints or specific code sections\n"
    "   - Review logs or error messages\n"
    "6. Recommend tools or techniques for debugging (e.g., API testing tools, logging, debuggers, print statements).\n"
    "7. Offer potential solutions or workarounds for the error.\n"
    "8. If relevant, suggest preventive measures to avoid similar errors in the future.\n"
    "9. Be prepared to explain API concepts, HTTP methods, status codes, and common programming concepts as needed.\n"
    "10. If the error seems unique or complex, provide resources for further research or suggest escalation paths."
)
        """

        response_text = get_chatgpt_response(input_text)

        if response_text:
            return jsonify({"Explanation": response_text})
        else:
            return jsonify({"Explanation": "No response from ChatGPT API."})

    except Exception as e:
        return jsonify({"error": f"Failed to process the request: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
