import random
from art import logo

# Initialize variables
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True
cards = {}
game = False


# Initialize the hands
def init_hands():
    global cards 
    cards = {
        "Player": {"hand": [], "score": 0},
        "Dealer": {"hand": [], "score": 0},
        }


# Deal the initial cards
def init_deal():
    # Deal initial cards (dealt cards are not removed from the deck)
    for i in range(0, 2):
        card = random.choice(deck)
        cards["Player"]["hand"].append(card)
        cards["Player"]["score"] += card
        card = random.choice(deck)
        cards["Dealer"]["hand"].append(card)
        cards["Dealer"]["score"] += card

    # Display initial hands to the player
    print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
    print(f'Dealer hand: [{cards["Dealer"]["hand"][0]}, _ ]')


# Does Player want a new card?
def new_card_player():
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
            i = 0
            while bust and i < len(cards["Player"]["hand"]):
                for _ in cards["Player"]["hand"]:
                    if cards["Player"]["hand"][i] == 11:
                        cards["Player"]["hand"][i] = 1
                        cards["Player"]["score"] -= 10
                        bust = False
                        new_card_player()
                    i += 1
            if bust:
                print(f'You Lose! You bust with a score of {cards["Player"]["score"]}')
                global game
                game = False
            else:
                new_card_player()
        else:
            new_card_player()


# Check for Blackjack
def check_blackjack():
    if cards["Player"]["score"] == 21:
        if cards["Dealer"]["score"] == 21: 
            print("Draw. Dealer also has Blackjack.")
        else:
            print("You win! You have Blackjack.")
        print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
        print(f'Dealer hand: {cards["Dealer"]["hand"]}, score: {cards["Dealer"]["score"]}')
        global game
        game = False


# New Dealer cards
def new_card_dealer():
    while cards["Dealer"]["score"] < 16:
        card = random.choice(deck)
        cards["Dealer"]["hand"].append(card)
        cards["Dealer"]["score"] += card
        print(f'Dealer\'s hand:   {cards["Dealer"]["hand"]}, score: {cards["Dealer"]["score"]}')

        # Check Dealer score.
        # If > 21 then check for Ace and make value = 1
        if cards["Dealer"]["score"] > 21: 
            bust = True
            i = 0
            while bust and i < len(cards["Dealer"]["hand"]):
                for _ in cards["Dealer"]["hand"]:
                    if cards["Dealer"]["hand"][i] == 11:
                        cards["Dealer"]["hand"][i] = 1
                        cards["Dealer"]["score"] -= 10
                        bust = False
                        new_card_dealer()
                    i += 1
            if bust:
                print(f'You Win! Dealer bust with a score of {cards["Dealer"]["score"]}')
                global game
                game = False


# Compare scores to decide winner
def decide_winner():
    if cards["Dealer"]["score"] > cards["Player"]["score"]:
        print("You Lose!")
    if cards["Dealer"]["score"] == cards["Player"]["score"]:
        print("Draw")
    if cards["Dealer"]["score"] < cards["Player"]["score"]:
        print("You Win!")
    print(f'Your hand:   {cards["Player"]["hand"]}, score: {cards["Player"]["score"]}')
    print(f'Dealer hand: {cards["Dealer"]["hand"]}, score: {cards["Dealer"]["score"]}')
    global game
    game = False


# ---------------------------------------------

# Start Game
while play:
    if input("Do you want to play a game of Blackjack? (Y)/N ").lower() == "n":
        play = False
        continue
    else:
        game = True

    # Print logo
    print(logo)

    init_hands()
    init_deal()
    check_blackjack()
    if game:
        new_card_player()
    if game:
        new_card_dealer()
    if game:
        decide_winner()
