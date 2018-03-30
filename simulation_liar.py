import numpy as np
from numpy import random as rand
from random import randint



# game state class
	# global dice, and which player has what
	# players turn
	# current bid



class GameState:
	def __init__(self, num_players):
		self.dice_per_player = 5

		self.num_players = num_players

		self.num_dice = self.dice_per_player * self.num_players

		self.player_hands = []

		# the current bid is a tuple of quantity and face value
		# i.E. initial bid is that there is at least one dice with 
		# face value 2
		self.current_bid = (1,2)

	def get_current_bid(self):
		return self.current_bid

	def get_all_player_hands(self):
		return self.player_hands

	def get_player_hand(self, player_id):
		return self.player_hands[player_id]



# utilities for running the actual rounds of the game
# inherits the gamestate class, as that is what it manipulates
class RunGame(GameState):
	# initial distribution (roll the dies)
	def __init__(self, game_state):
		# how many turns has it been
		self.num_turn = 0

	def initial_roll(self):
		all_rolls =[]
		for i in range(self.num_players * self.num_dice):
			roll = randint(1, 6)
			all_rolls.append(roll)
		#random.shuffle(all_rolls)
		size = self.dice_per_player
		# splits the rolls to different players
		self.player_hands = [all_rolls[i:i + size] for i  in range(0, len(all_rolls), size)]
		return

	def call_bluff(self, bet):
		# cnt is number of actual occurences of the face value
		# bet(0) is the number of occurrences in the current bet
		cnt = self.player_hands.count(bet(1))
		if cnt >= bet(0):
			return False
		else:
			return True

	def new_bet(self):
		return


	# simulates another round, says whether or not the game is won
	# takes the id of the current player's turn,
	# either the next bet or whether the player challenges the previous bet
	def next_player_turn(self, player_id, raise=None, call=False):
		
		if call == True:
			self.call_bluff(bet)

		return


class Player:
	# want to know which player it is, ids are just ints
	def __init__(self, player_id):
		self.player_id = player_id
		self.player_hand = None


	def update_my_hand(self, ):
		return


	def get_total_dice_left(self):
		return


	def get_current_bet(self):
		return


	def calculate_prob(self):
		return


	def make_new_bid(self):
		return


	def call_bluff(self):
		return



# player turn --> calculate probabilities for that player's bid
	# total number of dice 
	# their current dice


