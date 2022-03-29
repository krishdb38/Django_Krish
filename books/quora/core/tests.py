from django.test import TestCase
from .models import User

# Create your tests here.
class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username':'demo',
            'email':'demo@example.com',
            'password':'secret',
            'first_name':'demo',
            'last_name':'demo',
        }
        User.objects.create(**self.credentials)
        
    def test_register(self):
        response = self.client.post('/core/register/', self.credentials, follow=True)
        self.assertEquals(response.status_code, 200)
        
    def test_user(self):
        user = User.objects.get(username ='demo')
        self.assertEqual(user.username, 'demo')