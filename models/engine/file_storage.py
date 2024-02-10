#!/usr/bin/python3

import json
import importlib


class FileStorage:
    """File storage class (JSON)
    """
    __file_path = 'file.json'
    __objects = {}

    modules = {
                'BaseModel': 'base_model',
                'User': 'user',
                'State': 'state',
                'City': 'city',
                'Amenity': 'amenity',
                'Place': 'place',
                'Review': 'review'
            }

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    package = 'models'
                    module_name = self.modules[class_name]
                    module = importlib.import_module('.' + module_name,
                                                     package=package
                                                     )
                    class_ = getattr(module, class_name)

                    obj = class_(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
