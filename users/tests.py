from django.test import TestCase
from rest_framework.test import APIClient
from pprint import pprint
client = APIClient()


class StudentTestCase(TestCase):
    def setUp(self):
        
        pass
    def test_get_students(self):
        response = client.get('/api/users/students/')
        pprint(response.data)
        assert response.status_code == 200
    def test_get_single_students(self):
        response = client.get('/api/users/students/1/')
        pprint(response.data)
        assert response.status_code == 200
