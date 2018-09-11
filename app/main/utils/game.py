import random

from app.main.utils.helpers import response, possible_moves

# set up players
server_player = 'o'
user_player = 'x'


def is_game_won(board, player):
	"""
	checks if game is won
	returns True or False and the player that won
	"""

	is_won = False

	if (
		board[0] == board[1] == board[2] == player or
		board[3] == board[4] == board[5] == player or
		board[6] == board[7] == board[8] == player or
		board[0] == board[3] == board[6] == player or
		board[1] == board[4] == board[7] == player or
		board[2] == board[5] == board[8] == player or
		board[0] == board[4] == board[8] == player or
		board[2] == board[4] == board[6] == player
	):
		is_won = True

	return is_won


def random_move(board):
	"""
	Server plays randomly
	returns the board with the servers play
	"""
	possible_moves = []
	board_copy = list(board)

	for count, player in enumerate(board):
		if player == ' ':
			possible_moves.append(count)

	if len(possible_moves) != 0:
		move = random.choice(possible_moves)
		board_copy[move] = 'o'

		return ''.join(board_copy)
	
	else:
		return board


def is_draw(board):
	"""
	Check if game is a draw
	returns a Boolean
	"""
	if not is_game_won(board, user_player) and not is_game_won(board, server_player):
		check = [0, 1, 2, 3, 4, 5, 6, 7, 8]

		for item in check:

			if item in board:
				return False

		return True
	
	else:
		return False


def get_possible_moves(board):
	"""
	gets all available spots on the board
	returns a list of available spots
	"""
	possible_moves = []

	for count, player in enumerate(board):
		if player is not server_player and player is not user_player:
			possible_moves.append(count)

	return possible_moves


def convert_board(board):
	"""
	converts the string board
	returns a list of the board
	with the players and the index
	of empty spaces
	"""
	board_copy = list(board)
	for count, instance in enumerate(board_copy):
		if board_copy[count] == ' ':
			board_copy[count] = count
	return board_copy


def minimax(board, player):
	"""
	implements minimax algorithm for decision theory
	returns the best possible move for the server
	"""
	# store all the possible moves
	possible_moves = get_possible_moves(board)

	# generate the score for the board
	if is_game_won(board, server_player):
		return 10

	elif is_game_won(board, user_player):
		return -10

	elif is_draw(convert_board(board)):
		return 0

	moves = []

	for player_move in possible_moves:
		move = {
			'index': player_move
		}

		board[player_move] = player
		
		if player is server_player:
			result = minimax(board, user_player)

			if type(result) is int:
				move['score'] = result

			elif type(result) is dict:
				move['score'] = result['score']

		else:
			result = minimax(board, server_player)

			if type(result) is int:
				move['score'] = result

			elif type(result) is dict:
				move['score'] = result['score']

		board[player_move] = move['index']
		moves.append(move)

	# get and return the best move
	if player is server_player:
		best_score = -10000

		for count, move in enumerate(moves):

			if move['score'] > best_score:
				best_score = move['score']
				best_move = count

	else:
		best_score = 10000

		for count, move in enumerate(moves):

			if move['score'] < best_score:
				best_score = move['score']
				best_move = count

	return moves[best_move]


def play_move(board, move):
	"""
	server plays in the index sent
	returns the board with the play
	"""
	board_copy = list(board)

	board_copy[move] = 'o'
	return ''.join(board_copy)


def server_play(board):
	"""
	Server plays
	returns the response which contains
		the board with the servers play
	"""
	best_move = minimax(convert_board(board), server_player)['index']
	server_move = play_move(board, best_move)

	if server_move:

		# check if server has won the current game
		if is_game_won(server_move, server_player):
			return response(
				'Player o has won the game.',
				server_move,
				200
			)

		# check if user player has won the current game
		elif is_game_won(server_move, user_player):
			return response(
				'Player x has won the game.',
				server_move,
				200
			)

		# check if the current game is a draw
		elif is_draw(convert_board(server_move)):
			return response(
				'Draw!!!',
				server_move,
				200
			)

		# next turn
		else:
			return response(
				'Your turn',
				server_move,
				200
			)

	
