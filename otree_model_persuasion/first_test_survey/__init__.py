from otree.api import *


doc = """
Your app description
"""




class C(BaseConstants):
    NAME_IN_URL = 'first_test_survey'
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

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'graph_number']


class ResultsWaitPage(WaitPage):
    pass


class PicturePage(Page):

    @staticmethod
    def vars_for_template(player):
        return dict(
        image_path='first_test_survey/Rplot_1_{}.png'.format(player.graph_number),
        #image_path='first_test_survey/Rplot_1_5.png',
        a=15
        )


class Results(Page):
    pass


page_sequence = [MyPage, PicturePage, Results]
