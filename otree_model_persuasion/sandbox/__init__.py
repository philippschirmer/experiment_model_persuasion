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
        # player.std_layout= 5
        # testing things related to slider here.

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
    std_layout = models.IntegerField()
    price = models.FloatField()
    number = models.IntegerField()
    slider_one = models.IntegerField(initial=None, blank=False, max=100, min=-100)
    placeholder =models.IntegerField(initial=1)

    # Persuader's model choice / message
    model_message_1 = models.FloatField(initial=None, blank=False, max=100, min=-100)
    # models.FloatField(
    # widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
    # min=0,
    # initial=0,
    # max=80,
    # )
    # Model Message Test (TODO)
    # check_model_message = models.FloatField(blank=True, initial=None)


# PAGES

class Intro_Page(Page):
    pass

class Information_Receiver(Page):
    pass

class Treatment_Info_Incentives(Page):
    @staticmethod
    def is_displayed(player):
        return player.info_incentives == True


class Java_Test_1(Page):
    pass

class Java_Test_2(Page):
    pass

class Plotly_Test(Page):
    pass

class MyPage(Page):
    pass


class Investment_Decision(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class ImageAnnotating(Page):
    pass

class Plotly_Slider_Test(Page):
    pass
    # Test: Can we send e.g. the starting layout to JS/Plotly?
    # @staticmethod
    # def js_vars(player):
    # return dict(
    #    std_layout=player.std_layout,
    #)


class Plotly_Simple_Slider_Test(Page):
    pass



class SliderPage(Page):
    form_model = 'player'
    form_fields = ['price', 'number']

class Slider_Test2(Page):
    form_model = 'player'
    form_fields = ['placeholder']

    @staticmethod
    def vars_for_template(player):
        return dict(
            image_path='sandbox/Rplot_1_{}.png'.format(player.placeholder)
        )




page_sequence= [Intro_Page, Slider_Test2, SliderPage, Plotly_Simple_Slider_Test, Plotly_Slider_Test, Plotly_Test, Java_Test_2, Java_Test_1]