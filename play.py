import random
from IPython.display import clear_output

player_list = ['A', 'B']
player_mark = {
    'A': 'X',
    'B': 'O'
}

valid_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3x3 board to correspond 
board_positions = {
    '1_S': '',
    '1_M': '',
    '1_E': '',
    '2_S': '',
    '2_M': '',
    '2_E': '',
    '3_S': '',
    '3_M': '',
    '3_E': '',
}
# a mapping dictionary to make it easier to assign marks to the board position - gets rid of a long if else
# routine to bring the output
num_to_board = {
    1: '1_S',
    2: '1_M',
    3: '1_E',
    4: '2_S',
    5: '2_M',
    6: '2_E',
    7: '3_S',
    8: '3_M',
    9: '3_E',
}


# check invalid inputs are less than 3
def rounds_complete(tries: int):
    if tries > 3:
        return True
    return False


# switch player function
def switch_player(player):
    if player == player_list[0]:
        return player_list[1]
    else:
        return player_list[0]


# winning combinations
def winning_combination(played_board, symbol):
    """ working out the winning combinations from the board dictionary """
    # columns comparisons
    if played_board['1_S'] == played_board['2_S'] == played_board['3_S'] == symbol:
        return True
    elif played_board['1_M'] == played_board['2_M'] == played_board['3_M'] == symbol:
        return True
    elif played_board['1_E'] == played_board['2_E'] == played_board['3_E'] == symbol:
        return True
    # row comparisons
    elif played_board['1_S'] == played_board['1_M'] == played_board['1_E'] == symbol:
        return True
    elif played_board['2_S'] == played_board['2_M'] == played_board['2_E'] == symbol:
        return True
    elif played_board['3_S'] == played_board['3_M'] == played_board['3_E'] == symbol:
        return True
    # Diagonal comparisons
    elif played_board['1_S'] == played_board['2_M'] == played_board['3_E'] == symbol:
        return True
    elif played_board['1_E'] == played_board['2_M'] == played_board['3_S'] == symbol:
        return True
    else:
        return False


# printing the board - might not need this at the moment
def board():
    """function to print the board on screen and initialize the board to guide the users on
    the numbers to enter corresponding to the board dictionary"""
    print(' 1| 2 |3')
    print(' 4| 5 |6')
    print(' 7| 8 |9')


# populating the board - this just helps with the formatting and presentation
# on screen
def pop_board(bp):
    """Function for populating and displaying our result on screen main action is on
    board table dictionary initialized above"""
    print(f' {bp["1_S"]} | {bp["1_M"]} | {bp["1_E"]}')
    print(f' {bp["2_S"]} | {bp["2_M"]} | {bp["2_E"]}')
    print(f' {bp["3_S"]} | {bp["3_M"]} | {bp["3_E"]}')


# catching exceptions
def verify_entries(entry):
    """this function is used to prevent the user/player from inserting anything other than numbers as
    input for processing to place on the board"""
    while True:
        try:
            int(entry)
        except ValueError:
            print('enter a valid number')
            entry = input('choose a valid number: ')
        else:
            break
    return int(entry)


# Check if board is full
def board_check(board_game):
    """This function is to check if the board is full and terminate the program by announcing a draw or a win
    it returns True by default to and false to indicate the board is not full yet"""
    for keys in board_game:
        if board_game[keys] == '':
            return False
    return True


player_turn = random.choice(player_list)
play = 0
attempt_a = 0
attempt_b = 0
score_a = 0
score_b = 0
played_figures = []

board()
pop_board(board_positions)

while play < 10:
    player_input: int = verify_entries(input(f'{player_turn} choose a number between 1 and 9: '))
    if player_turn == player_list[0]:
        while (player_input in played_figures) and (not rounds_complete(attempt_a)):
            attempt_a += 1
            if rounds_complete(attempt_a):
                print('you have used up all 4 attempts')
                break
            print('number selected has already been played, or number beyond scope choose another number')
            player_input: int = int(verify_entries(input(f'{player_turn} choose another number')))

        print('valid number chosen: 3 points')
        # this can be a function
        player_position = num_to_board[player_input]
        board_positions[player_position] = player_mark[player_turn]
        board()
        pop_board(board_positions)
        winning = winning_combination(board_positions, player_mark[player_turn])
        clear_output(wait=False)
        if winning:
            score_a += 3
            print(f'congratulations {player_turn} you won')
            break
        # end function
        player_turn = switch_player(player_turn)
        play += 1
        played_figures.append(player_input)

    elif player_turn == player_list[1]:
        while (player_input in played_figures) and (not rounds_complete(attempt_b)):
            attempt_b += 1
            if rounds_complete(attempt_b):
                print('you have used up all 4 attempts')
                break
            print('number selected has already been played, choose another number')
            player_input: int = verify_entries(input(f'{player_turn} choose another number'))

        print('valid number chosen: 3 points')
        # this can be a function
        player_position = num_to_board[player_input]
        board_positions[player_position] = player_mark[player_turn]
        board()
        pop_board(board_positions)
        winning = winning_combination(board_positions, player_mark[player_turn])
        clear_output(wait=False)
        if winning:
            score_a += 3
            print(f'congratulations {player_turn} you won')
            break
        # end of function
        score_b += 3
        player_turn = switch_player(player_turn)
        play += 1
        played_figures.append(player_input)

    if rounds_complete(attempt_a) or rounds_complete(attempt_b):
        print('all valid attempts exhausted. exiting game')
        break
    if board_check(board_positions):
        print('game is a draw')
        break
    else:
        continue
