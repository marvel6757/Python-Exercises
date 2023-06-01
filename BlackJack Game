#BlackJack Game 

import random
#from replit import clear
#from art import logo


#hint6
def calculate_score(list_of_cards):
    '''takes a list of cards and return the score for the game'''
    value = sum(list_of_cards)
    #hint7
    if len(list_of_cards) == 2 and value == 21:
        return 0
    #hint8
    if value > 21 and (11 in list_of_cards):
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return value


#hint4
def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


#hint13
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "you Lose, opponent has a BlackJack"
    elif user_score == 0:
        return "you win with a BlackJack"
    elif user_score > 21:
        return "you went over, u lose"
    elif computer_score > 21:
        return "opponent went over, u win"
    elif user_score > computer_score:
        return "u have the highest score, u win"
    else:
        return "opponent has the highest score, u lose"


def play_game():
    #print(logo)

    user_cards = []
    computer_cards = []
    is_gameover = False
    #hint5
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #hint 11
    while not is_gameover:
        user_sum = calculate_score(user_cards)
        computer_sum = calculate_score(computer_cards)
        print(f"User's Cards : {user_cards} User' Score : {user_sum} ")
        print(f"Computer first Cards : {user_cards[0]}")

        #Hint9
        if user_sum > 21 or user_sum == 0 or computer_sum == 0:
            is_gameover = True
        else:
            user_choice = input(
                'type "y" to get another card or "n" to pass :: ')
            #hint 10
            if user_choice == 'y':
                user_cards.append(deal_card())
            elif user_choice == 'n':
                is_gameover = True
            else:
                print("Invalid Input")
    #hint12
    while computer_sum != 0 and computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum = calculate_score(computer_cards)
    print(f"User cards {user_cards} and score {user_sum}")
    print(f"Computer cards {computer_cards} and score {computer_sum}")

    print(compare(user_sum, computer_sum))


#hint14
while input("Do u wanna play blackJack:::") == 'y':
    #clear()
    play_game()
