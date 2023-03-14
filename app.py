import time
from brain import ask_chat_gpt
from voice import say, play_mp3
from ears import get_audio_text, get_most_likely_phrase
from config import KEYWORD, READY_SOUND

def is_key_word_in_text(text):
    return KEYWORD in [word.lower() for sentence in text["alternative"] for word in sentence["transcript"].split()]

def get_keyword_loop():
    while True:
        seconds_to_listen = 3
        text = get_audio_text(seconds_to_listen)
        if text is None:
            continue
        if is_key_word_in_text(text):
            return     

def get_instruction_loop():
    t_end = time.time() + 60 * 5
    while time.time() < t_end:
        text = get_audio_text()
        if text is None:
            continue

        response = ask_chat_gpt(get_most_likely_phrase(text))
        response_text = response['choices'][0]['message']['content']
        print(response_text)
        say(response_text)
        return 

while True:
    get_keyword_loop()
    play_mp3(READY_SOUND)
    get_instruction_loop()
