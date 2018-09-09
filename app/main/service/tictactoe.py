from flask import jsonify
from app.main.utils.validation import board_is_valid
from app.main.utils.game import is_game_won, random_move

def play_game(request):
    """Let's play tic tac toe"""
    board = request.args.get('board').lower()

    if board_is_valid(board):
        user_player = is_game_won(board, 'x')
        server_player = is_game_won(board, 'o')

        if user_player['won']:
            response_object = {
                'message': 'Congratulations, you have won the game!!!',
                'board': board
            }

            return response_object, 200

        elif server_player['won']:
            response_object = {
                'message': 'Sorry, the computer has won this game!!!',
                'board': board
            }

            return response_object, 200
        else:
            response_object = {
                'message': 'successfully hit this endpoint to play the game',
                'board': random_move(board)
            }

            return response_object, 200

    else:
        response_object = {
            'message': 'invalid board'
        }

        return response_object, 400
