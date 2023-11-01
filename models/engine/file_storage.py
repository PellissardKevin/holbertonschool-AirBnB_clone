#!/usr/bin/python3
"""definition of class used to store objects"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        index = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[index] = obj

    def save(self):
        dict_to_save = {}
        for key, obj in self.__objects.items():
            dict_to_save[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(dict_to_save, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                my_obj_dict = json.load(file)
                for key, dict in my_obj_dict.items():
                    self.__objects[key] = eval(dict['__class__'])(**dict)
        except Exception as e:
            pass
