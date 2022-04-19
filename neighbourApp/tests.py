from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood, Business, Admin

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.silvia= User(username = 'silvia',  email ='silvia@gmail.com', n_name='nairobi', profile_id='21882' )
        self.profile = Profile(user=self.silvia, name='sivia', email='silvia@gmail.com', profile_id='21882')
        self.silvia.save()
        self.profile.save_profile()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.silvia,User))
        self.assertTrue(isinstance(self.silvia,Profile))

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        
