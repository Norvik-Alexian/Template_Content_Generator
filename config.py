import re

KEYWORDS = ['Ucraft', 'drag and drop website builder', 'ecommerce', 'company']
ENDING_PUNCTUATIONS = ['.', '!']
TEMPERATURE = 0.7
MAX_TOKENS = 80
TOP_P = 1.
FREQUENCY_PENALTY = 1.
PRESENCE_PENALTY = 1.
SPACE_REMOVER_PATTERN = re.compile(r'\s+')
