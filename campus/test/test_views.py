from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token


class CampusViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client: APIClient;
        
        dict_owner_user = {
            "username": "owner",
            "password": "s3nh4s3gur4",
            "first_name": "Owner",
            "last_name": "Special One",
            "email": "owner.special@mail.com",
            "cellphone": "11999999999"
        }
        cls.owner = User.objects.create_user(**dict_owner_user)
        cls.token = Token.objects.create(user=cls.owner).key
        cls.base_create_campus_url = reverse("campus-list-create-view")


    def test_create_campus_with_invalid_token(self):
        test_request = {"title": "Colégio Token Inválido", "adress": "R. Token Inválido , 011"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'Invalid')
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        response = self.client.post(self.base_create_campus_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)        
    
    def test_empty_create_campus(self):
        test_request = {}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_400_BAD_REQUEST
        response = self.client.post(self.base_create_campus_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)
        
    def test_create_campus(self):
        test_request = {"title": "Colégio Novo Teste", "adress": "R. Iguaçuano , 1"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_201_CREATED
        response = self.client.post(self.base_create_campus_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)