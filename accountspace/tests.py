from django.test import TestCase
from django.test import Client

from .forms import BewerberSignUpForm


class RegisterTest(TestCase):

    def test_valid_data(self):
        form = BewerberSignUpForm({
            'first_name': "Max",
            'last_name': "Mustermann",
            'username': "max@mustermann.de",
            "password1": "mama-mia123",
            "password2": "mama-mia123",
            'street': "Musterstr.1",
            'city': "Musterstadt",
            'post_code': "123456",
            'phone': "0800666666",
        })

        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.first_name, "Max")

    def test_blank_data(self):
        form_data = {}
        form = BewerberSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())


class LogInTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_direct_access(self):
        response = self.client.get('/viewapplications')
        self.assertEqual(response.status_code, 302)

