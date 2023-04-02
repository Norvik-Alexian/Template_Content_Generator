import re

ENDING_PUNCTUATIONS = ['.', '!']
SPACE_REMOVER_PATTERN = re.compile(r'\s+')
MODEL = 'gpt-3.5-turbo	'
TEMPERATURE = 0.7
MAX_TOKENS = 80
TOP_P = 1.
FREQUENCY_PENALTY = 1.
PRESENCE_PENALTY = 1.
N = 1
STOP = None
ABOUT_US_PROMPT = f'''Write an "About Us" content in more than 2 paragraphs within the Keywords and include company
mission and purpose, establish a mission statement, explain who you serve, explain what you're offering and what makes
you unique, describe your values, direct customer towards the next action:'''
