"""Flask server for Emotion Detection application using Watson NLP."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the main page of the application.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Analyze the emotion of the provided text and return formatted response.
    
    Returns:
        str: Emotion scores with dominant emotion, or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detection.emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    