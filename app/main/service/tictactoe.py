from flask import jsonify
from app.main.utils.validation import board_is_valid
from app.main.utils.game import is_game_won, random_move, is_draw, server_play, convert_board
from app.main.utils.helpers import response

def play_game(request):
    """Let's play tic tac toe"""
    try:
        board = request.args.get('board').lower()

        # validate board is valid
        if board_is_valid(board):
            user_player = is_game_won(board, 'x')
            server_player = is_game_won(board, 'o')

            # check whether the player or the server has won the current game
            if user_player:
                return response(
                    'Player x has won the game!!!',
                    board,
                    200
                )

            elif server_player:
                return response(
                    'Player o has won the game!!!',
                    board,
                    200
                )

            # check if current board is a draw
            elif is_draw(convert_board(board)):
                return response(
                    'Draw!!!',
                    board,
                    200
                )

            # the server plays
            else:
                return server_play(board)

        # invalid board response
        else:
            return response(
                    'invalid board',
                    board,
                    400
                )

    except:
        return response(
                    "Let's play Tic-Tac-Toe",
                    '         ',
                    200
                )
        
