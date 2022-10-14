#Blackjack Project

#Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from replit import clear
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
comp_cards = []
end = False


# Function that asks the user if they wanted to play again after every game
def restart():
    continue_game = input("Do you want to play blackjack again? Type 'y' for yes and 'n' for no")
    if continue_game == "y":
        clear()
        player_cards.clear()
        comp_cards.clear()
        blackjack_game()
    if continue_game == "n":
        print("Thank you for playing")
        clear()
        exit()


def blackjack_game():
    start_game = input("Do  you want to play blackjack? Type 'y' or 'n' ")
    if start_game == "y":
        print(logo)
        # Generates a random value from "cards" list and appends it to the player and computer card lists
        for random_card in range(0, 2):
            random_cards1 = random.choice(cards)
            random_cards2 = random.choice(cards)
            player_cards.append(random_cards1)
            comp_cards.append(random_cards2)

        # Sum the total value of cards for both player and computer
        player_first_score = sum(player_cards)
        computer_first_score = sum(comp_cards)
        print(f"Your cards:{player_cards}, current score: {player_first_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        comp_total = sum(comp_cards)

        # Adds a card for computer if the total is less than 17
        while comp_total < 17:
            random_comp = random.choice(cards)
            comp_cards.append(random_comp)
            comp_total = sum(comp_cards)

        end = False
        ace = False
        player_total = sum(player_cards)
        # Since Ace represents 11 or 1, this if statement catches a condition when the players sum is over 21 and has
        # an ace.
        if sum(player_cards) > 21 and 11 in player_cards:
            ace = True

            # Asking player if they want to add a card to their deck. While loop exits if either player/computer looses.

        while player_total <= 21 and not end or ace:
            hit_or_stand = input("Type 'y' to get another card, type 'n' to pass:")
            # Add an extra card to player list, and calculating the player's card sum
            if hit_or_stand == "y":
                add_rand = random.choice(cards)
                player_cards.append(add_rand)
                player_sum = sum(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_sum}")
                # Switches the value of the ace from 11 to 1 if the ace condition is true
                if ace:
                    index = player_cards.index(11)
                    player_cards[index] = 1
                    comp_total = sum(comp_cards)
                    player_total = sum(player_cards)
                # Player loses if card sum goes over 21
                if sum(player_cards) > 21:
                    print("You went over, you lose!")
                    restart()

            # Check and compare both player and computer cards and determine the winner
            if hit_or_stand == "n":
                if sum(player_cards) > 21 and 11 in player_cards:
                    index = player_cards.index(11)
                    player_cards[index] = 1
                comp_total = sum(comp_cards)
                player_total = sum(player_cards)
                if sum(player_cards) > 21:
                    print("You went over, you lose!")
                    restart()
                elif sum(comp_cards) > 21:
                    print(f"Computer cards: {comp_cards}, current score: {comp_total}")
                    print("The computer went over, you win!")
                    restart()
                elif player_total == comp_total:
                    print(f"Your cards: {player_cards}, current score: {player_total}")

                    print("It's a draw!")
                    restart()
                elif player_total > comp_total:
                    print(f"Your cards: {player_cards}, current score: {player_total}")
                    print(f"Computer cards: {comp_cards}, current score: {comp_total}")
                    print("You win yay")
                    restart()
                elif comp_total > player_total:
                    print(f"Your cards: {player_cards}, current score: {player_total}")
                    print(f"Computer cards: {comp_cards}, current score: {comp_total}")
                    print("You lost rip")
                    restart()


    else:
        end = True


blackjack_game()
