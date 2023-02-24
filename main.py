import art
import random

player_cards = {}
cpu_cards = {}

card_pool = {
        "2 of Hearts": 2,
        "3 of Hearts": 3,
        "4 of Hearts": 4,
        "5 of Hearts": 5,
        "6 of Hearts": 6,
        "7 of Hearts": 7,
        "8 of Hearts": 8,
        "9 of Hearts": 9,
        "10 of Hearts": 10,
        "Jack of Hearts": 10,
        "Queen of Hearts": 10,
        "King of Hearts": 10,
        "Ace of Hearts": 1,
        "2 of Diamonds": 2,
        "3 of Diamonds": 3,
        "4 of Diamonds": 4,
        "5 of Diamonds": 5,
        "6 of Diamonds": 6,
        "7 of Diamonds": 7,
        "8 of Diamonds": 8,
        "9 of Diamonds": 9,
        "10 of Diamonds": 10,
        "Jack of Diamonds": 10,
        "Queen of Diamonds": 10,
        "King of Diamonds": 10,
        "Ace of Diamonds": 1,
        "2 of Clubs": 2,
        "3 of Clubs": 3,
        "4 of Clubs": 4,
        "5 of Clubs": 5,
        "6 of Clubs": 6,
        "7 of Clubs": 7,
        "8 of Clubs": 8,
        "9 of Clubs": 9,
        "10 of Clubs": 10,
        "Jack of Clubs": 10,
        "Queen of Clubs": 10,
        "King of Clubs": 10,
        "Ace of Clubs": 1,
        "2 of Spades": 2,
        "3 of Spades": 3,
        "4 of Spades": 4,
        "5 of Spades": 5,
        "6 of Spades": 6,
        "7 of Spades": 7,
        "8 of Spades": 8,
        "9 of Spades": 9,
        "10 of Spades": 10,
        "Jack of Spades": 10,
        "Queen of Spades": 10,
        "King of Spades": 10,
        "Ace of Spades": 1,
    }


def get_cpu_cards():
    sum_cpu = 0
    for i in range(0, 2):
        key, value = random.choice(list(card_pool.items()))
        cpu_cards[key] = value
        card_pool.pop(key)
        sum_cpu += value
    return sum_cpu


def get_player_cards():
    sum_player = 0
    for i in range(0, 2):
        key, value = random.choice(list(card_pool.items()))
        player_cards[key] = value
        card_pool.pop(key)
        sum_player += value
    return sum_player


def get_new_card(player):
    key, value = random.choice(list(card_pool.items()))
    player[key] = value
    card_pool.pop(key)
    return value


def check_cards(player_total_sum, cpu_total_sum):
    if player_total_sum <= 21 and cpu_total_sum <= 21:
        if player_total_sum < cpu_total_sum:
            print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - You Lose.")
        elif player_total_sum > cpu_total_sum:
            print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - You Win.")
        else:
            print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - It's a draw.")
    elif player_total_sum <= 21 and cpu_total_sum > 21:
        print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - Dealer busted. You Win.")
    elif player_total_sum > 21 and cpu_total_sum <= 21:
        print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - Busted. You Lose")
    elif player_total_sum == cpu_total_sum == 21:
        print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - Both players Blackjacked. It's a draw")
    elif player_total_sum == 21 and cpu_total_sum < 21:
        print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - Blackjack. You Win")
    elif player_total_sum < 21 and cpu_total_sum == 21:
        print(f"Player({player_total_sum})-CPU({cpu_total_sum}) - Dealer Blackjacked. You lose")


def play():
    print(art.logo)
    player_total_sum = get_player_cards()
    cpu_total_sum = get_cpu_cards()
    game_ended = False
    player_finished = False
    cpu_finished = False
    while not game_ended:
        while not player_finished:
            print(f"{list(player_cards.keys())} - Total: {player_total_sum}")
            option_player = input("Hit or stay? (h/s): ")
            if option_player == "h":
                player_total_sum += get_new_card(player_cards)

            else:
                player_finished = True
        while not cpu_finished:
            if cpu_total_sum <= 14:
                cpu_total_sum += get_new_card(cpu_cards)
            elif 14 <= cpu_total_sum <= 19:
                option_cpu = random.choice(range(1, 3))
                if option_cpu == 1:
                    cpu_total_sum += get_new_card(cpu_cards)
                else:
                    cpu_finished = True
            else:
                cpu_finished = True

        if cpu_finished and player_finished:
            game_ended = True
    # print(card_pool)
    print(f"{list(player_cards.keys())}")
    print(f"{list(cpu_cards.keys())}")
    check_cards(player_total_sum, cpu_total_sum)


option = input("Do you want to play Blackjack? (y/n) ").lower()
if option == "y":
    play()
else:
    print("Game end.")
