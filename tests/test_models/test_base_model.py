import unittest
from datetime import datetime
from models import *


class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        self.model1 = BaseModel()

        test_args = self.model1.to_dict()
        self.model2 = BaseModel(**test_args)
        print(self.model1.id)
        print(self.model2.id)

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.assertDictEqual(self.model1.to_dict(), self.model2.to_dict())


if __name__ == "__main__":
    unittest.main()
