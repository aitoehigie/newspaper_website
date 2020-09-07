from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    username = 'admin'
    password = 'password'
    
    def test_user_creation(self):
        user = get_user_model().objects.create_user(username=self.username, password=self.password, email='test@email.com')
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, 'test@email.com')
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)


    def test_superuser_creation(self):
        superuser = get_user_model().objects.create_superuser(username=self.username, password=self.password, email='admin@email.com')
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(superuser.username, "admin")
        self.assertEqual(superuser.email, 'admin@email.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)



