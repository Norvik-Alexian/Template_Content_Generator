import logging
import os
import config
import openai

from dotenv import load_dotenv

load_dotenv()
OPEN_API_GPT_SECRET_KEY = os.getenv('OPEN_API_GPT_SECRET_KEY')

if not OPEN_API_GPT_SECRET_KEY:
    raise EnvironmentError('You should set OPEN_API_GPT_SECRET_KEY in your environment variable in .env file')


class AboutUsGenerator:
    def __init__(self, temperature=config.TEMPERATURE[1], max_tokens=config.MAX_TOKENS[1], top_p=config.TOP_P,
                 frequency_penalty=config.FREQUENCY_PENALTY[0], presence_penalty=config.PRESENCE_PENALTY[0]):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def generate_content(self, keywords: list):
        try:
            openai.api_key = OPEN_API_GPT_SECRET_KEY
            keywords = ' '.join(keywords)
            model = openai.Completion.create(
                engine='text-davinci-001',
                prompt=f'Keywords: {keywords}\ngenerate about us content for the product:',
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty
            )
            generated_content = model['choices'][0]['text']

            return generated_content, model

        except Exception as e:
            message = f'Something went wrong with generating about us content, message: {e}'
            logging.error(message, exc_info=True)

    @staticmethod
    def prettify(content: str, finish_reason: str):
        try:
            if finish_reason == 'stop':
                ending_punctuations = config.ENDING_PUNCTUATIONS
                any_finished_sentence = any([mark in content for mark in ending_punctuations])
                if any_finished_sentence:
                    reversed_content = content[::-1]
                    last_finished_sentence = len(content) - 1 - min([
                        reversed_content.index(mark) for mark in ending_punctuations if mark in content
                    ])
                    content = content[: last_finished_sentence + 1]

            content = config.space_remover.sub(' ', content)

            return content

        except Exception as e:
            message = f'Something went wrong with prettifying the content, message: {e}'
            logging.error(message, exc_info=True)

    def about_us_content(self):
        try:
            generated_content, model = self.generate_content(config.KEYWORDS)
            content = generated_content.strip()
            finish_reason = model['choices'][0]['finish_reason']

            return self.prettify(content, finish_reason)

        except Exception as e:
            message = f'Something went wrong with about us content, message: {e}'
            logging.error(message, exc_info=True)


content = AboutUsGenerator()
print(content.about_us_content())