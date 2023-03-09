from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import User
from campus.utils import roles
from campus.models import Campus, Roles
from courses.models import Courses
from classes.models import Classes
from django.urls import reverse
from rest_framework.authtoken.models import Token


class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client: APIClient;
        cls.campus = Campus.objects.create(**{"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"})
        cls.course = Courses.objects.create(**{"title": "9º ano", "campus": cls.campus})
        cls.classe = Classes.objects.create(**{"title": "Turma 1135", "courses": cls.course})
        
        cls.dict_owner = {
            "username": "owner",
            "password": "s3nh4s3gur4",
            "first_name": "Owner",
            "last_name": "Special One",
            "email": "owner.special@mail.com",
            "cellphone": "11999999999"
            }
        
        cls.dict_admin = {
            "first_name": "Admin",
		    "last_name": "Admin",
		    "username": "admin.um",
            "email": "admin@mail.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11777777777",
		    "role": ''
            }
        
        cls.teacher = {
            "first_name": "Professor",
            "last_name": "Primeiro Cadastrado",
            "username": "prof.um",
            "email": "prof.um@mail.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11777777777"
            }
        
        cls.assistant_class = {
            "first_name": "Assistant",
            "last_name": "Primeiro Cadastrado",
            "username": "assistant.um",
            "email": "assistant.um@mail.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11777777775"
            }

        cls.studant = {
            "first_name": "Studant",
            "last_name": "Studant Cadastrado",
            "username": "studant.um",
            "email": "assistant.um@mail.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11777777774"
            }

        cls.base_create_user_url = reverse("user-create-view")
        cls.base_login_url = reverse("login-view")
        cls.base_user_retrive_url = reverse("user-retrive-view", kwargs={'pk': cls.dict_owner})
        cls.base_list_users_url = reverse("list-users-view")
        
        for role in roles:
            Roles.objects.create(title=role['title'], permission=role['permission'], campus=cls.campus)
        
    
    def test_empty_create_user(self):
        test_request = {}
        expected_status_code = status.HTTP_400_BAD_REQUEST
        response = self.client.post(self.base_create_user_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)
        
    def test_create_user_owner(self):
        expected_status_code = status.HTTP_201_CREATED
        response = self.client.post(self.base_create_user_url, self.dict_owner);
        self.assertEquals(response.status_code, expected_status_code)
        
    def test_login_username_owner(self):
        self.client.post(self.base_create_user_url, self.dict_owner);
        login = {"username": self.dict_owner['username'], 'password': self.dict_owner['password']}
        expected_status_code = status.HTTP_200_OK
        response = self.client.post(self.base_login_url, login)
        self.assertEquals(response.status_code, expected_status_code)
        
    
    def test_create_user_admin(self):
        owner_created = User.objects.create_user(**self.dict_owner);
        User.objects.filter(email=owner_created.email).update(role=Roles.objects.get(title='owner'))
        
        login = {"username": self.dict_owner['username'], 'password': self.dict_owner['password']}
        response = self.client.post(self.base_login_url, login)
        token = response.data['token'];
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.dict_admin['role'] = Roles.objects.get(title="admin").id
        response = self.client.post(self.base_create_user_url, self.dict_admin);
        
        expected_status_code = status.HTTP_201_CREATED
        self.assertEquals(response.status_code, expected_status_code)
        
        
    def test_create_user_teacher(self):
        owner_created = User.objects.create_user(**self.dict_owner);
        User.objects.filter(email=owner_created.email).update(role=Roles.objects.get(title='owner'))
        login = {"username": self.dict_owner['username'], 'password': self.dict_owner['password']}
        response = self.client.post(self.base_login_url, login)
        token = response.data['token'];
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.dict_admin['role'] = Roles.objects.get(title="admin").id
        response = self.client.post(self.base_create_user_url, self.dict_admin);
        
        expected_status_code = status.HTTP_201_CREATED
        self.assertEquals(response.status_code, expected_status_code)
        
        
    def test_create_user_assistant_class(self):
        owner_created = User.objects.create_user(**self.dict_owner);
        User.objects.filter(email=owner_created.email).update(role=Roles.objects.get(title='owner'))
        login = {"username": self.dict_owner['username'], 'password': self.dict_owner['password']}
        response = self.client.post(self.base_login_url, login)
        token = response.data['token'];
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.assistant_class['role'] = Roles.objects.get(title="assistant class").id
        self.assistant_class['classe'] = Classes.objects.all()[0].id
        response = self.client.post(self.base_create_user_url, self.assistant_class);
        
        expected_status_code = status.HTTP_201_CREATED
        self.assertEquals(response.status_code, expected_status_code)
        

    def test_create_user_studant(self):
        owner_created = User.objects.create_user(**self.dict_owner);
        User.objects.filter(email=owner_created.email).update(role=Roles.objects.get(title='owner'))
        login = {"username": self.dict_owner['username'], 'password': self.dict_owner['password']}
        response = self.client.post(self.base_login_url, login)
        token = response.data['token'];
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.studant['role'] = Roles.objects.get(title="studant").id
        self.studant['classe'] = Classes.objects.all()[0].id
        response = self.client.post(self.base_create_user_url, self.studant);
        
        expected_status_code = status.HTTP_201_CREATED
        self.assertEquals(response.status_code, expected_status_code)