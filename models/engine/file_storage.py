#!/user/bin/python3
"""
serialize and deserialize instances to a JSON file and JSON to instances
"""

import json
from datetime import datetime


class FileStorage:
    """
    A class that does serializing and deserializing
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns all objects of FileStorage"""
        return FileStorage.__objects

    def new(self, obj):
        """creates new key for the objeckt"""
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes FileStorage.__objects"""
        with open(FileStorage.__file_path, 'w+') as f:
            dict_ = {}
            for key, value in FileStorage.__objects.items():
                dict_[key] = value.to_dict()
            json.dump(dict_, f)

    def reload(self):
        """
        if JSON file exists deserializes JSON to __objects
        else do nothing
        """
        try:
            with open(FileStorage.__file_path, mode='r', encoding='UTF-8')
            as to_file:
                objects_ = json.load(to_file)
                from models.base_model import BaseModel
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User

                class_list = [
                        'BaseModel', 'Amenity',
                        'City', 'Place',
                        'Review', 'State', 'User'
                        ]

                for key, value in objects_loaded.items():
                    if value.get("__class__") in class_list:
                        met = value.get("__class__")
                        self.objects[key] = eval(str(met))(objects_loaded[key])
        except(Exception):
            pass
