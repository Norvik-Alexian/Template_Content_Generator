import os
import config
import openai

from dotenv import load_dotenv

load_dotenv()
OPEN_API_GPT_SECRET_KEY = os.getenv('OPEN_API_GPT_SECRET_KEY')

if not OPEN_API_GPT_SECRET_KEY:
    raise EnvironmentError('You should set OPEN_API_GPT_SECRET_KEY in your environment variable in .env file')


def generate_title(keywords: list):
    openai.api_key = OPEN_API_GPT_SECRET_KEY
    keywords = ' '.join(keywords)
    model = openai.Completion.create(
        engine='text-davinci-001',
        prompt=f'Keywords: {keywords}\ngenerate short headline for the content:',
        temperature=1.,
        max_tokens=15,
        top_p=1.,
        frequency_penalty=1.5,
        presence_penalty=0.
    )

    headline = model['choices'][0]['text'].strip()
    headline = headline.strip('Re:').strip()
    headline = config.space_remover.sub(' ', headline)

    return headline

print(generate_title(config.KEYWORDS))