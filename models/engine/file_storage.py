#!/usr/bin/python3
"""definition of class used to store objects"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())
        except:
            pass
