matrix = [
    [0], [1], [2],
    [3], [4], [5],
    [6], [7], [8]
]
# matrix = [
#     ["[0]", "[1]", "[2]"],
#     ["[3]", "[4]", "[5]"],
#     ["[6]", "[7]", ]
# ]

def play_game():
    play_game.counter+=1
    prompt = "{} {} {}\n{} {} {}\n{} {} {}\ninput a position for ".format(matrix[0], matrix[1], matrix[2],
                                                                          matrix[3], matrix[4], matrix[5],
                                                                          matrix[6], matrix[7], matrix[8])
    try:
        if play_game.counter %2 == 1:
            play = int(input(prompt + "X:\n"))
        else:
            play = int(input(prompt + "O:\n"))
    except ValueError:
        print("Input was not an integer.")
    try:
        if matrix[play] == "[X]" or matrix[play] == "[O]":
            print("Someone has already played there :(")
        elif play_game.counter % 2 == 1:
            matrix[play] = "[X]"
        else:
            matrix[play] = "[O]"
    except IndexError:
        print("input was out of bounds.\nEnter a number from 0-8.")
        return prompt

def check_board(board):
    if matrix[0] == matrix[1] and matrix[1] == matrix[2]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over
    elif matrix[3] == matrix[4] and matrix[4] == matrix[5]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over
    elif matrix[6] == matrix[7] and matrix[7] == matrix[8]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over
    elif matrix[0] == matrix[3] and matrix[3] == matrix[6]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over
    elif matrix[1] == matrix[4] and matrix[4] == matrix[7]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over
    elif matrix[2] == matrix[5] and matrix[5] == matrix[8]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over
    elif matrix[0] == matrix[4] and matrix[4] == matrix[8]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over
    elif matrix[2] == matrix[4] and matrix[4] == matrix[6]:
        if matrix[0] == "[X]":
            print("X is the winner!")
            game_over = True
            return game_over
        else:
            print("O is the winner!")
            game_over = True
            return game_over

play_game.counter = 0
game_over = False
i=0
while game_over == False:
    play_game()
    check_board(matrix)