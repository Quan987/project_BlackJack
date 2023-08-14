from img import *
from function import *
import os, random


def cls():
    """This method is use to clear the game board"""
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card(player_list):
    """This method get a random key from the cards dictionaries"""
    return player_list.append(random.choice(list(cards)))


def init_deal(list_switch, player_list):
    """This method initiate the initial deal for the players"""
    if list_switch == True:
        for i in range(2):
            deal_card(player_list=player_list)
    else:
        deal_card(player_list=player_list)
    return player_list


def list_to_int(list):
    """This method convert list to int data type and calculate its sum"""
    list_sum = 0
    for i in range(len(list)):
        list_sum += cards[list[i]]
    return list_sum


def calc(player_list):
    """This method calculate the score for the players"""
    temp_list = player_list.copy()
    player_sum = 0
    for i in player_list:
        if len(player_list) > 2 and i == 'A':
            if list_to_int(temp_list) > 21:
                cards['A'] = 1
        player_sum += cards[i]
    cards['A'] = 11
    return player_sum


def is_blackjack(player_list):
    """This method check if player got blackjack at the beginning of the game"""
    counter = 0
    if (len(player_list) == 2):
        if (player_list[0] == 'A') and (
                player_list[1] == '10' or player_list[1] == 'J' or player_list[1] == 'Q' or player_list[1] == 'K'):
            counter += 1
        elif (player_list[0] == '10' or player_list[0] == 'J' or player_list[0] == 'Q' or player_list[0] == 'K') and (
                player_list[1] == 'A'):
            counter += 1
    return counter == 1  # Return True if counter == 1


def is_over21(player_list):
    """This method check if player are over 21"""
    if calc(player_list) > 21:
        return True


def play_game():
    """This method is use to initiate the game"""
    user_list = []
    cp_list = []
    stopper = False
    print(f"\nYour card is: {init_deal(list_switch=True, player_list=user_list)}, your score is: {calc(user_list)}")
    print(
        f"Computer card is: {init_deal(list_switch=False, player_list=cp_list)}, computer score is: {calc(cp_list)}\n")
    while not stopper:
        if is_blackjack(user_list):
            stopper = True
            print("You got Black Jack!\n\nYou Win!")
        else:
            if input("Draw a card? Type 'y' or 'n': ") == 'y':
                cls()
                deal_card(user_list)
                print(f"You Draw!\nYour card is: {user_list}, your score is: {calc(user_list)}\n")
                if is_over21(user_list):
                    stopper = True
                    print("You Busts! Computer Win!")
            else:
                while calc(cp_list) < calc(user_list):
                    deal_card(cp_list)
                    print(f"\nComputer Draw!\nComputer card is: {cp_list}, computer score is: {calc(cp_list)}")
                if is_over21(cp_list) or calc(user_list) > calc(cp_list):
                    stopper = True
                    if is_over21(cp_list):
                        print("\nComputer Busts! You Win!")
                    else:
                        print("\nYou have higher hand! You Win!")
                elif calc(user_list) < calc(cp_list):
                    stopper = True
                    print("\nComputer have higher hand! Computer Win!")
                else:
                    print("\nBoth hand are equal! Tie!")

