from django.test import TestCase
from ..models import User
from campus.models import Campus, Roles
from campus.utils import roles
from courses.models import Courses
from classes.models import Classes


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
                
        cls.dict_campus = {"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"}
        cls.campus = Campus.objects.create(**cls.dict_campus)
        
        cls.dict_course = {"title": "9º ano", "campus": cls.campus}
        cls.course = Courses.objects.create(**cls.dict_course)
        
        cls.dict_classe = {"title": "Turma 1135", "courses": cls.course}
        cls.classe = Classes.objects.create(**cls.dict_classe)
        
        for role in roles:
            Roles.objects.create(title=role['title'], permission=role['permission'], campus=cls.campus)
        

    def test_db_create_owner(self):
        dict_owner_user = {
            "username": "owner",
            "password": "s3nh4s3gur4",
            "first_name": "Owner",
            "last_name": "Special One",
            "email": "owner.special@mail.com",
            "cellphone": "11999999999"
        }
        self.owner_user = User.objects.create_user(**dict_owner_user)
        get_owner_user = User.objects.all()[0]
        self.assertEqual(get_owner_user, self.owner_user)

    def test_create_user_with_no_username(self):
        dict_secondu_owner_error = {
            "username": None,
            "password": "s3nh4s3gur4",
            "first_name": "Owner_two",
            "last_name": "Special Two",
            "email": "owner2error.special@mail.com",
            "cellphone": "11999999998"
        }
        with self.assertRaises(ValueError):
            User.objects.create_user(**dict_secondu_owner_error)
    
    def test_create_admin(self):
        role_admin = Roles.objects.get(title="admin", campus=self.campus)
        dict_admin_user = {
            "first_name": "Admin",
		    "last_name": "Admin",
		    "username": "admin.um",
            "email": "admin@mail.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11777777777",
		    "role": role_admin
        }
        self.admin = User.objects.create_user(**dict_admin_user)
        compare_admin = User.objects.get(email=dict_admin_user['email'])
        self.assertEqual(compare_admin, self.admin)

        
    def test_create_admin_role_invalid(self):
        dict_admin_2_user = {
            "first_name": "Admin2",
		    "last_name": "Admin2",
		    "username": "admin.two",
            "email": "admin.2@mail.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11777777772",
		    "role": 0
        }
        with self.assertRaises(ValueError):
            self.admin2 = User.objects.create_user(**dict_admin_2_user)
            
    def test_create_teacher(self):
        role_teacher = Roles.objects.get(title="teacher", campus=self.campus)
        dict_teacher = {
            "first_name": "Professor",
            "last_name": "Primeiro Cadastrado",
            "username": "prof.um",
            "email": "prof.um@mail.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11777777777",
            "role": role_teacher
        }
        self.teacher = User.objects.create_user(**dict_teacher)
        compare_teacher = User.objects.get(email=dict_teacher['email'])
        self.assertEqual(compare_teacher, self.teacher)
        
        
    def test_create_assistant(self):
        role_assistant = Roles.objects.get(title="assistant class", campus=self.campus)
        dict_assistant = {
            "first_name": "Georgian",
            "last_name": "De Arrascaeta",
            "username": "A14.flamengo",
            "email": "arrascaeta@exemplo.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11900000084",
		    "classe": self.classe,
            "role": role_assistant
        }
        self.assistant = User.objects.create_user(**dict_assistant)
        compare_assistant = User.objects.get(email=dict_assistant['email'])
        self.assertEqual(compare_assistant, self.assistant)
        
    def test_create_studant(self):
        role_studant = Roles.objects.get(title="studant", campus=self.campus)
        dict_studant = {
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "username": "cr7.allhillal",
            "email": "cristiano.ronaldo@exemplo.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11900000088",
            "classe": self.classe,
            "role": role_studant
        }
        self.studant = User.objects.create_user(**dict_studant)
        compare_studant = User.objects.get(email=dict_studant['email'])
        self.assertEqual(compare_studant, self.studant)
        