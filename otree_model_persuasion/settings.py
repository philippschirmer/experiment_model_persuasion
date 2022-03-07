from os import environ


SESSION_CONFIGS = [
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        app_sequence=['guess_two_thirds', 'payment_info'],
        num_demo_participants=3,
    ),
    dict(
        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='first_test_survey',
        num_demo_participants=3,
        app_sequence=['first_test_survey']
    ),
    dict(
        name='persuasion',
        # Game should be able to support any number of players >=2.
        # If changing the number of demo_participants, ensure that PLAYERS_PER_GROUP
        # as defined  in the __init__.py is a divisor.
        num_demo_participants=4,
        app_sequence=['persuasion'],
        # Set use_browser_bots to True to automatically test the app
        # with bots from "tests.py"
        use_browser_bots=True
    ),
    dict(
        name='sandbox',
        display_name='Sandbox A first attempt at a receiver game',
        num_demo_participants=3,
        app_sequence=['sandbox']
    )

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '7941745652380'

INSTALLED_APPS = ['otree']
