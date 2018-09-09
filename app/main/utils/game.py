import random

from app.main.utils.helpers import response, possible_moves


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


def defense_win_play(possible_moves, board):
	"""
	Server blocks a possible user win or
	plays in a possible server win
	return boolean of possible_win with the current board
	"""
	board_copy = list(board)
	server_move = {
		'played': False,
		'board': ''.join(board_copy)
	}

	# block possible user win
	for move in possible_moves:
		if board_copy[move[0][0]] == board_copy[move[0][1]] == 'x':
			# validate the possible move
			if board_copy[move[1]] != ' ':
				continue

			board_copy[move[1]] = 'o'
			server_move['played'] = True
			server_move['board'] = ''.join(board_copy)
			return server_move

	# server possible win
	for move in possible_moves:
		if board_copy[move[0][0]] == board_copy[move[0][1]] == 'o':
			# validate the possible move
			if board_copy[move[1]] != ' ':
				continue

			board_copy[move[1]] = 'o'
			server_move['played'] = True
			server_move['board'] = ''.join(board_copy)
			return server_move

	return server_move


def server_play(board):
	"""
	Server plays
	returns the response which contains
	the board with the servers play
	"""

	server_move = defense_win_play(possible_moves, board)

	if server_move['played']:
		# check if server has won the current game
		if is_game_won(server_move['board'], 'o')['won']:
			return response(
				'Player o has won the game!!!',
				server_move['board'],
				200
			)

		# check if current board is a draw
		elif is_draw(server_move['board']):
			return response(
				'Draw!!!',
				server_move['board'],
				200
			)

		else:
			return response(
				'Your turn',
				server_move['board'],
				200
			)

	else:
		# random server play
		random_server_play = random_move(board)

		# check if server has won the current game
		if is_game_won(random_server_play, 'o')['won']:
			return response(
				'Player ' + is_game_won(random_server_play, 'o')['player'] + ' has won the game!!!',
				random_server_play,
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
