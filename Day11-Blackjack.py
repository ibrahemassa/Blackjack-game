import os
import random as rand

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end = False
if input("Do u wanna play a game of black jack? y/n ") != "y":
    end = True
os.system('cls')
while not end:
    os.system('cls')
    player_cards = [cards[rand.randint(0,len(cards)-1)], cards[rand.randint(0,len(cards)-1)]]
    player_score = player_cards[0] + player_cards[1]
    computer_cards = [cards[rand.randint(0,len(cards)-1)], cards[rand.randint(0,len(cards)-1)]]
    computer_score = computer_cards[0] + computer_cards[1]
    while computer_score < 16:
        computer_cards.append(cards[rand.randint(0,len(cards)-1)])
    print(logo)
    print(f"Your cards are: {player_cards}, current score: {player_score}")
    print(f"Computer's first card is: {computer_cards[0]}")
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        player_cards.append(cards[rand.randint(0,len(cards)-1)])
        player_score += player_cards[2]
    if player_score > 21:
        if player_cards.find(11):
            player_cards[player_cards.index[11]] = 1
        else:
            print(f"DUST, your score is: {player_score}")
            if input("Do u wanna play agian? y/n ") != 'y':
                end = True
    print(f"Your final hand is: {player_cards}, final score: {player_score}")
    print(f"computer's final hand is: {computer_cards}, final score: {computer_score}")
    if player_score > computer_score or computer_score > 21:
        print("U win 😎")
    else:
        print("U lose 😂")
    if input("Do u wanna play agian? y/n ") != 'y':
        end = True
        