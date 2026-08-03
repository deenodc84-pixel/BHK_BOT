import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Bot settings
COMMANDS = [
    ('start', 'Start the bot'),
    ('help', 'Show all commands'),
    ('stats', 'Get player statistics'),
    ('champions', 'NBA champions by year'),
    ('teams', 'Show all NBA teams'),
    ('schedule', 'Next week game schedule'),
    ('trivia', 'Random basketball trivia'),
    ('facts', 'Random basketball facts'),
    ('records', 'NBA all-time records'),
    ('about', 'About this bot')
]
