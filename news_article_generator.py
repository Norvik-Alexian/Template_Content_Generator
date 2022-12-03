import os
import config
import openai
import logging

from utils import prettify
from dotenv import load_dotenv

load_dotenv()
OPEN_API_GPT_SECRET_KEY = os.getenv('OPEN_API_GPT_SECRET_KEY')

if not OPEN_API_GPT_SECRET_KEY:
    raise EnvironmentError('You should set OPEN_API_GPT_SECRET_KEY in your environment variable in .env file')


class NewsArticleGenerator:
    def __init__(self,
                 temperature=config.TEMPERATURE,
                 max_tokens=config.MAX_TOKENS,
                 top_p=config.TOP_P,
                 frequency_penalty=config.FREQUENCY_PENALTY,
                 presence_penalty=config.PRESENCE_PENALTY):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    @property
    def generate_news_article(self):
        try:
            openai.api_key = OPEN_API_GPT_SECRET_KEY
            keywords = ' '.join(config.KEYWORDS)
            model = openai.Completion.create(
                engine='text-davinci-002',
                prompt=f'Generate News Article within the Keywords\nKeywords: {keywords}\nNews Article:',
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty
            )

            generated_content = model['choices'][0]['text'].strip()
            finish_reason = model['choices'][0]['finish_reason']

            return prettify(generated_content, finish_reason)
        except Exception as e:
            message = f'Something went wrong with generating news article content, message: {e}'
            logging.error(message, exc_info=True)


content = NewsArticleGenerator()
print(content.generate_news_article)