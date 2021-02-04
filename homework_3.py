from random import choice


# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.


def game(player_choice):
    game_attr = ('Rock', 'Scissors', 'Paper')
    if player_choice not in game_attr:
        return 'Incorrect input!'
    else:
        computer_choice = choice(game_attr)
        player_choice_idx = game_attr.index(player_choice)
        computer_choice_idx = game_attr.index(computer_choice)
        result = f'{player_choice} {computer_choice} - '
        if game_attr[player_choice_idx] == game_attr[computer_choice_idx]:
            return f'{result}Draw!'
        elif game_attr[player_choice_idx] == game_attr[computer_choice_idx - 1]:
            return f'{result}You won!!!'
        else:
            return f'{result}You lose.'


# print(game(input('Please, make your choice: ')))


# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!
def more_tp(data):
    people, tp = data.get('people'), data.get('tp')
    return True if people * 57 * 14 > tp * 500 else False


# print(more_tp({'people': 7, 'tp': 10}))
# print(more_tp({'people': 2, 'tp': 4}))

# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0baca"
# encrypt("karaca") ➞ "0c0r0kaca"
# encrypt("burak") ➞ "k0r3baca"
# encrypt("alpaca") ➞ "0c0pl0aca"
def encrypt(word):
    vowels_enc = {'a': '0', 'e': '1', 'i': '2', 'o': '2', 'u': '3'}
    return ''.join(vowels_enc.get(letter, letter) for letter in word[::-1])


# print(encrypt("banana"))  # ➞ "0n0n0baca"
# print(encrypt("karaca"))  # ➞ "0c0r0kaca"
# print(encrypt("burak"))  # ➞ "k0r3baca"
# print(encrypt("alpaca"))  # ➞ "0c0pl0aca"

# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"
def tic_tac_toe(matrix):
    result = [''.join(matrix[i][j] for j in range(3)) for i in range(3)] + \
             [''.join(matrix[j][i] for j in range(3)) for i in range(3)] + \
             [''.join(matrix[i][i] for i in range(3))] + \
             [''.join(matrix[i][2 - i] for i in range(3))]
    return 'X' if 'XXX' in result else 'O' if 'OOO' in result else 'Draw'

# print(tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]))  # ➞ "X"
#
# print(tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]))  # ➞ "O"
#
# print(tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]))  # ➞ "Draw"