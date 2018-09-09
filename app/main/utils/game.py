import random

from app.main.utils.helpers import response


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


def is_draw(board):
	"""
	Check if game is a draw
	"""
	user_player = is_game_won(board, 'x')
	server_player = is_game_won(board, 'o')

	if not user_player['won'] and not server_player['won']:
		draw_game = board.find(' ')
		if draw_game < 0:
			return True
		
		else:
			return False
	
	else:
		return False


def server_play(board):
	"""
	Server plays
	returns the response which contains
	the board with the servers play
	"""
	random_server_play = random_move(board)

	# check if server has won the current game
	if is_game_won(random_server_play, 'o')['won']:
		return response(
			'Player ' + is_game_won(random_server_play, 'o')['player'] + ' has won the game!!!',
			board,
			200
		)

	# check if current board is a draw
	elif is_draw(random_server_play):
		return response(
			'Draw!!!',
			random_server_play,
			200
		)

	# next turn
	else:
		return response(
			'Your turn',
			random_server_play,
			200
		)
