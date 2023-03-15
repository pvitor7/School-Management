from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from campus.models import Campus, Roles
from courses.models import Courses
from classes.models import Classes
from campus.utils import roles
from django.urls import reverse
from rest_framework.authtoken.models import Token


class CoursesViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client: APIClient;
        
        cls.campus = Campus.objects.create(**{"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"})
        cls.course = Courses.objects.create(**{"title": "9º ano", "campus": cls.campus})
        cls.classe_test = Classes.objects.create(**{"title": "Turma 0001", "courses": cls.course})
        
        for role in roles:
            Roles.objects.create(title=role['title'], permission=role['permission'], campus=cls.campus)
        role_admin = Roles.objects.get(title="admin", campus=cls.campus)
        
        dict_owner_user = {
            "username": "owner",
            "password": "s3nh4s3gur4",
            "first_name": "Owner",
            "last_name": "Special One",
            "email": "owner.special@mail.com",
            "cellphone": "11999999999",
            "role": role_admin
        }
                
        cls.owner = User.objects.create_user(**dict_owner_user)
        cls.token = Token.objects.create(user=cls.owner).key
        cls.base_list_create_classes_url = reverse("classes-list-create-view", kwargs={'campus_id': cls.campus.id, 'course_id': cls.course.id})
        cls.base_id_classes_url = reverse("classes-retrive-view", kwargs={'campus_id': cls.campus.id, 'course_id': cls.course.id, 'pk': cls.classe_test.id})


    def test_create_classe_with_invalid_token(self):
        test_request = {"title": "Turma 1135"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'Invalid')
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        response = self.client.post(self.base_list_create_classes_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)        
    
    def test_empty_create_classe(self):
        test_request = {}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_400_BAD_REQUEST
        response = self.client.post(self.base_list_create_classes_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)
        
        
    def test_create_classe(self):
        test_request = {"title": "Turma 1136"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_201_CREATED
        response = self.client.post(self.base_list_create_classes_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)
        
        
    def test_list_all_classes(self):
        classes_list = [
        {"title": "Turma 0001", "courses": self.course},
        {"title": "Turma 0002", "courses": self.course},
        {"title": "Turma 0003", "courses": self.course}]
        for classe in classes_list:
            Classes.objects.create(**classe)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_200_OK
        response = self.client.get(self.base_list_create_classes_url)
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(len(response.data), 4)
        
        
    def test_retrive_classe_with_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        expected_status_code = status.HTTP_200_OK
        response = self.client.get(self.base_id_classes_url)
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(response.data['title'], self.classe_test.title)
        self.assertEquals(response.data['courses'], self.course.id)
        self.assertEquals(response.data['studants'], [])