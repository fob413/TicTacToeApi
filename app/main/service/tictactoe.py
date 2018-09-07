from flask import jsonify

def play_game():
    response_object = {
        'status': 'success',
        'message': 'successfully hit this endpoint to play the game'
    }

    return response_object, 200
