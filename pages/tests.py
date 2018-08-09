from django.test import SimpleTestCase

# Create your tests here.
class SImpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/') 
        print("test_home_page_status_code: ", response)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/') 
        print("test_about_page_status_code: ", response)
        self.assertEqual(response.status_code, 200)

