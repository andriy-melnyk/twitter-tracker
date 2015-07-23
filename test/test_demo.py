import unittest
from app import demo

class TestDemo(unittest.TestCase):
	def test_demo(self):
		demo.app.config.from_object('config.demo')
		self.test_app = demo.app.test_client()
		response = self.test_app.get('/')
		self.assertEquals(response.status, '200 OK')
		self.assertEquals(response.headers['Content-Type'], "text/html; charset=utf-8")
		self.assertEquals(response.data, 'Hello World!')