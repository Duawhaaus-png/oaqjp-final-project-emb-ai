"""
emotion_detection.py

Core logic for the Emotion Detector application.

- emotion_detector(text_to_analyze): calls the Watson NLP EmotionPredict
  service and returns a formatted dictionary of emotion scores plus the
  dominant emotion.
- Handles blank / invalid input by returning None for every field, so the
  Flask layer can turn that into a friendly error message.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Send text to the Watson NLP EmotionPredict service and return a
    dictionary with the scores for anger, disgust, fear, joy, sadness,
    and the dominant emotion.

    Parameters
    ----------
    text_to_analyze : str
        The text the user wants analyzed.

    Returns
    -------
    dict
        {
            'anger': float,
            'disgust': float,
            'fear': float,
            'joy': float,
            'sadness': float,
            'dominant_emotion': str
        }
        All values are None if the input is blank/invalid or the service
        call fails (mirrors a 400 response from Watson NLP).
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Guard clause: blank/whitespace-only input never even hits the service.
    if not text_to_analyze or not text_to_analyze.strip():
        return _blank_result()

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return _blank_result()

    # Watson NLP returns 400 for input it considers invalid.
    if response.status_code == 400:
        return _blank_result()

    if response.status_code != 200:
        return _blank_result()

    try:
        response_dict = json.loads(response.text)
        emotions = response_dict["emotionPredictions"][0]["emotion"]

        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
        }
        dominant_emotion = max(scores, key=scores.get)

        scores["dominant_emotion"] = dominant_emotion
        return scores
    except (KeyError, IndexError, json.JSONDecodeError):
        return _blank_result()


def _blank_result():
    """Standard 'no result' payload used for blank input or any failure."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
