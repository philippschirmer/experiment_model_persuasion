# Run bots as an oTree-specific way of testing.

# Similar to "normal" tests written for general code, bots interact with the
# experiment, enter certain values into the formfields and click through pages.
# The PlayerBot in this file contains in a sense a large number of "small" tests,
# as it interacts with all pages of the experiment.
# For pages where the submission has to be restricted e.g. by requiring a
# number in an interval, the bot contains tests for whether such a submission
# "rightly" fails.

from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Introduction
        yield Demographics, dict(age=20, gender='Male', finance=50 )
        if self.player.id_in_group==1:
            yield PersuaderPage
            if self.player.bias() == 'biased':
                yield BiasedPage
                yield BiasedPage_Q, dict(item1A = 1, item2A= 30, item3A = "Increase")
            
            if self.player.bias() == 'aligned':
                yield AlignedPage 
                yield AlignedPage_Q, dict(item1B = 'The buyer receives a positive revenue since he/she could sell the stock and make a profit.',
                                            item2A= 30,
                                            item3A = 'Increase')
            yield DecisionPersuader1, dict(model_message_1 = 40)
            # Need to change syntax as model_message_2 and further are created
            # dynamically in a Javascript, not in the html.

            # Test whether model messages are enforced in valid range (0,...,T_trunc.)
            yield SubmissionMustFail(DecisionPersuader2, dict(model_message_2 = 120), check_html=False)
            yield SubmissionMustFail(DecisionPersuader2, dict(model_message_2 = -10), check_html=False)
            yield Submission(DecisionPersuader2, dict(model_message_2 = 40), check_html=False)

            yield SubmissionMustFail(DecisionPersuader3, dict(model_message_3 = -120), check_html=False)
            yield SubmissionMustFail(DecisionPersuader3, dict(model_message_3 = 120), check_html=False)
            yield Submission(DecisionPersuader3, dict(model_message_3 = 40), check_html=False)
            
            yield SubmissionMustFail(DecisionPersuader4, dict(model_message_3 = -120), check_html=False)
            yield SubmissionMustFail(DecisionPersuader4, dict(model_message_4 = 120), check_html=False)
            yield Submission(DecisionPersuader4, dict(model_message_4 = 40), check_html=False)

            yield SubmissionMustFail(DecisionPersuader5, dict(model_message_3 = -120), check_html=False)
            yield SubmissionMustFail(DecisionPersuader5, dict(model_message_5 = 120), check_html=False)
            yield Submission(DecisionPersuader5, dict(model_message_5 = 40), check_html=False)
        
        # Pages seen by a receiver player:
        if self.player.id_in_group>1:
            yield ReceiverPage
            yield ReceiverPage_Q
            yield DecisionReceiverNeutral1, dict(receiver_decision_neutral_1 = "Buy")
            yield DecisionReceiverNeutral2, dict(receiver_decision_neutral_2 = "Buy")
            yield DecisionReceiverNeutral3, dict(receiver_decision_neutral_3 = "Buy")
            yield DecisionReceiverNeutral4, dict(receiver_decision_neutral_4 = "Buy")
            yield DecisionReceiverNeutral5, dict(receiver_decision_neutral_5 = "Buy")
            yield EffortTask, dict(number_selected= 1)
            # skip the Wait page here, as bots handle these automatically.
            yield DecisionReceiver1, dict(receiver_decision_1="Buy")
            yield DecisionReceiver2, dict(receiver_decision_2="Sell")
            yield DecisionReceiver3, dict(receiver_decision_3="Buy")
            yield DecisionReceiver4, dict(receiver_decision_4="Sell")
            yield DecisionReceiver5, dict(receiver_decision_5="Buy")
        
        if self.player.id_in_group==1:
            yield ThoughtProcessPersuader, dict(item2C= 3, item3C= 3)
            # skip WaitForResults here, as bots handle these automatically.
            # yield Results