import logging
import os
import config
import openai

from dotenv import load_dotenv

load_dotenv()
OPEN_API_GPT_SECRET_KEY = os.getenv('OPEN_API_GPT_SECRET_KEY')

if not OPEN_API_GPT_SECRET_KEY:
    raise EnvironmentError('You should set OPEN_API_GPT_SECRET_KEY in your environment variable in .env file')


class TitleGenerator:
    def __init__(self, temperature=config.TEMPERATURE[1], max_tokens=config.MAX_TOKENS[0], top_p=config.TOP_P,
                 frequency_penalty=config.FREQUENCY_PENALTY[2], presence_penalty=config.PRESENCE_PENALTY[0]):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def generate_title(self, keywords: list):
        try:
            openai.api_key = OPEN_API_GPT_SECRET_KEY
            keywords = ' '.join(keywords)
            model = openai.Completion.create(
                engine='text-davinci-001',
                prompt=f'Keywords: {keywords}\ngenerate short tagline for the content:',
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty
            )

            headline = model['choices'][0]['text'].strip()
            headline = headline.strip('Re:').strip()
            headline = config.space_remover.sub(' ', headline)

            return headline

        except Exception as e:
            message = f'Something went wrong with generating titles, message: {e}'
            logging.error(message, exc_info=True)


content = TitleGenerator()
print(content.generate_title(config.KEYWORDS))
