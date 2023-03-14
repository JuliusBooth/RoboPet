import speech_recognition as sr

def get_most_likely_phrase(text):
    return text["alternative"][0]["transcript"]

def get_audio_text(phrase_time_limit=10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=phrase_time_limit)
        print("Got it! Now to recognize it...")
        try:
            text = r.recognize_google(audio, show_all=True)
            print("Google Speech Recognition thinks you said " + get_most_likely_phrase(text))
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except:
            print(text)
            print("Unknown error")
    return None
