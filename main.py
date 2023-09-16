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

    game = Game(makeDeck()) # initialising a new game

    print("You are now playing a game of Blackjack")

    playerHand = game.createHand() # creating a hand for the player
    dealerHand = game.createHand()

    print(f"Your hand {', '.join(playerHand)}")
    
    playerScore = game.getHandValue(playerHand)
    dealerScore = game.getHandValue(dealerHand)

    # print(game.deck)

    if sum(playerScore) == 21 and sum(dealerScore) == 21:
        print("Push! Neither player wins!")

    elif sum(playerScore) == 21:
        print("Blackjack! You win!")
        
    elif sum(dealerScore) == 21:
        print("Blackjack! The Dealer wins!")

    
    else:
        # print(playerScore)

        keepGoing = True
        while keepGoing:
            playerScore = game.getHandValue(playerHand)
            dealerScore = game.getHandValue(dealerHand)
            if 11 in playerScore:
                while True:
                    print("You have an Ace in your hand. Would you like the Ace to be 1 or 11?")
                    aceOr11 = input("1/11 > ")

                    try:
                        aceOr11 = int(aceOr11)
                            
                        if aceOr11 == 1 or aceOr11 == 11:
                            playerScore[playerScore.index(11)] = aceOr11
                            break
                           
                        else:
                            print(invalid)
                    except ValueError:
                        print(invalid)

                # while True:

                #     print("You have an Ace in your hand. Would you like the Ace to be 11 or 1?")

                #     aceOr11 = input("1/11 > ")

                #     try:
                #         aceOr11 = int(aceOr11)


                #         if aceOr11 == 1:

                #             playerScore[playerScore.index(11)] = 1
                #             break
                
                #         elif aceOr11 == 11:
                #             break
                
                #         else:
                #             print(invalid)
                    
                #     except ValueError:
                #         print(invalid)
            
            print(f"Your hand value is {sum(playerScore)}")

            print("Would you like a hit? Y/N")

            hitOrNot = input("> ")

            while True:
                try:
                    hitOrNot = hitOrNot.upper()

                    if hitOrNot == "Y":
                        card = random.choice(game.deck)
                        game.deck.remove(card)
                        playerHand.append(card)

                        playerScore = game.getHandValue(playerHand)


                        game.playerHand = game.playerHand + 1
                        # print(game.playerHand)

                        if sum(playerScore) > 24 or sum(playerScore) == 21 or game.playerHand == 5:
                            break

                        break
                    
                    elif hitOrNot == "N":
                        break

                    else:
                        print(invalid + "...")
                        break
                
                except AttributeError:
                    print(invalid)
                    break
            
            if sum(playerScore) > 24 or game.playerHand == 5:
                break

    if sum(playerScore) == 21:
        print("21! You win!")

    elif sum(playerScore) <= sum(dealerScore) or sum(playerScore) > 24 or sum(dealerScore) == 21:
        print("You lose!")

        #     print(f"Your new hand is {', '.join(playerHand)} and the value is {playerScore}")
        # break
    
    elif sum(playerScore) >= sum(dealerScore) or sum(playerScore) == 21:
        print("You win!")

    print("Do you want to play again?")

    play = input("> ").lower()
