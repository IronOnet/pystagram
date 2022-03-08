from django.test import TestCase
from app.models import User

class UserTestSuite(TestCase): 

    def test_create_user(self): 
        user_data = {
            'name': 'john', 
            'last_name': 'doe', 
            'email': 'johndoe123@somemail.com', 
            'password': 'password123'
        }

        user = User.objects.create(user_data)
        self.assertEqual(user_data, user.get_data())

    def test_update_user(self): 
        user_data1 = {
            'name': 'john', 
            'last_name': 'doe', 
            'email': 'johndoe123@somemail.com', 
            'password': 'password123'
        }

        user_data2 = {
            'name': 'robert', 
            'last_name': 'sampson', 
            'email': 'johndoe123@somemail.com', 
            'password': 'password123'
        }

        user_1 = User.objects.create(user_data1) 
        user_1 = User.objects.update_or_create(user_data2) 
        self.assertNotEqual(user_1.data, user_data1)

    def test_delete_user(self): 
        pass 

    def test_get_user(self): 
        pass

class UploadPhotoTestSuite(TestCase): 
    
    def test_like_post(self): 
        pass 

    def test_comment_post(self): 
        pass 

    def test_create_post(self): 
        pass 

    def test_update_post(self):
        pass 

    def test_delete_post(self): 
        pass 

