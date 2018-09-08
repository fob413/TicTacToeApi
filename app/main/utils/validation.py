def board_is_present(board):
	"""validate user sent a board"""
	if board:
		return True
	else:
		return False



def validate_length(board):
	"""validate length of the board"""
	if len(board) is 9:
		return True
	else:
		return False


def validate_characters(board):
	"""validate player and servers characters"""
	allowed_characters = set('xo ')
	if set(board).issubset(allowed_characters):
		return True
	else:
		return False


def validate_turn(board):
	"""validate who's turn is next"""
	server_play = board.count('o')
	user_play = board.count('x')
	difference = abs(user_play - server_play)

	if difference is 0 or difference is 1:
		return True
	else:
		return False



def board_is_valid(board):
	"""validate board is valid"""
	if (board_is_present(board) and
		validate_length(board) and
		validate_characters(board) and
		validate_turn(board)):
		return True
	else:
		return False