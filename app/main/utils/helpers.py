def response(message, board, status):
	"""
	returns the response object, with the parameters sent
	xoxxoooxx
	"""
	return {
		'message': message,
		'board': board,
	}, status


possible_moves = [
	[[0, 1], 2],
	[[1, 2], 0],
	[[0, 2], 1],
	[[3, 4], 5],
	[[4, 5], 3],
	[[3, 5], 4],
	[[6, 7], 8],
	[[7, 8], 6],
	[[6, 8], 7],
	[[0, 3], 6],
	[[3, 6], 0],
	[[0, 6], 3],
	[[1, 4], 7],
	[[4, 7], 1],
	[[1, 7], 4],
	[[2, 5], 8],
	[[5, 8], 2],
	[[2, 8], 5],
	[[0, 4], 8],
	[[4, 8], 0],
	[[0, 8], 4],
	[[2, 4], 6],
	[[4, 6], 2],
	[[2, 6], 4],
]