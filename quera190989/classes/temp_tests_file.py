from django.test import TestCase
from classes.models import Classroom
from classes.serializers import ClassroomSerializer


class SerializerTest(TestCase):
    # tests
    def test_valid_data1(self):
        data = {
            'capacity': 5,  # Minimum allowed capacity
            'name': 'Room1',
            'department': 'main',
            'area': 10,  # A positive number
        }
        serializer = ClassroomSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_valid_data2(self):
        data = {
            'capacity': 5,  # Minimum allowed capacity
            'name': 'Room1',
            'department': 'main',
            'area': 0, 
        }
        serializer = ClassroomSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_capacity(self):
        data = {
            'capacity': 2,  # Less than minimum allowed capacity
            'name': 'Room2',
            'department': 'lab',
            'area': 15,  # A positive number
        }
        serializer = ClassroomSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_area1(self):
        data = {
            'capacity': 20,  # Valid capacity
            'name': 'Room3',
            'department': 'store',
            'area': -0.015,  # A negative number
        }
        serializer = ClassroomSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_area2(self):
        data = {
            'capacity': 20,  # Valid capacity
            'name': 'Room3',
            'department': 'store',
            'area': 10.15,  # positive but with floating point
        }
        serializer = ClassroomSerializer(data=data)
        self.assertFalse(serializer.is_valid())
