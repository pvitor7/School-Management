from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from campus.models import Campus
from django.urls import reverse
from rest_framework.authtoken.models import Token


class CoursesViewTest(APITestCase):
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
        
        cls.campus = Campus.objects.create(**{"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"})
        
        cls.owner = User.objects.create_user(**dict_owner_user)
        cls.token = Token.objects.create(user=cls.owner).key
        cls.base_create_courses_url = reverse("courses-list-create-view", kwargs={'campus_id': cls.campus.id})


    def test_create_course_with_invalid_token(self):
        test_request = {"title": "9º ano"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'Invalid')
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        response = self.client.post(self.base_create_courses_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)        
    
    def test_empty_create_course(self):
        test_request = {}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_400_BAD_REQUEST
        response = self.client.post(self.base_create_courses_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)
        
    def test_create_course(self):
        test_request = {"title": "8º ano"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_201_CREATED
        response = self.client.post(self.base_create_courses_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)