"""
test_emotion_detection.py

Unit tests for EmotionDetection.emotion_detector.

Run with:
    python -m unittest test_emotion_detection.py -v
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verifies emotion_detector() returns the expected dominant emotion
    for one example sentence per emotion, plus blank-input handling."""

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_blank_input_returns_none(self):
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])
        self.assertIsNone(result["disgust"])
        self.assertIsNone(result["fear"])
        self.assertIsNone(result["joy"])
        self.assertIsNone(result["sadness"])

    def test_whitespace_input_returns_none(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
