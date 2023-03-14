import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')

def ask_chat_gpt(phrase):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are my knowledgable friend and co-worker. You keep everything short and sweet."},
            {"role": "user", "content": "%s" % phrase}
        ]
    )
    return response
    