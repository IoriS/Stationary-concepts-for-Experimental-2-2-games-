# coding:utf-8
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decide(Page):
    form_model = models.Player
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
    body_text = "通信待機中・・・"


class Results(Page):

    def vars_for_template(self):
        self.group.set_payoffs()
        return {'cumulative_1_payoff':self.group.cumulative_1_payoff,
                'cumulative_2_payoff':self.group.cumulative_2_payoff,
                'player_in_all_rounds':self.player.in_all_rounds(),
        }



page_sequence = [
    Decide,
    ResultsWaitPage,
    Results
]
