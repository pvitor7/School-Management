from django.test import TestCase
from campus.models import Campus
from ..models import Courses
from django.db.utils import IntegrityError


class CoursesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dict_campus = {"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"}
        cls.campus = Campus.objects.create(**cls.dict_campus)
        
        cls.dict_course = {"title": "9º ano", "campus": cls.campus}
        cls.course = Courses.objects.create(**cls.dict_course)

    def test_db_create_course(self):
        course_2 = Courses.objects.create(**{"title": "8º ano", "campus": self.campus})
        course_compare = Courses.objects.get(title=course_2.title)
        self.assertEqual(course_compare, course_2)
        
    def test_db_create_course_with_title_invalid(self):
        with self.assertRaises(IntegrityError):
            Courses.objects.create(**{"title": None, "campus": self.campus})
            
            
    def test_db_create_course_with_course_invalid(self):
        with self.assertRaises(ValueError):
            Courses.objects.create(**{"title": "5º ano", "campus": "0"})
            
    def test_db_relations(self):
        relation_campus = Campus.objects.create(**{	"title": "Colégio Test Relations",	"adress": "R. Relations , 1"})
        for x in range(5):
            course = Courses.objects.create(**{"title": f"Test Course {x}", "campus": relation_campus})
            self.assertEqual(course.campus, relation_campus)
        
        count_courses = Courses.objects.filter(campus=relation_campus).count()
        self.assertEqual(count_courses, 5)