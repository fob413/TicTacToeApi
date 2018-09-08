from flask import request, jsonify
from flask_restful import Resource
from app.main.service.tictactoe import play_game


class Game(Resource):
    def get(self):
        if request.method == "GET":
            """Play Tic Tac Toe"""
            return play_game(request)
