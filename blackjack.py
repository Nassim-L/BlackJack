import random
from art import logo
import os




def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card






    


def calculat(cards):
    
    if sum(cards)== 21 and len(cards)== 2:
        return 0
    if sum(cards) > 21 and 11 in cards:

        cards.remove(11)
        cards.append(1)
        
        return sum(cards)
        
    return sum(cards)
def compare(userscore ,computerscore):
    if userscore == computerscore :
        return 'its a draw'
    elif computerscore == 0 :
        return 'You lose , Compter he have BlackJack'

    elif userscore == 0 :
        return 'You Win , You have BlackJack'

    elif userscore >21:
        return "you lose , your score is great then 21 "

    elif computerscore > 21:
        return "you win , computer score great then21"

    elif userscore > computerscore :
        return "you win "
    else:
        return " You lose"




def playgame():
    print(logo)
    user_cards = []
    computer_card = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_card.append(deal_card())

    is_game_over = False
    while not is_game_over:

        computerscore = calculat(computer_card)
        yourscore = calculat(user_cards)

        print(f'your cards : {user_cards} , your score : {yourscore} ')
        print(f'computer first card : {computer_card[0]}')

        if computerscore==0 or yourscore == 0 or yourscore > 21:
            is_game_over = True

        else:
            user_should_deal = input('Type "Y" to get another card ,"N" to pass: ')
            if user_should_deal.upper() == "Y":
                user_cards.append(deal_card())

            else:
                is_game_over = True



        while computerscore!=0 and computerscore <= 17:
            computer_card.append(deal_card())
            computerscore = calculat(computer_card)

        print(f'Your finale hand: {user_cards} , Your final score : {yourscore}')
        print(f'computer  finale hand: {user_cards} , Computer final score : {computerscore}')
        result = compare(yourscore,computerscore)
        print(result)

playgame()
while input('Type Y to play again: ').lower() == "y":
    os.system("clear")
    playgame()
