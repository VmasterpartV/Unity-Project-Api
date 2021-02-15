from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Player, Clan

class ProjectTests(APITestCase):
    def setUp(self):

        # create divisions
        spartan = Clan.objects.create(name='Spartan')
        # TODO: create more divisions

        # create users
        admin_user = Player.objects.create(
            email= 'admin@admin.com',
            username= 'masterpart',
            first_name='Ivan',
            last_name='Mota',
            clan=spartan,
        )
        admin_user.set_password('12345')
        admin_user.save()

        # TODO: create more users...

    def test_something(self):
        data = { 'username': 'masterpart', 'password': '12345' }
        response = self.client.post('/api/auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.json()['access']
        print(token)

    def tests_users(self):
        response = self.client.get('/api/players/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        #self.client.login(username)
