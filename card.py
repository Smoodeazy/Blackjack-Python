#!/usr/bin/env python3

#### IMPORTING

from config import *
import random


def makeDeck():
    deck = []
    for i in cardSym:
        for j in values:
            deck.append(f"{j} of {i}")
    
    return deck

class Game():

    def __init__(self, deck):

        self.player = 0
        self.playerHand = 2
        self.dealerHand = 2
        self.dealer = 0
        self.deck = deck


    def hit(self, q, amount):

        if q == "dealer":
            self.dealer = self.dealer + amount
        
        else:
            self.player = self.player + amount

    def addCard(self):
        print(self.deck)
        card = random.choice(self.deck)
        self.deck.remove(card)

        return f"{card}"

    def createHand(self):
        hand = []
        for i in range(2):
            card = random.choice(self.deck) # Creating a hand and removing the card being used from the original list
            self.deck.remove(card)
            hand.append(card)
        
        return hand
    
    # def createHand(self):
    #     hand = []
    #     for i in range(2):
    #         if self.deck:
    #             card = random.choice(self.deck)  # Draw a card from the deck
    #             self.deck.remove(card)
    #             hand.append(card)
    #         else:
    #             print("The deck is empty.")
    #             break  # Stop drawing if the deck is empty
    #     return hand 

    def getHandValue(self, hand):
        output = []
        for j in hand: # Go through the hand
            first = j.split()[0] # Split the string, an input such as "King of Spades" will be split into a list ["King", "Of", "Spades"]
            # By getting the first element of the list, we find out the value of the card
            if first in faceCards and first != "Ace":
                output.append(10)
                
            elif first == "Ace":
                output.append(11) ## Return 11 if its an ace, this will be used later...
                
            else:
                output.append(int(first))

        # print(output)
        return output
