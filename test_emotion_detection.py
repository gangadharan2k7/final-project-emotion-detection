
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        res1 = emotion_detector("I am glad this happened")
        self.assertEqual(res1['dominant_emotion'], 'joy')

if __name__ == '__main__':
    unittest.main()
