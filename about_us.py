import os
import openai

from dotenv import load_dotenv

load_dotenv()
OPEN_API_GPT_SECRET_KEY = os.getenv('OPEN_API_GPT_SECRET_KEY')

if not OPEN_API_GPT_SECRET_KEY:
    raise EnvironmentError('You should set OPEN_API_GPT_SECRET_KEY in your environment variable in .env file')


def generate_about_us_content(keywords: list):
    openai.api_key = OPEN_API_GPT_SECRET_KEY
    keywords = ' '.join(keywords)
    model = openai.Completion.create(
        engine='text-davinci-001',
        prompt=f'Keywords: {keywords}\nwrite long content about the content:',
        temperature=0.6,
        max_tokens=600,
        top_p=1.,
        frequency_penalty=0.2,
        presence_penalty=0.
    )
    generated_content = model['choices'][0]['text']

    return generated_content
