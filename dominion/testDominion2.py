# -*- coding: utf-8 -*-
"""
Created on 1/15/2020

@author: Jia Yi Li
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Input player names
player_names = ["Annie","*Ben","*Carla"]

#get number of victory and curses cards
nV, nC = testUtility.get_nV_nC(player_names)

#Define box
box = testUtility.get_box(nV)

supply_order = testUtility.get_supply_order()

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:20]
supply = defaultdict(list,[(k,box[k]) for k in random10])

#The supply always has these cards
supply = testUtility.get_supply(supply, nV, nC, player_names)

#Costruct the Player objects
players = testUtility.get_players(player_names)

#initialize the trash
trash = []

#initialize turn number
turn  = 0

#Play the game
testUtility.play_game(trash, turn, supply, supply_order, players)

#Announce Final score and Winners
testUtility.get_final_score(players)
