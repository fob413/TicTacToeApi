from flask import jsonify
from app.main.utils.validation import board_is_valid
from app.main.utils.game import is_game_won, random_move

def play_game(request):
    """Let's play tic tac toe"""
    try:
        board = request.args.get('board').lower()

        if board_is_valid(board):
            user_player = is_game_won(board, 'x')
            server_player = is_game_won(board, 'o')

            # check whether the player or the server has won the current game
            if user_player['won']:
                response_object = {
                    'message': 'Player ' + user_player['player'] + ' has won the game!!!',
                    'board': board
                }

                return response_object, 200

            elif server_player['won']:
                response_object = {
                    'message': 'Player ' + server_player['player'] + ' has won the game!!!',
                    'board': board
                }

                return response_object, 200

            # the server plays
            else:
                response_object = {
                    'message': 'Your turn',
                    'board': random_move(board)
                }

                return response_object, 200

        else:
            response_object = {
                'message': 'invalid board'
            }

            return response_object, 400

    except:
        response_object = {
            'message': "Let's play Tic-Tac-Toe"
        }

        return response_object, 200
