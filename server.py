"""
server.py

Flask web application for the Emotion Detector.

Routes
------
GET /                 -> renders the index page (templates/index.html)
GET /emotionDetector   -> takes ?textToAnalyze=... and returns a formatted
                          string with the emotion scores and dominant emotion,
                          or an error message for blank/invalid input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Serve the main page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text passed in the textToAnalyze query parameter."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    # Error handling: blank/invalid input comes back with dominant_emotion=None
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
