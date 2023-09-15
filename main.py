#!/usr/bin/env python3

"""
    Written by Smoodeazy Sept 15 2023
    Feel free to edit the code to your liking

"""
####### IMPORTING

from config import *
from card import *

play = ""


# game = Game()
# print(game.deck)
while play.lower() != "no":
    
    game = Game() # initialising a new game

    print("You are now playing a game of Blackjack")

    playerHand = game.createHand() # creating a hand for the player
    dealerHand = game.createHand()
    
    dealerScore = sum(game.getHandValue(dealerHand))
    playerScore = sum(game.getHandValue(playerHand))

    if playerScore == 21 and dealerScore == 21:
        print("Push! Neither player wins!")
    
    break