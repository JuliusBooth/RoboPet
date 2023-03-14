from gtts import gTTS
import os
from config import RESOURCES_DIR

def play_mp3(file, tempo=1):
    os.system('play %s tempo %s' % (file, tempo))

def say(text):
    tts = gTTS(text, tld="us")
    temp_file = os.path.join(RESOURCES_DIR, "temp.mp3")
    tts.save(temp_file)
    play_mp3(temp_file, 1.6)
