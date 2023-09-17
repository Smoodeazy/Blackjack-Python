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

    print("\nYou are now playing a new game of Blackjack")

    playerHand = game.createHand() # creating a hand for the player
    dealerHand = game.createHand()

    playerScore = game.getHandValue(playerHand)
    dealerScore = game.getHandValue(dealerHand)

    if ("11A" in playerScore and 10 in playerScore) and ("11A" in dealerScore and 10 in dealerScore):
        playerScore[playerScore.index("11A")] = 11
        dealerScore[dealerScore.index("11A")] = 11
        
        print("Push! Neither player wins!")

    elif ("11A" in playerScore and 10 in playerScore) == 21:
        playerScore[playerScore.index("11A")] = 11
        print("Blackjack! You win!")
        
    elif ("11A" in dealerScore and 10 in dealerScore) == 21:
        dealerScore[dealerScore.index("11A")] = 11
        print("Blackjack! The Dealer wins!")

    else:

        keepGoing = True
        
        while keepGoing:

            if "11A" in dealerScore:
                dealerScore[dealerScore.index("11A")] = 11
                
            if "11A" in playerScore:

                while True: 
                    print("You have an Ace in your hand. Would you like the Ace to be 1 or 11?")
                    print("Your hand is {}".format(", ".join(playerHand)))
                    aceOr11 = input("1/11 > ")

                    try:
                        aceOr11 = int(aceOr11)
                            
                        if aceOr11 == 1:
                            playerScore[playerScore.index("11A")] = 1
                            print(", ".join(playerHand))
                            break
                        
                        elif aceOr11 == 11:
                            playerScore[playerScore.index("11A")] = 11
                            break

                        else:
                            print(invalid)

                    except ValueError:
                        print(invalid)
            
            print("Your hand is {}".format(", ".join(playerHand)))
            print(f"Your hand value is {sum(playerScore)}")

            hitOrNot = "."
            while hitOrNot != "" or sum(playerScore) < 21:
                if sum(playerScore) > 24 or sum(playerScore) == 21 or game.playerHand == 5:
                    break

                print("Would you like a hit? Y/N")
                hitOrNot = input("> ")
                
                try:

                    hitOrNot = hitOrNot.upper()
                    print("\n{}".format(hitOrNot))

                    if hitOrNot.upper() == "Y":
                        card = random.choice(game.deck)
                        game.deck.remove(card)
                        playerHand.append(card)

                        playerScore = game.getHandValue(playerHand)

                        game.playerHand = game.playerHand + 1

                        print("You got a {}".format(card))

                        break
                    
                    elif hitOrNot.upper() == "N":
                        
                        print("Dont want a hit?")

                        keepGoing = False
                        hitOrNot = ""
                        break

                    else:

                        print(invalid + "...")
                        break
                
                except AttributeError:
                    print(invalid + " Perhaps you entered a number?")
                    break
            
            if sum(playerScore) > 21 or sum(playerScore) == 21:
                keepGoing = False
                hitOrNot = ""
                break

    print("Hitting stage finished!\n")
    if sum(playerScore) == 21:
        print("21! You win!")
        print("Dealers total hand value was {}".format(sum(dealerScore)))

    elif sum(playerScore) > 21:
        print("Bust! You lost! Your hand value was {}".format(sum(playerScore)))
    
    elif game.playerHand == 5:
        print("5 card trick! You win!")

    elif sum(playerScore) <= sum(dealerScore) or sum(playerScore) > 24 or sum(dealerScore) == 21:
        print("You lose! Your total was {}".format(sum(playerScore)))
        print("Dealers total was {}".format(sum(dealerScore)))

        # if sum(playerScore) < sum(dealerScore) and sum(dealerScore) != 21:
        #     print("Bust! Your total was {}".format(sum(playerScore)))


        #     print(f"Your new hand is {', '.join(playerHand)} and the value is {playerScore}")
        # break
    
    elif sum(playerScore) >= sum(dealerScore) or sum(playerScore) == 21:
        print("You win!")

        if sum(playerScore) > sum(dealerScore):
            print("Your total score was {}\nDealers score was {}.".format(sum(playerScore), sum(dealerScore)))

    print("Do you want to play again?")

    play = input("> ").lower()
