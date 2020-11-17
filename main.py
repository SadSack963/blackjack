deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

# Start
if input("Do you want to play a game of Blackjack? (Y)/N" ).lower() == "n":
    quit()

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

# Display hands to the player
print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
print(f'Dealer hand: [{cards["Dealer"]["hand"][0]}, _]')

# Check for Blackjack
if cards["Player"]["score"] == 21:
    if cards["Dealer"]["score"] == 21: 
        print("Draw. Dealer also has Blackjack.")
    else:
        print("You win! You have Blackjack.")
    print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
    print(f'Dealer hand: {cards["Dealer"]["hand"]}, score: {cards["Dealer"]["score"]}')




