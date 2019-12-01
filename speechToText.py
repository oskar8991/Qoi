import pyaudio
import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        print("Speech To Text initialized...")

    def recognizeSpeech(self):
        # obtain audio from the microphone
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            
        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
            return r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


