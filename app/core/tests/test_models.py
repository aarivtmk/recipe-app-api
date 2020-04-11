from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with email is successful"""
        email = 'aariv@gmail.com'
        password = 'begainer'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the new user email is normalized"""
        email = 'aariv@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'begainer')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'begainer')

    def test_create_new_superuser(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'aariv@gmail.com',
            'begainer')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
