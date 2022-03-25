import re

KEYWORDS = ['Ucraft', 'drag and drop website builder', 'ecommerce', 'company']
ENDING_PUNCTUATIONS = ['.', '...', '!']
TEMPERATURE = [0.6, 1.]
MAX_TOKENS = [15, 600]
TOP_P = 1.
FREQUENCY_PENALTY = [0.2, 0.3, 1.5]
PRESENCE_PENALTY = [0., 0.1]
space_remover = re.compile(r'\s+')
