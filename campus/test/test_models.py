from django.test import TestCase
from ..models import Campus, Roles
from campus.utils import roles
from django.db.utils import IntegrityError


class CampusModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dict_campus = {"title": "Colégio Nova Iguaçu", "adress": "R. Iguaçuano , 1"}
        cls.campus = Campus.objects.create(**cls.dict_campus)

    def test_db_create_campus(self):
        campus_2 = Campus.objects.create(**{"title": "Colégio Nova Geração", "adress": "R. Geração , 1000"})
        campus_compare = Campus.objects.get(title=campus_2.title)
        self.assertEqual(campus_compare, campus_2)

    def test_roles_to_campus(self):
        for role in roles:
            Roles.objects.create(title=role['title'], permission=role['permission'], campus=self.campus)
        
        role_owner = Roles.objects.get(title="owner", campus=self.campus)
        role_admin = Roles.objects.get(title="admin", campus=self.campus)
        role_teacher = Roles.objects.get(title="teacher", campus=self.campus)
        role_assistant = Roles.objects.get(title="assistant class", campus=self.campus)
        role_studant = Roles.objects.get(title="studant", campus=self.campus)
        role_no_authorized = Roles.objects.get(title="no authorized", campus=self.campus)
        
        self.assertEqual(role_owner.permission, 9)
        self.assertEqual(role_admin.permission, 7)
        self.assertEqual(role_teacher.permission, 5)
        self.assertEqual(role_assistant.permission, 3)
        self.assertEqual(role_studant.permission, 1)
        self.assertEqual(role_no_authorized.permission, 0)

        
    def test_db_create_campus_invalid_title(self):
        with self.assertRaises(IntegrityError):
            Campus.objects.create(**{"title": None, "adress": "R. Teste , 5000"})
        
    def test_db_create_course_with_course_invalid(self):
        with self.assertRaises(IntegrityError):
            Campus.objects.create(**{"title": "Colégio Teste", "adress": None})