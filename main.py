deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

# Start
play = True
# while play:
if input("Do you want to play a game of Blackjack? (Y)/N" ).lower() == "n":
    play = False

# Initialize the hands
cards = {
    "Player": {"hand": [], "score": 0},
    "Dealer": {"hand": [], "score": 0},
    }

# Print logo
from art import logo
print(logo)

# Deal initial cards (dealt cards are not removed from the deck)
for i in range(0,2):
    card = random.choice(deck)
    cards["Player"]["hand"].append(card)
    cards["Player"]["score"] += card
    card = random.choice(deck)
    cards["Dealer"]["hand"].append(card)
    cards["Dealer"]["score"] += card

# Display initial hands to the player
print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
print(f'Dealer hand: [{cards["Dealer"]["hand"][0]}, _ ]')

# Check for Blackjack
if cards["Player"]["score"] == 21:
    if cards["Dealer"]["score"] == 21: 
        print("Draw. Dealer also has Blackjack.")
    else:
        print("You win! You have Blackjack.")
    print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
    print(f'Dealer hand: {cards["Dealer"]["hand"]}, score: {cards["Dealer"]["score"]}')
    play = False

# Another card for Player
new_card = input("Do you want another card? Y/(N) ").lower()
if new_card == "y":
    card = random.choice(deck)
    cards["Player"]["hand"].append(card)
    cards["Player"]["score"] += card
    print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')

    # Check Player score.
    # If > 21 then check for Ace and make value = 1
    if cards["Player"]["score"] > 21: 
        bust = True
        while bust:
            for i in cards["Player"]["hand"]:
                if cards["Player"]["hand"][i] == 11:
                    cards["Player"]["hand"][i] == 1
                    cards["Player"]["score"] -= 10
                    bust = False
    if bust:
        print(f'You Lose! You bust with a score of {cards["Player"]["score"]}')
    else:
        # TODO Pick another card?
        print()

# New Dealer cards
while cards["Dealer"]["score"] < 16:
    card = random.choice(deck)
    cards["Dealer"]["hand"].append(card)
    cards["Dealer"]["score"] += card
    print(f'Dealer\'s hand:   {cards["Dealer"]["hand"]}, score: {cards["Dealer"]["score"]}')

    # Check Dealer score.
    # If > 21 then check for Ace and make value = 1
    if cards["Dealer"]["score"] > 21: 
        bust = True
        while bust:
            for i in cards["Dealer"]["hand"]:
                if cards["Dealer"]["hand"][i] == 11:
                    cards["Dealer"]["hand"][i] == 1
                    cards["Dealer"]["score"] -= 10
                    bust = False
    if bust:
        print(f'You Win! Dealer bust with a score of {cards["Dealer"]["score"]}')

# Compare scores to decide winner
if cards["Dealer"]["score"] > cards["Player"]["score"]:
    print("You Lose!")
if cards["Dealer"]["score"] == cards["Player"]["score"]:
    print("Draw")
if cards["Dealer"]["score"] > cards["Player"]["score"]:
    print("You Win!")
print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
print(f'Dealer hand: {cards["Dealer"]["hand"]}, score: {cards["Dealer"]["score"]}')
play = False

