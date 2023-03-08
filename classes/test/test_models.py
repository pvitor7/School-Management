from django.test import TestCase
from campus.models import Campus
from courses.models import Courses
from ..models import Classes
from django.db.utils import IntegrityError

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dict_campus = {"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"}
        cls.campus = Campus.objects.create(**cls.dict_campus)
        
        cls.dict_course = {"title": "9º ano", "campus": cls.campus}
        cls.course = Courses.objects.create(**cls.dict_course)
        

    def test_db_create_classe(self):
        classe_2 = Classes.objects.create(**{"title": "Turma 1135", "courses": self.course})
        classe_compare = Classes.objects.get(title=classe_2.title)
        self.assertEqual(classe_compare, classe_2)
        
    
    def test_db_create_classe_with_title_invalid(self):
        with self.assertRaises(IntegrityError):
            Classes.objects.create(**{"title": None, "courses": self.course})
            
    def test_db_create_classe_with_course_invalid(self):
        with self.assertRaises(ValueError):
            Classes.objects.create(**{"title": "Turma 1000", "courses": "0"})
    
    
    def test_db_relations(self):
        campus = Campus.objects.create(**{"title": "Campus Test Classe", "adress": "R. Test Classe , 1"})
        relation_course = Courses.objects.create(**{"title": f"Test Course", "campus": campus})
        for x in range(5):
            classe = Classes.objects.create(**{"title": f"Test Classe {x}", "courses": relation_course})
            self.assertEqual(classe.courses, relation_course)
        
        count_classes = Classes.objects.filter(courses=relation_course).count()
        self.assertEqual(count_classes, 5)
    
    