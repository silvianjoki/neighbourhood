from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood, Business, Admin, Post

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

class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.silvia = User(username = 'silvia',  email ='silvia@gmail.com', n_name='nairobi', profile_id='21882')
        self.profile = Profile(user=self.silvia, name='sivia', email='silvia@gmail.com', profile_id='21882')
        self.neighbourhood = Neighbourhood(n_name='nairobi', location='kenya', occupants='10000', admin='self.admin')
        
        self.silvia.save()
        self.profile.save_profile
        self.neighbourhood.save_neighbourhood

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_save_neighbourhood(self):
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood)>0)

    def test_delete_neighbourhood(self):
        neighbourhood1 = Neighbourhood.objects.all()
        self.assertEqual(len(neighbourhood1),1)
        self.neighbourhood.delete_project()
        neighbourhood2 = Neighbourhood.objects.all()
        self.assertEqual(len(neighbourhood2),0)
        
    def test_search_neighbourhood(self):
        neighbourhood = Neighbourhood.search_neighbourhood('testing')
        self.assertEqual(len(neighbourhood),1)
    
    def test_display_neighbourhood(self):
        neighbourhood = Neighbourhood.display_all_neighbourhood()
        self.assertTrue(len(neighbourhood) > 0)
        
    def test_get_user_neighbourhood_(self):
        profile_projects = Neighbourhood.get_user_projects(self.profile.id)
        self.assertEqual(profile_projects[0].name, 'testing')
        self.assertEqual(len(profile_projects),1 )

class BusinessTestCase(TestCase):
    def setUp(self):
        self.silvia = User(username = 'silvia',  email ='silvia@gmail.com', n_name='nairobi', profile_id='21882')
        self.profile = Profile(user=self.silvia, name='sivia', email='silvia@gmail.com', profile_id='21882')
        self.neighbourhood = Neighbourhood(n_name='nairobi', location='kenya', occupants='10000', admin='self.admin')
        self.business = Business(name='biashara', user='self.user', n_name='self.neighbourhood', email='silvia@gmail.com')
        
        self.silvia.save()
        self.profile.save_profile()
        self.neighbourhood.save_neighbourhood
        
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Business.objects.all().delete()
        
    def test_business_instance(self):
        self.assertTrue(isinstance(self.business, Business))
        
    def test_save_business(self):
        business = Business.objects.all()
        self.assertTrue(len(business)>0)
        
    def test_delete_business(self):
        business1 = Business.objects.all()
        self.assertEqual(len(business1),1)
        self.business.delete_business()
        business2 = Business.objects.all()
        self.assertEqual(len(business2),0)
        
class AdminTestCase(TestCase):
    def setUp(self):
        self.silvia = User(username = 'silvia',  email ='silvia@gmail.com', n_name='nairobi', profile_id='21882')
        self.profile = Profile(user=self.silvia, name='sivia', email='silvia@gmail.com', profile_id='21882')
        self.neighbourhood = Neighbourhood(n_name='nairobi', location='kenya', occupants='10000', admin='self.admin')
        self.business = Business(name='biashara', user='self.user', n_name='self.neighbourhood', email='silvia@gmail.com')
        self.admin= Admin(user='administrator', name='admin', profile_pic='image3')
        
        self.silvia.save()
        self.profile.save_profile()
        
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Business.objects.all().delete()
        Admin.objects.all().delete()
        
    def test_admin_instance(self):
        self.assertTrue(isinstance(self.admin, Admin))
        
    