import unittest
import os
import requests

class FlaskTests(unittest.TestCase):
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		pass
	def tearDown(self):
		pass

	#test if the site respond 
	def test_a_interface(self):
		response = requests.get('http://localhost:5000')
		self.assertEqual(response.status_code,200)
	
	#test positive txt
	def test_c_submit_positive_txt(self):
		txt={"txt": "good","form_type":"submit_txt"}
		response = requests.post('http://localhost:5000',data=txt)
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content,'Positive'.encode())
	
	#test negative txt
	def test_d_submit_negative_txt(self):
		txt={"txt": "bad","form_type":"submit_txt"}
		response = requests.post('http://localhost:5000',data=txt)
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content,'Negative'.encode())

if __name__=='__main__':
	unittest.main()

