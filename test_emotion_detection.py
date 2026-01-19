import unittest
from EmotionDetection import emotion_detection

class TestEmotionDetector(unittest.TestCase):
  
    def test_emotion_joy(self):
        result = emotion_detection.emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_anger(self):
        result = emotion_detection.emotion_detector("I am really angry about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_disgust(self):
        result = emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_sadness(self):
        result = emotion_detection.emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_fear(self):
        result = emotion_detection.emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()