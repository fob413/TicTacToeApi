import random


def is_game_won(board, player):
	"""
	checks if game is won
	returns True or False and the player that won
	"""

	is_won = {
		'won': False,
		'player': ''
	}

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
		is_won = {
			'won': True,
			'player': player
		}
	
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