#!/usr/bin/env python3

#### IMPORTING

from config import *
import random


class Game():

    def __init__(self):

        self.player = 0
        self.dealer = 0
        self.deck = []

        for i in cardSym:
            for j in values:
                self.deck.append(f"{j} of {i}")

    def hit(self, q, amount):

        if q == "dealer":
            self.dealer = self.dealer + amount
        
        else:
            self.player = self.player + amount
    
    def addCard(self):
        card = random.choice(self.deck)
        self.deck.remove(card)

        return card
    
    def createHand(self):
        hand = []
        for i in range(2):
            card = self.addCard() # Creating a hand and removing the card being used from the original list
            hand.append(card)
        
        return hand
    
    def getHandValue(self, hand):
        output = []
        for j in hand: # Go through the hand
            first = j.split()[0] # Split the string, an input such as "King of Spades" will be split into a list ["King", "Of", "Spades"]
            # By getting the first element of the list, we find out the value of the card
            if first in faceCards and first != "Ace":
                output.append(10)
                
            elif first == "Ace":
                output.append(11)
                
            else:
                output.append(first)
        
        return output

        

