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
