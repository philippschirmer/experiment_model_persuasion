from numpy import number
from otree.api import *
import random

author = 'Carolina Alvarez and Philipp Schirmer'

doc = """
Demo of o-Tree Persuasion game
"""

"""
Constant values for game.
"""
class C(BaseConstants): #do not vary from player to player
    NAME_IN_URL = 'persuasion'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    #AGE_MIN = cu(18)
    #AGE_MAX = cu(80)
    #PERSUADER_ROLE = 'persuader'
    #RECEIVER_ROLE = 'receiver'
    INSTRUCTIONS_TEMPLATE = 'persuasion/instructions.html' #general instructions
    BinaryChoices=[
    [1, 'True'],
    [2, 'False']
    ]
    CathegoricalChoices= [
        [1, 'I strongly disagree'],
        [2, 'I moderately disagree'],
        [3, 'I neither agree nor disagree'],
        [4, 'I moderately agree'],
        [5, 'I strongly agree'],
    ]
    

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.IntegerField(
        label='What is your age?',
        blank=True
    ) 
    gender = models.StringField(
        choices=[
                ['Male', 'Male'], 
                ['Female', 'Female'],
                ['Other', 'Other']                
        ],
        label='What is your gender?',
        widget=widgets.RadioSelect,
        blank=True # FOR TESTING...quitar despues 
    )
    finance = models.IntegerField(
        label="Please rate your previous financial knowledge on a percentage scale between 0 and 100.",
        #min=0,
        #max=100,
        blank=True,
        initial=None
    )
    treatment = models.BooleanField(initial=False)
    def role(player):
        if player.id_in_group == 1:
            return 'persuader'
        else:
            return 'receiver'
    def bias(player):
        if player.id_in_group == 1:
            if player.treatment == True:
                return  'biased'
            else:
                return 'aligned'

    # Comprehension questions for biased 
    item1A = models.IntegerField(
        label = '1. If the receiver buys the stock, do you expect to win an extra payoff?',
        choices = C.BinaryChoices,
        blank=True
    )
    item2A = models.IntegerField(
        label = '',
        choices = [
        '10', 
        '20',
        '30'                
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    item3A = models.StringField(
        label='',
        choices = [
        'Increase', 
        'Decrease', 
        'Remain the same'],
        widget=widgets.RadioSelect,
        blank=True
    )
    #comprehension questions for aligned
    item1B = models.StringField(
        label = '1. What happens if someone buys the stock at the current price and later on the price increases?',
        choices = [
        'The buyer will be worse off and could not make any profit from the transaction.',
        'The buyer receives a positive revenue since he/she could sell the stock and make a profit.',
        'The buyer will be indiferent.'
        ],
        widget = widgets.RadioSelect,
        blank=True
    )
    #comprehension questions for receiver
    item1C = models.StringField(
        label = '1. In which situation will you gain profit from your financial transaction?',
        choices = [
        'If you buy the stock now and sell it later at a higher price.',
        'If you sell the stock now and buy it later at a lower price',
        'All the above'
        ],
        widget = widgets.RadioSelect,
        blank=True
    )
    item1D = models.IntegerField(
        label = 'It was easy to understand the general purpose of the game',
        widget=widgets.RadioSelect,
        choices=C.CathegoricalChoices
    )
    item2D = models.IntegerField(
        label = 'I did not have troubles understand the selection of regression models',
        widget=widgets.RadioSelect,
        choices=C.CathegoricalChoices
    )
    number_selected = models.IntegerField()
    sum_random_numbers = models.IntegerField()
#def creating_session(subsession):
#    for player in subsession.get_players():
#        if player.role == C.PERSUADER_ROLE:
#            player.biased = True           #random.choice([True, False])
#    else:
#        pass 

# PAGES

"""
Introduction page where general instructions are displayed.
"""
class Introduction(Page):
    pass

"""
General survey page to collect demographic data.
"""
class Demographics(Page):
    form_model = 'player'
    form_fields = [
    'age', 
    'gender', 
    'finance'
    ]

    def error_message(player, values):
        if values['age'] < 18:
            return 'You have to be above 18 to participate in the current experiment.'

    def error_message(player, values):
        if values['finance'] > 100:
            return 'Please select a value between the range 0 and 100'
    def error_message(player, values): #check later
        while True: # Infinite loop
            try:
                values['age'] = int() # Try to convert the input into a number
                break                # Break out of the infinite loop if the conversion is successful
            except ValueError:       # Do this instead if the try block causes a ValueError
                print("Sorry, that is not an integer. Please try again.")

"""
Landing page if participant is randomly selected as persuader.
"""
class PersuaderPage(Page):

    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'

    @staticmethod
    def vars_for_template(player):
        return dict(
        image_path='first_test_survey/Rplot_1_{}.png',
        #image_path='first_test_survey/Rplot_1_5.png',
        a=15
        )

"""
Landing page if participant is randomly selected as biased persuader.
"""
class BiasedPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.bias() == 'biased'

"""
Comprehension questions for biased persuader.
"""

class BiasedPage_Q(Page):
    form_model = 'player'
    form_fields = [
    'item1A', 
    'item2A', 
    'item3A'
    ]

    def error_message(player, values):
        if values['item1A'] == 2:
            return 'Incorrect answer for Question 1. Please try again.'
        if values['item2A'] != 30: ### check which value will apply after selecting final image
            return 'Incorrect answer for Question 2. Please try again.'
        if values['item3A'] != 'Increase':
            return 'Incorrect answer for Question 3. Please try again.'

    @staticmethod
    def is_displayed(player):
        return player.bias() == 'biased'

class AlignedPage_Q(Page):
    form_model = 'player'
    form_fields = [
    'item1B', 
    'item2A', 
    'item3A'
    ]

    def error_message(player, values):
        if values['item1B'] != 'The buyer receives a positive revenue since he/she could sell the stock and make a profit.':
            return 'Incorrect answer for Question 1. Please try again.'
        if values['item2A'] != 30: ### check which value will apply after selecting final image
            return 'Incorrect answer for Question 2. Please try again.'
        if values['item3A'] != 'Increase':
            return 'Incorrect answer for Question 3. Please try again.'

    @staticmethod
    def is_displayed(player):
        return player.bias() == 'aligned'

"""
Page for decision making for the persuader (does it matter if he/she is aligned or biased?)

"""
class DecisionPersuader(Page):
    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'
"""
Landing page if participant is randomly selected as aligned persuader.
"""
class AlignedPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.bias() == 'aligned'

"""
Page to keep receiver busy while persuader makes chart choiced.
"""
class ReceiverBusy(Page):
    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

"""
Wait page.
"""
class Wait(WaitPage):
    pass

"""
Landing page if participant is randomly selected as receiver.
"""
class ReceiverPage(Page):

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

class ReceiverPage_Q(Page):
    form_model = 'player'
    form_fields = [
    'item1C', 
    'item2A', 
    'item3A'
    ]

    def error_message(player, values):
        if values['item1C'] != 'All the above':
            return 'Incorrect answer for Question 1. Please try again.'
        if values['item2A'] != 30: ### check which value will apply after selecting final image
            return 'Incorrect answer for Question 2. Please try again.'
        if values['item3A'] != 'Increase':
            return 'Incorrect answer for Question 3. Please try again.'
    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

class DecisionReceiver(Page):
    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'


class ThoughtProcessPersuader(Page):
    form_model = 'player'
    form_fields = [
    'item1D',
    'item2D'
    ]
    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'

class EffortTask(Page):
    form_model = 'player'
    form_fields = ['number_selected']

    def vars_for_template(player):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)

        player.sum_random_numbers = number_1 + number_2

        return{
            'number_1':number_1,
            'number_2':number_2,
        }
    
    
    #def error_message(player, values) error message for wrong sum
    def error_message(player, values):
        if player.sum_random_numbers != values['number_selected']:
            return 'Wrong answer, please try again.'

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

page_sequence = [Introduction, 
                Demographics, 
                PersuaderPage, 
                BiasedPage, 
                BiasedPage_Q,
                AlignedPage,
                AlignedPage_Q,
                DecisionPersuader, 
                ReceiverPage,
                ReceiverPage_Q,
                ReceiverBusy, 
                EffortTask,
                Wait,
                DecisionReceiver,
                Wait,
                ThoughtProcessPersuader,
                ] 