from otree.api import *


doc = """
Your app description
"""

## Functions

def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.info_incentives = random.choice([True, False])
        print('Receiver is informed about persuader`s incentives ', player.info_incentives)


class C(BaseConstants):
    NAME_IN_URL = 'my_first_receiver_exp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()
    graph_number = models.IntegerField()
    info_incentives = models.BooleanField()


# PAGES

class Treatment_Info_Incentives(Page):
    @staticmethod
    def is_displayed(player):
        return player.info_incentives == True


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, Treatment_Info_Incentives, Results]
