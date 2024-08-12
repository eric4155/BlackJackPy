import random
import time

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.deck.append(new_card)       
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.value = 0
        self.cards = []
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

    def display_hand(self):
        for i in range(len(self.cards)):
            print(self.cards[i])
            time.sleep(1)
    
    def hit(self, card):
        self.add_card(self, card)
    
    def win(self):
        return self.value == 21
    def bust(self):
        return self.value > 21
    
    

class Bank_roll:
    def __init__(self, amount):
        self.amount = amount
    
    def lose(self, amount_lost):
        self.amount -= amount_lost

    def win(self, amount_won):
        self.amount += amount_won

    def __str__(self) -> str:
        return self.amount
    
    
def gameplay():
    print("Welcome to blackjack! Ace is high card only.")
    bankroll = Bank_roll(int(input("How much money do you have? ")))
    
    # while loop controls when the game will temrinate based on user response
    game_continuing = "Y"

    while game_continuing == "Y":  
        bet_amount = int(input("How much are you betting? "))
        deck = Deck()
        deck.shuffle()
        new_hand = Hand()
        dealer_hand = Hand()
    # Creating a new shuffled deck and hand instances for every new game
    # Player receives 2 initial cards
        while len(new_hand.cards) < 2:
            new_hand.add_card(deck.deal())
        # Dealer receives initial card
        dealer_hand.add_card(deck.deal())
        print("Your hand is: ")
        new_hand.display_hand()
        if new_hand.win():
            print("You win!")
            bankroll.win(bet_amount)
            print(f"Your new bankroll is {bankroll.amount}")
            break

        print(f"Your hand's value is {new_hand.value}")
        print("The dealer has a: ")
        dealer_hand.display_hand()

        print(f"The dealer's hand's value is {dealer_hand.value}")
        action = input("Would you like to (H)it or (S)tay? ")
        
        while action == "H":
            new_card = deck.deal()
            new_hand.add_card(new_card)
            print(f"You have been dealt the {new_card}. Your updated hand is: ")
            new_hand.display_hand()
            print(f"Your hand's value is {new_hand.value}")
            if new_hand.win():
                print("You win!")
                bankroll.win(bet_amount)
                print(f"Your new bankroll is {bankroll.amount}")
                dealer_hand.value = 22
                break
            if new_hand.bust():
                print("You busted!")
                bankroll.lose(bet_amount)
                print(f"Your new bankroll is {bankroll.amount}")
                dealer_hand.value = 22
                break
            action = input("Would you like to (H)it or (S)tay? ")
            
        while dealer_hand.value < 17:
            new_card = deck.deal()
            dealer_hand.add_card(new_card)
            print(f"The dealer flipped a {new_card}. The dealer's hand is now: ")
            dealer_hand.display_hand()
            print(f"The dealer's hand's value is {dealer_hand.value}")
            if dealer_hand.bust():
                print("The dealer busted!")
                bankroll.win(bet_amount)
                print(f"Your new bankroll is {bankroll.amount}")
                break
            elif dealer_hand.value > new_hand.value:
                print("The dealer wins")
                bankroll.lose(bet_amount)
                print(f"Your new bankroll is {bankroll.amount}")
                break
            elif dealer_hand.value == new_hand.value:
                print(f"You tied!")
                print(f"Your bankroll has not changed: {bankroll.amount}")
                break
            elif dealer_hand.value == 17:
                bankroll.win(bet_amount)
                print(f"You win! your new bankroll is {bankroll.amount}")
            time.sleep(3)

        if bankroll.amount == 0:
            print("You are out of money. Better luck next time!")
            break

        game_continuing = input("Would you like to play again? Y or N: ")
        while game_continuing != "Y" and game_continuing != "N":
            game_continuing = input("Would you like to play again? Y or N: ")
            

gameplay()


    
