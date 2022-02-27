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
    model_message_2 = models.IntegerField()
    model_message_3 = models.IntegerField()
    model_message_4 = models.IntegerField()
    model_message_5 = models.IntegerField()

    message_received_1 = models.IntegerField()
    message_received_2 = models.IntegerField()
    message_received_3 = models.IntegerField()
    message_received_4 = models.IntegerField()
    message_received_5 = models.IntegerField()


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
    model_message_test_1 = player_receiver.model_message_1
    model_message_test_2 = player_receiver.model_message_2
    model_message_test_3 = player_receiver.model_message_3
    model_message_test_4 = player_receiver.model_message_4
    model_message_test_5 = player_receiver.model_message_5
    for player in players:
        player.message_received_1 = model_message_test_1
        player.message_received_2 = model_message_test_2
        player.message_received_3 = model_message_test_3
        player.message_received_4 = model_message_test_4
        player.message_received_5 = model_message_test_5


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
class DecisionPersuader1(Page):
    template_name = "persuasion/DecisionPersuader.html"
    form_model = 'player'
    form_fields = ['model_message_1']
    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'
    # def var_for_template(player):
    #     graph_number = 1
    #     model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
    #     # Incomplete model path, to be extended with chosen model message (slider in html/JS)
    def vars_for_template(player):
        graph_number = 1
        init_model = "/static/persuasion/model_graph_trunc_{}_0.jpg".format(graph_number)
        return{
            'init_model': init_model
        }

    @staticmethod
    def js_vars(player):
        graph_number = 1
        #model_path_init = "/static/persuasion/model_graph_trunc_{}_0".format(graph_number)
        model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
        slider_name = "model_message_{}".format(graph_number)
        return dict(
            model_path_incomplete = model_path_incomplete,
            slider_name = slider_name
        )

class DecisionPersuader2(Page):
    template_name = "persuasion/DecisionPersuader.html"
    form_model = 'player'
    form_fields = ['model_message_2']
    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'
    # def var_for_template(player):
    #     graph_number = 2
    #     model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
    #     # Incomplete model path, to be extended with chosen model message (slider in html/JS)
    def vars_for_template(player):
        graph_number = 2
        init_model = "/static/persuasion/model_graph_trunc_{}_0.jpg".format(graph_number)
        return{
            'init_model': init_model
        }

    @staticmethod
    def js_vars(player):
        graph_number = 2
        model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
        slider_name = "model_message_{}".format(graph_number)
        return dict(
            model_path_incomplete = model_path_incomplete,
            slider_name = slider_name
        )

class DecisionPersuader3(Page):
    template_name = "persuasion/DecisionPersuader.html"
    form_model = 'player'
    form_fields = ['model_message_3']
    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'
    # def var_for_template(player):
    #     graph_number = 2
    #     model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
    #     # Incomplete model path, to be extended with chosen model message (slider in html/JS)
    def vars_for_template(player):
        graph_number = 3
        init_model = "/static/persuasion/model_graph_trunc_{}_0.jpg".format(graph_number)
        return{
            'init_model': init_model
        }
    @staticmethod
    def js_vars(player):
        graph_number = 3
        model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
        slider_name = "model_message_{}".format(graph_number)
        return dict(
            model_path_incomplete = model_path_incomplete,
            slider_name = slider_name
        )

class DecisionPersuader4(Page):
    template_name = "persuasion/DecisionPersuader.html"
    form_model = 'player'
    form_fields = ['model_message_4']
    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'
    # def var_for_template(player):
    #     graph_number = 2
    #     model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
    #     # Incomplete model path, to be extended with chosen model message (slider in html/JS)
    def vars_for_template(player):
        graph_number = 4
        init_model = "/static/persuasion/model_graph_trunc_{}_0.jpg".format(graph_number)
        return{
            'init_model': init_model
        }
    @staticmethod
    def js_vars(player):
        graph_number = 4
        model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
        slider_name = "model_message_{}".format(graph_number)
        return dict(
            model_path_incomplete = model_path_incomplete,
            slider_name = slider_name
        )

class DecisionPersuader5(Page):
    template_name = "persuasion/DecisionPersuader.html"
    form_model = 'player'
    form_fields = ['model_message_5']
    @staticmethod
    def is_displayed(player):
        return player.role() == 'persuader'
    # def var_for_template(player):
    #     graph_number = 2
    #     model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
    #     # Incomplete model path, to be extended with chosen model message (slider in html/JS)
    def vars_for_template(player):
        graph_number = 5
        init_model = "/static/persuasion/model_graph_trunc_{}_0.jpg".format(graph_number)
        return{
            'init_model': init_model
        }

    @staticmethod
    def js_vars(player):
        graph_number = 5
        model_path_incomplete = "/static/persuasion/model_graph_trunc_{}_".format(graph_number)
        slider_name = "model_message_{}".format(graph_number)
        return dict(
            model_path_incomplete = model_path_incomplete,
            slider_name = slider_name
        )
