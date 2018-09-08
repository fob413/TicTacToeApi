from flask import jsonify
from app.main.utils.validation import board_is_valid

def play_game(request):
    """Let's play tic tac toe"""
    board = request.args.get('board')

    if board_is_valid(board):
        response_object = {
            'message': 'successfully hit this endpoint to play the game'
        }

        return response_object, 200

    else:
        response_object = {
            'message': 'invalid board'
        }

        return response_object, 400
