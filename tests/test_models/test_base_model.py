#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ test model: base_model  """
    def setUp(self):
        """ standard setUp() """
        self.model = BaseModel()

    def test_name_number(self):
        """ test name and number """
        self.model.name = "my_school"
        self.model.my_number = 89
        self.assertEqual(self.model.name, "my_school")
        self.assertEqual(self.model.my_number, 89)

    def test_public_attr(self):
        """ id (uuid), created_at (datetime), updated_at (datetime) """
        self.assertEqual(self.model.__class__.__name__, "BaseModel")
        self.assertFalse(hasattr(self.model, "name"))
        self.assertFalse(hasattr(self.model, "my_number"))
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_save(self):
        """ save  """
        self.model.save()


if __name__ == "__main__":
    unittest.main()
