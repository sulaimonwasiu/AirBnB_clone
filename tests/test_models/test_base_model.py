#!/usr/bin/python3
import sys
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(
            obj_dict['created_at'],
            self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            obj_dict['updated_at'],
            self.base_model.updated_at.isoformat()
        )

    def test_init_with_kwargs(self):
        kwargs = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'name': 'Test Model',
            'value': 10
        }
<<<<<<< HEAD
        model = BaseModel(**kwargs) 
=======
        model = BaseModel(**kwargs)
>>>>>>> b63a81e9a4422163977621f10b511720e4ac1c0b
        self.assertEqual(model.id, '123')
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.value, 10)
        self.assertEqual(str(model.created_at), '2022-01-01 12:00:00')
        self.assertEqual(str(model.updated_at), '2022-01-02 12:00:00')

    def tearDown(self):
        del self.base_model


if __name__ == '__main__':
    unittest.main()
