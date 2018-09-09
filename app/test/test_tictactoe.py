import unittest
import os
from app.test.base import BaseTestCase
from app import create_app


class TicTacToeTestCase(BaseTestCase):
	""""""
	def setUp(self):
		self.app = create_app('testing')
		self.client = self.app.test_client


	def test_tictactoe(self):
		"""Test the endpoint exist"""
		res = self.client().get('/')
		self.assertEqual(res.status_code, 200)

	
	def test_tictactoe_valid_board(self):
		"""Test the server plays when the board is valid"""
		res = self.client().get('/?board=+++++++++')
		self.assertEqual(res.status_code, 200)


	def test_tictactoe_invalid_board_character(self):
		"""Test the server throws an error on invalid character"""
		res = self.client().get('/?board=++++++++y')
		self.assertEqual(res.status_code, 400)


	def test_tictactoe_invalid_board_length(self):
		"""Test the server throws an error on an invalid board length"""
		res = self.client().get('/?board=++++++')
		self.assertEqual(res.status_code, 400)

	
	def test_tictactoe_invalid_board_4(self):
		"""Test the server throws an error on invalid player turns"""
		res = self.client().get('/?board=+++++++xx')
		self.assertEqual(res.status_code, 400)


	def test_tictactoe_invalid_board_5(self):
		"""Test the server throws an error on invalid player turns"""
		res = self.client().get('/?board=xxx+ooooo')
		self.assertEqual(res.status_code, 400)