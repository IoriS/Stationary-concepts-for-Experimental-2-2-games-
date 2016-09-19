# coding:utf-8
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
Stationary concepts for 2x2-gamesのgame1の再現
"""


class Constants(BaseConstants):
    name_in_url = 'stationaryconcepts'
    players_per_group = 2
    num_rounds = 20

    player1_A_A_payoff = c(10)
    player1_A_B_payoff = c(0)
    player1_B_A_payoff = c(9)
    player1_B_B_payoff = c(10)

    player2_A_A_payoff = c(8)
    player2_B_A_payoff = c(9)
    player2_A_B_payoff = c(18)
    player2_B_B_payoff = c(8)


class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.group_randomly(fixed_id_in_group=True)



class Group(BaseGroup):
    def set_payoffs(self):
        player1 = self.get_player_by_role('player1')
        player2 = self.get_player_by_role('player2')


        if player1.decision == 'A' and player2.decision == 'A':
            player1.payoff = Constants.player1_A_A_payoff
            player2.payoff = Constants.player2_A_A_payoff

        elif player1.decision == 'B' and player2.decision == 'A':
            player1.payoff = Constants.player1_B_A_payoff
            player2.payoff = Constants.player2_B_A_payoff

        elif player1.decision == 'A' and player2.decision == 'B':
            player1.payoff = Constants.player1_A_B_payoff
            player2.payoff = Constants.player2_A_B_payoff

        elif player1.decision == 'B' and player2.decision == 'B':
            player1.payoff = Constants.player1_B_B_payoff
            player2.payoff = Constants.player2_B_B_payoff

        for player in self.get_players():
            self.cumulative_1_payoff = sum([p.payoff for p in player1.in_all_rounds()])
            self.cumulative_2_payoff = sum([p.payoff for p in player2.in_all_rounds()])


class Player(BasePlayer):
    decision = models.CharField(
        choices=['A', 'B'],
        doc="""このプレーヤーの行動""",
        widget=widgets.RadioSelect()
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def role(self):
        if (self.id_in_group)%2 == 0:
            return 'player1'
        if (self.id_in_group)%2 == 1:
            return 'player2'

