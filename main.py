try:
    import random
    import math
except ModuleNotFoundError:
    print('ModuleNotFound')

def display_board(board): 

    print('\n') 
    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#choose function

def player_input():
    marker = input('Player 1: Do you want to be X or O? ').upper()
    
    while not (marker == 'X' or marker == 'O'):
        print('invalid input input must be X or O')
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Game_on function

def replay():

    Game_on=input('you want to play or not (for yes y and for no n : )').lower()

    return Game_on=='y'

#Choose first function

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#space_check_function

def space_check(board, position):
    
    return board[position] == ' '

#index position function

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

# board full function 

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# select random

def select_random(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

#AI for level 1

def level1():
    possiblemoves = []

    for i in [1,2,3,4,5,6,7,8,9]:
        if space_check(theBoard, i):
            possiblemoves.append(i)

    move = select_random(possiblemoves)
    return move


#AI for level 2

def level2():
    possiblemoves = []
    move = 0

    for i in [1,2,3,4,5,6,7,8,9]:
        if space_check(theBoard, i):
            possiblemoves.append(i)

    for let in player2_marker:

        for i in possiblemoves:
            boardcopy = theBoard[:]
            boardcopy[i] = let
            if win_check(boardcopy, let):
                move = i
                return move

    for let in player1_marker:

        for i in possiblemoves:
            boardcopy = theBoard[:]
            boardcopy[i] = let
            if win_check(boardcopy,let):
                move = i
                return move

    cornersopen = []
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)

    if len(cornersopen) > 0:
        move = select_random(cornersopen)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgesopen = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)

    if len(edgesopen) > 0:
        move = select_random(edgesopen)

    return move


def num_of_empty_spaces(board):
	possiblemoves = []
	for j in [1,2,3,4,5,6,7,8,9]:
		if space_check(board, j):
			possiblemoves.append(j)

	return len(possiblemoves)


# put_O_or_X_func
 
def place_marker(board, marker, position):
    board[position] = marker

def minimax(player,board):
	maxplayer = player2_marker
	other_player = player1_marker if player == player2_marker else player2_marker

	if win_check(board, other_player):
		return {"position":None, "score":1*( num_of_empty_spaces(board)+1 ) if other_player == maxplayer else -1*( num_of_empty_spaces(board)+1 ) }

	elif num_of_empty_spaces(board) == 0:
		return {"position":None, "score":0}

	if player == maxplayer:
		best = {"position":None, "score":-math.inf}

	else:
		best = {"position":None, "score":math.inf}

	possiblemoves = []
	for i in [1,2,3,4,5,6,7,8,9]:
		if space_check(board,i):
			possiblemoves.append(i)

	for i in possiblemoves:
		place_marker(board,player,i)
		sim_score = minimax(other_player,board)
		board[i]=' '
		sim_score["position"]=i

		if player==maxplayer:
			if sim_score["score"] > best["score"]:
				best = sim_score

		else:
			if sim_score["score"] < best["score"]:
				best = sim_score

	return best

def level3(board):
	if num_of_empty_spaces(board)==9:
		move = 1
		return move
	else:
		best_move = minimax(player2_marker, board)
		return best_move["position"]

# Win_func

def win_check(board, mark):


    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# the game

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10

    multiplayer=int(input('do you want to play against human player or computer:(for human player enter 1 for computer player enter 2) '))

    while not(multiplayer==1 or multiplayer==2):
        print('Invalid input input must be 1 or 2')
        multiplayer = int(input('do you want to play against human player or computer:(for human player enter 1 for computer player enter 2) '))

    if multiplayer==1:
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        while game_on:

            #player1 turn

            if turn == 'Player 1':                
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! player 1 won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.
                
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1' 

    if multiplayer == 2:
        level = int(input('Which level you want to play (1,2,3) '))
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        while game_on:        
            if level == 1:
                #player1 turn
                if turn == 'Player 1':                
                    display_board(theBoard)
                    position = player_choice(theBoard)
                    place_marker(theBoard, player1_marker, position)

                    if win_check(theBoard, player1_marker):
                        display_board(theBoard)
                        print('Congratulations! you won the game!')
                        game_on = False
                    else:
                        if full_board_check(theBoard):
                            display_board(theBoard)
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 2'

                else:
                    display_board(theBoard)
                    position = level1()
                    place_marker(theBoard, player2_marker, position)

                    if win_check(theBoard, player2_marker):
                        display_board(theBoard)
                        print('Sorry Computer won the game')
                        game_on = False
                    elif full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is draw!')
                        break
                    else:
                        turn = 'Player 1'

            if level == 2:

                #player1 turn

                if turn == 'Player 1':                
                    display_board(theBoard)
                    position = player_choice(theBoard)
                    place_marker(theBoard, player1_marker, position)

                    if win_check(theBoard, player1_marker):
                        display_board(theBoard)
                        print('Congratulations! you won the game!')
                        game_on = False
                    else:
                        if full_board_check(theBoard):
                            display_board(theBoard)
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 2'

                else:
                    display_board(theBoard)
                    position = level2()
                    place_marker(theBoard, player2_marker, position)

                    if win_check(theBoard, player2_marker):
                        display_board(theBoard)
                        print('Sorry Computer won the game')
                        game_on = False
                    else:
                        if full_board_check(theBoard):
                            display_board(theBoard)
                            print('The game is draw!')
                            break
                        else:
                            turn = 'Player 1'  

            if level == 3:

                #player1 turn

                if turn == 'Player 1':                
                    display_board(theBoard)
                    position = player_choice(theBoard)
                    place_marker(theBoard, player1_marker, position)

                    if win_check(theBoard, player1_marker):
                        display_board(theBoard)
                        print('Congratulations! you won the game!')
                        game_on = False
                    else:
                        if full_board_check(theBoard):
                            display_board(theBoard)
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 2'

                else:
                    display_board(theBoard)
                    position = level3(theBoard)
                    place_marker(theBoard, player2_marker, position)

                    if win_check(theBoard, player2_marker):
                        display_board(theBoard)
                        print('Sorry Computer won the game')
                        game_on = False
                    else:
                        if full_board_check(theBoard):
                            display_board(theBoard)
                            print('The game is draw!')
                            break
                        else:
                            turn = 'Player 1'  



    if not replay():
        break
