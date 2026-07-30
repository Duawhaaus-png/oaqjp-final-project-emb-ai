# Emotion Detector (Watson NLP + Flask)

An AI-based web application that detects the emotions (anger, disgust, fear,
joy, sadness) expressed in a piece of text, using the Watson NLP
EmotionPredict service, and serves it through a Flask web app.

## Project structure

```
emotion_detector/
├── EmotionDetection/
│   ├── __init__.py            # package entry point
│   └── emotion_detection.py   # emotion_detector() core logic
├── templates/
│   └── index.html             # front-end page
├── static/                    # (optional) css/js assets
├── server.py                  # Flask app (routes: / and /emotionDetector)
├── test_emotion_detection.py  # unit tests
├── requirements.txt
└── README.md
```

## 1. Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Run the unit tests (package validation)

```bash
python -m unittest test_emotion_detection.py -v
```

## 3. Run the Flask app

```bash
python server.py
```

Then open `http://localhost:5000` in a browser, type a sentence, and click
**Analyze**.

You can also call the API endpoint directly:

```
GET http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy%20today
```

Sample success response:

```
For the given statement, the system response is 'anger': 0.0064, 'disgust': 0.0057,
'fear': 0.0063, 'joy': 0.9733 and 'sadness': 0.0074. The dominant emotion is joy.
```

Sample error response (blank input):

```
Invalid text! Please try again!
```

## 4. Error handling

`emotion_detector()` returns `None` for every field (including
`dominant_emotion`) when:
- the input text is blank or whitespace-only,
- the Watson NLP service returns a 400 (invalid input), or
- the request otherwise fails.

`server.py` checks `dominant_emotion is None` and returns
`"Invalid text! Please try again!"` instead of a formatted result.

## 5. Static code analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py test_emotion_detection.py
```

## 6. Publishing to GitHub

```bash
git init
git add .
git commit -m "Emotion Detector final project"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```
