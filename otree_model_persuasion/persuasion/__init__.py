from otree.api import *
import random

class C(BaseConstants): #do not vary from player to player
    NAME_IN_URL = 'persuasion'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    AGE_MIN = cu(18)
    AGE_MAX = cu(80)
    #PERSUADER_ROLE = 'persuader'
    #RECEIVER_ROLE = 'receiver'
    INSTRUCTIONS_TEMPLATE = 'persuasion/instructions.html' #general instructions

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=C.AGE_MIN, max=C.AGE_MAX)
    gender = models.StringField(
        choices=[
                ['Male', 'Male'], 
                ['Female', 'Female'],
                ['Other', 'Other']                
        ],
        label='What is your gender?',
        widget=widgets.RadioSelect,
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

#def creating_session(subsession):
#    for player in subsession.get_players():
#        if player.role == C.PERSUADER_ROLE:
#            player.biased = True           #random.choice([True, False])
#    else:
#        pass 

# PAGES
class Introduction(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']

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

class BiasedPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.bias() == 'biased'

class AlignedPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.bias() == 'aligned'

class ReceiverBusy(Page):

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

class Wait(WaitPage):
    pass

class ReceiverPage(Page):

    @staticmethod
    def is_displayed(player):
        return player.role() == 'receiver'

page_sequence = [Introduction, 
                Demographics, 
                PersuaderPage, 
                BiasedPage, 
                AlignedPage, 
                ReceiverBusy, 
                Wait, 
                ReceiverPage]