"""
Landing page if participant is randomly selected as aligned persuader.
"""
class AlignedPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.bias() == 'aligned'

"""
Pages to keep receiver busy while persuader makes chart choiced.
"""
class DecisionReceiverNeutral1(Page):
    template_name = 'persuasion/ReceiverBusy.html'
    form_model = 'player'
    form_fields = ['receiver_decision_1']

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

    def vars_for_template(player):
        graph_number = 1
        model_path = "/static/persuasion/neutral_graph_trunc_{}.jpg".format(graph_number)

        return{
            'model_path':model_path
        }

class DecisionReceiverNeutral2(Page):
    template_name = 'persuasion/ReceiverBusy.html'
    form_model = 'player'
    form_fields = ['receiver_decision_1']

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

    def vars_for_template(player):
        graph_number = 2
        model_path = "/static/persuasion/neutral_graph_trunc_{}.jpg".format(graph_number)

        return{
            'model_path':model_path
        }

class DecisionReceiverNeutral3(Page):
    template_name = 'persuasion/ReceiverBusy.html'
    form_model = 'player'
    form_fields = ['receiver_decision_1']

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

    def vars_for_template(player):
        graph_number = 3
        model_path = "/static/persuasion/neutral_graph_trunc_{}.jpg".format(graph_number)

        return{
            'model_path':model_path
        }

class DecisionReceiverNeutral4(Page):
    template_name = 'persuasion/ReceiverBusy.html'
    form_model = 'player'
    form_fields = ['receiver_decision_1']

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

    def vars_for_template(player):
        graph_number = 4
        model_path = "/static/persuasion/neutral_graph_trunc_{}.jpg".format(graph_number)

        return{
            'model_path':model_path
        }

class DecisionReceiverNeutral5(Page):
    template_name = 'persuasion/ReceiverBusy.html'
    form_model = 'player'
    form_fields = ['receiver_decision_1']

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

    def vars_for_template(player):
        graph_number = 5
        model_path = "/static/persuasion/neutral_graph_trunc_{}.jpg".format(graph_number)

        return{
            'model_path':model_path
        }

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

class DecisionReceiver1(Page):
    #page_number = 1 (for figure recognition later)
    template_name = 'persuasion/DecisionReceiver.html'
    form_model = 'player'
    form_fields = ['receiver_decision_1']


    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'


    def vars_for_template(player):
        #graph_number = 1
        # Just using age right now, to check whether it works in general
        # TODO: Have received model message depend on OTHER player.
        # model_path = "static " + "persuasion/fig_test_{}.jpg".format(player.age)
        # model_path = "static " + "persuasion/fig_test_10.jpg"
        model_path = "/static/persuasion/model_graph_trunc_1_{}.jpg".format(player.message_received_1)
        return{
            'model_path':model_path
        }

class DecisionReceiver2(Page):
    #page_number = 2 (for figure recognition later)
    template_name = 'persuasion/DecisionReceiver.html'
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
        model_path = "/static/persuasion/model_graph_trunc_2_{}.jpg".format(player.message_received_2)

        return{
            'model_path':model_path
        }

class DecisionReceiver3(Page):
    #page_number = 2 (for figure recognition later)
    template_name = 'persuasion/DecisionReceiver.html'
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

class DecisionReceiver4(Page):
    #page_number = 2 (for figure recognition later)
    template_name = 'persuasion/DecisionReceiver.html'
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

class DecisionReceiver5(Page):
    #page_number = 2 (for figure recognition later)
    template_name = 'persuasion/DecisionReceiver.html'
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
                DecisionPersuader1,
                DecisionPersuader2,
                DecisionPersuader3,
                DecisionPersuader4,
                DecisionPersuader5, 
                ReceiverPage,
                ReceiverPage_Q,
                DecisionReceiverNeutral1, 
                DecisionReceiverNeutral2,
                DecisionReceiverNeutral3,
                DecisionReceiverNeutral4,
                DecisionReceiverNeutral5,
                EffortTask,
                Wait,
                DecisionReceiver1,
                DecisionReceiver2,
                DecisionReceiver3,
                DecisionReceiver4,
                DecisionReceiver5,
                Wait,
                ThoughtProcessPersuader,
                ] 