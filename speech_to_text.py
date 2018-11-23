import speech_recognition as sr  # import the library
import requests
# from urllib.error import HTTPError
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PIL import Image
from io import BytesIO
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pyaudio

def speech2text():
    r = sr.Recognizer()  # initialize recognizer
    # trying to fix it on linux
    #myPyAudio = pyaudio.PyAudio()
    #index = myPyAudio.get_device_count()

    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")

    return text


def evaluate_sentient(s):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(s)


def text2img(text):
    api_key = '5ac6d2d46f6b4366ba5dfa2691912f4f'
    search_term = text
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": search_term, "license": "public", "imageType": "photo"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    for result in search_results['value']:
        try:
            r = requests.get(result['contentUrl'], verify=False)
            image = Image.open(BytesIO(r.content))
            image.show()
        except TypeError as err:
            print(err)

    return
