from django.test import TestCase
from campus.models import Campus, Roles
from courses.models import Courses
from ..models import Subjects, SubjectsStudants
from campus.utils import roles
from users.models import User
from classes.models import Classes
from django.db.utils import IntegrityError


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.campus = Campus.objects.create(**{"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"})
        cls.course = Courses.objects.create(**{"title": "9º ano", "campus": cls.campus})
        cls.classe = Classes.objects.create(**{"title": "Turma 1135", "courses": cls.course})
        
        for role in roles:
            Roles.objects.create(title=role['title'], permission=role['permission'], campus=cls.campus)
     
        cls.role_studant = Roles.objects.get(title="studant", campus=cls.campus)
     
        cls.studant = User.objects.create_user(**{
            "first_name": "Cristiano",
            "last_name": "Ronaldo",
            "username": "cr7.allhillal",
            "email": "cristiano.ronaldo@exemplo.com",
            "password": "s3nh4s3gur4",
            "cellphone": "11900000088",
            "classe": cls.classe,
            "role": cls.role_studant
        })
       

    def test_db_create_subject(self):
        subject = Subjects.objects.create(**{"title": "Literatura", "course": self.course})
        subject_compare = Subjects.objects.get(title=subject.title)
        self.assertEqual(subject_compare, subject)
    
        
    def test_db_create_subject_with_invalid_course(self):
        with self.assertRaises(ValueError):
            Subjects.objects.create(**{"title": "Course inválido", "course": ""})
    
        
    def test_db_create_subject_with_invalid_title(self):
        with self.assertRaises(IntegrityError):
            Subjects.objects.create(**{"title": None, "course":  self.course})
    
    
    def test_db_create_subject_studant(self):
        subject = Subjects.objects.create(**{"title": "Matemática", "course": self.course})
        studant_subject = SubjectsStudants.objects.create(**{"user": self.studant, "subject": subject, "test_1": None, "test_2": None, "test_3": None, "test_4": None})
        studant_subject_compare = SubjectsStudants.objects.get(subject=subject)
        self.assertEqual(studant_subject_compare, studant_subject)
        
    
    def test_db_create_subject_studant_with_invalid_user(self):
        self.subject = Subjects.objects.create(**{"title": "Matemática", "course": self.course})
        with self.assertRaises(ValueError):
            SubjectsStudants.objects.create(**{"user": "", "subject": self.subject, "test_1": None, "test_2": None, "test_3": None, "test_4": None})
            
    
    def test_db_create_subject_studant_with_invalid_subject(self):
        with self.assertRaises(ValueError):
            SubjectsStudants.objects.create(**{"user": self.studant, "subject": "", "test_1": None, "test_2": None, "test_3": None, "test_4": None})
    

    def teste_db_relations(self):
        relation_user = User.objects.create_user(**{
	    	"username": "Gabigol",
            "password": "s3nh4s3gur4",
            "first_name": "Gabriel",
            "last_name": "Barbosa",
            "email": "gabi.gol@mail.com",
            "cellphone": "11999999910",
            "classe": self.classe,
            "role": self.role_studant
        })
        for x in range(10):
            subject = Subjects.objects.create(**{"title": f"Test {x}", "course": self.course})
            studant_subject = SubjectsStudants.objects.create(**{"user": relation_user, "subject": subject, "test_1": 0, "test_2": 3, "test_3": 7.5, "test_4": x})
            self.assertEqual(relation_user, studant_subject.user)
            self.assertEqual(subject, studant_subject.subject)
        
        count_subjects = SubjectsStudants.objects.filter(user=relation_user).count()
        self.assertEqual(count_subjects, 10)
            
                
                
            
