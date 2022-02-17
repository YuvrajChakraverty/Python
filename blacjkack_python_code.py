import random

val={'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}
suits=('Clubs','Spades','Diamonds','Hearts')
ranks=('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
suits=('Clubs','Spades','Diamonds','Hearts')

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=val[rank]
        
    def __str__(self):
        return "-> "+self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards=[]
        
        for s in suits:
            for r in ranks:
                created_card= Card(s,r)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

class Players:
    def __init__(self,name):
        self.name=name
        self.cards_on_board=[]
        self.sum_of_cards=0
        self.balance=10000
        self.bet_amount=0
        self.wins=0
        
    def __str__(self):
        return f"\nPlayer name: {self.name}\nWallet Balance: ${self.balance}  Wins: {self.wins}"
    
    def win(self):
        self.balance+=self.bet_amount
        self.wins+=1
    
    def lose(self):
        self.balance-=self.bet_amount
    
    def draw_card(self,deck_object):
        popped_card=deck_object.all_cards.pop(0)
        self.cards_on_board.append(popped_card)
        self.sum_of_cards+=popped_card.value
        
    def return_cards(self,deck_object):
        deck_object.all_cards.extend(self.cards_on_board)
        self.cards_on_board=[]
        self.sum_of_cards=0
            
    def show_cards(self):
        
        for x in self.cards_on_board:
            print(x)
        print(f"\n# Sum of {self.name}'s card values: {self.sum_of_cards}")
              
    def accept_bet(self):
        while True:
            self.bet_amount=int(input("\nEnter the amount you want to bet for: "))
            if self.balance<self.bet_amount:
                print("\nNot enough balance! Enter the amount again.")
            else:
                print("\nBet placed!")
                break
                
                
play=1
rounds=1
name=input("Enter your name: ")
new_player=Players(name)
print('\nYou have an initial balance of $10000')
computer=Players('Computer')
new_deck=Deck()

while play==1:
    
    choice=0
    if new_player.balance==0:
        print("\n\nZero Balance, You can't play anymore!")
        break
    new_deck.shuffle()
    print(f"\n\n== Round {rounds} ==")
    print(new_player)
    new_player.accept_bet()
    computer.draw_card(new_deck)
    computer.draw_card(new_deck)
    new_player.draw_card(new_deck)
    new_player.draw_card(new_deck)
    print("\n@ Computer's initial cards are:\n")
    print(computer.cards_on_board[0])
    print("-> ???  of  ???\n")
    print(f"@ {new_player.name}'s initial cards are:\n")
    new_player.show_cards()
    
    while choice!=1:
       
        choice=int(input("\n\n%% Enter choice: 1. Stay  2. Hit : "))
        
        if choice==1:
                bust=0
                while computer.sum_of_cards<=new_player.sum_of_cards:
                    computer.draw_card(new_deck)
                    if computer.sum_of_cards==21==new_player.sum_of_cards:
                        print("\n\n* Tie Game! *")
                        break
                    if computer.sum_of_cards>21:
                        print("\n!! Computer busted with the following cards:\n")
                        computer.show_cards()
                        print("\n\n* You won! *")
                        new_player.win()
                        bust=1
                        break
                
                if bust==0:
                    print("\n\nComputer won with the following cards:\n")
                    computer.show_cards()
                    print("\n\n* You lost! Better luck next time *")
                    new_player.lose()
                    break
        
        elif choice==2:
            new_player.draw_card(new_deck)
            print(f"\n\n@ Now {new_player.name} has cards:\n")
            new_player.show_cards()
            if new_player.sum_of_cards>21:
                print("\n!! Busted!")
                print("\n* You lost! Better luck next time! *")
                new_player.lose()
                break
                
        else:
            print("\n\nInvalid Input! Please enter again")
            
    print(new_player)
    new_player.return_cards(new_deck)
    computer.return_cards(new_deck)
    play=int(input("\n%% Enter 1 to play another round & 0 to exit: "))
    print("---------------------------------------------------------------")
    rounds+=1
    

print("\n\nFinal Results:\n")
print(new_player)
if new_player.balance>=10000:
    print(f'\nYou Won a Total of ${new_player.balance-10000} !')
else:
    print(f'\nYou Beared a Loss of ${10000-new_player.balance} !')
print("\nThank you for Playing!")