from openai import OpenAI
from voicettss import generate_and_send_audio
import asyncio
import os

client = OpenAI(api_key='')

def get_response(prompt):
    global response
    global messageapi
    print('Prompt Gathered: ',prompt)
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo"
    )
    messageapi = response.choices[0].message.content
    print('Response Gathered: ',messageapi)
    generate_and_send_audio(messageapi)