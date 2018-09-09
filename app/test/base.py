from app import create_app
from flask_testing import TestCase


class BaseTestCase(TestCase):

	def create_app(self):
		"""Create the app and specify the testing environment"""
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.client = self.app.test_client()
		return self.app