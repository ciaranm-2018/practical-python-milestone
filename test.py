from run import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # Ensure that the home page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Enter' in response.data)
    
    # Ensure that leaderboard page loads correctly
    def test_records(self):
        tester = app.test_client(self)
        response = tester.get('records', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    # Ensure that contact page loads correctly
    def test_contact(self):
        tester = app.test_client(self)
        response = tester.get('contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
     # Ensure that the contact page requires data entry
    def test_contact_route_requires_name(self):
        tester = app.test_client(self)
        response = tester.get('contact', follow_redirects=True)
        self.assertTrue(b'Please' in response.data)
        
if __name__ == '__main__':
    unittest.main()