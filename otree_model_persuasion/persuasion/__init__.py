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
    #model_message_1 = models.IntegerField()

    # def set_model_message_received(group):
    #     players = group.get_players()
    #     model_message_test = [p.model_message_1 for p in players]
    #     for player in players:
    #         player.message_received = model_message_test[0]

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
    number_selected = models.IntegerField(
        label = 'Your answer'
    )
    item1E = models.IntegerField()
    item2E = models.IntegerField()
    item3E = models.IntegerField()
    item4E = models.IntegerField()
    item5E = models.IntegerField()

    model_message_1 = models.IntegerField()
    message_received = models.IntegerField()

    receiver_decision_1 = models.StringField(
    choices=[
            ['Buy', 'Buy'], 
            ['Sell', 'Sell']            
    ],
    label='Would you like to buy, or sell the stock?',
    widget=widgets.RadioSelect,
    blank=True # FOR TESTING...quitar despues 
    )


#def creating_session(subsession):
#    for player in subsession.get_players():
#        if player.role == C.PERSUADER_ROLE:
#            player.biased = True           #random.choice([True, False])
#    else:
#        pass 



# FUNCTIONS

# Update players' (receivers) received model message.
# Function gets called after the effort task, before the second set of receiver decisions.
def set_model_message_received(group):
    players = group.get_players()
    player_receiver = players[0]
    model_message_test = player_receiver.model_message_1
    for player in players:
        player.message_received = model_message_test


# Calculate the players' payoffs at the end of the game.
def set_payoffs(group):
    players = group.get_players()

    # Define when a buy/sell are the ex post "right" decision.

    # Persuaders gets payoffs depending on role (biased or aligned),
    # and decisions of receivers
    player_receiver = players[0]

    # Persuaders get payoff if their predictions are correct.
    #

    for player in players:
        player.payoff = C.ENDOWMENT + 5

    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    for player in players:
        player.payoff = C.ENDOWMENT - player.contribution + group.individual_share


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
    """
    def error_message(player, values):
        if values['item1B'] != 'The buyer receives a positive revenue since he/she could sell the stock and make a profit.':
            return 'Incorrect answer for Question 1. Please try again.'
        if values['item2A'] != 30: ### check which value will apply after selecting final image
            return 'Incorrect answer for Question 2. Please try again.'
        if values['item3A'] != 'Increase':
            return 'Incorrect answer for Question 3. Please try again.'"""

    @staticmethod
    def is_displayed(player):
        return player.bias() == 'aligned'

"""
Page for decision making for the persuader (does it matter if he/she is aligned or biased?)

"""
class DecisionPersuader(Page):
    form_model = 'player'
    form_fields = ['model_message_1']
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
    template_name = 'persuasion/Wait.html'
    title_text = "Please Wait"
    body_text = "Please wait until the other participants have make their choices!"

    after_all_players_arrive = set_model_message_received

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

    """    def error_message(player, values):
        if values['item1C'] != 'All the above':
            return 'Incorrect answer for Question 1. Please try again.'
        if values['item2A'] != 30: ### check which value will apply after selecting final image
            return 'Incorrect answer for Question 2. Please try again.'
        if values['item3A'] != 'Increase':
            return 'Incorrect answer for Question 3. Please try again.'"""

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

class DecisionReceiver(Page):
    form_model = 'player'
    form_fields = ['receiver_decision_1']


    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'


    def vars_for_template(player):
        # Just using age right now, to check whether it works in general
        # TODO: Have received model message depend on OTHER player.
        # model_path = "static " + "persuasion/fig_test_{}.jpg".format(player.age)
        # model_path = "static " + "persuasion/fig_test_10.jpg"
        model_path = "/static/persuasion/fig_test_{}.jpg".format(player.message_received)

        return{
            'model_path':model_path
        }

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
        rand_numbers_1=dict()
        N_1 = range(1,11)
        for i in list(N_1):
            number_i = random.randint(1,100)
            rand_numbers_1['number_'+ str(i)] = number_i
        return rand_numbers_1

    def correct_answer(player):
        values = player.rand_numbers_1.values
        return values 

    # def vars_for_template(player):
    #     rand_numbers_2=dict()
    #     N = range(11,21)
    #     for i in list(N):
    #         number_i = random.randint(1,100)
    #         rand_numbers_2['number_'+ str(i)] = number_i
    #     return rand_numbers_2

    #def error_message(player, values):
    #    if player.sum_random_numbers != values['number_selected']:
    #        return 'Wrong answer, please try again.'

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