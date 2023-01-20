from flask import Flask, request, jsonify
import openai
from urllib.parse import quote
app = Flask(__name__)

# Set the API key
openai.api_key = "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"


@app.route("/generate", methods=["GET"])
def generateParaPhraser():
    # Get the input string from the request
    processInput = "Read the input and " \
                   "predict 5 suggestions to rephrase the input. " \
                   "Separate the predicted sentences with a semi colon. Here is the input: "
    processInput += request.json["input_string"]
    # Generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=processInput,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )

    generated_sentences = response["choices"]

    # Get the first generated sentence
    generated_sentence = generated_sentences[0]["text"]

    # Create a JSON object containing the generated sentence
    result = {"generated_sentence": generated_sentence}

    # Return the JSON object
    return jsonify(result)


@app.route("/generate-sentence", methods=["GET"])
def generateSentenceSuggestion():
    # Get the input string from the request
    processInput = "Read the following input and predict the next sentence. " \
                   "Please make 5 predictions." \
                   "Separate the predicted sentences with a semi colon. Here is the input: "
    processInput += request.json["input_string"]
    # Generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=processInput,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )

    generated_sentences = response["choices"]

    # Get the first generated sentence
    generated_sentence = generated_sentences[0]["text"]

    # Create a JSON object containing the generated sentence
    result = {"generated_sentence": generated_sentence}

    # Return the JSON object
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="192.168.217.253", port=8081)
