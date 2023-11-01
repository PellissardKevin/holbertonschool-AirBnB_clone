#!/usr/bin/python3
"""definition of class used to store objects"""
import json
import models


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        index = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[index] = obj.to_dict()

    def save(self):
        dict_to_json = {}
        for key, value in self.__objects.items():
            dict_to_json[key] = value
        with open(self.__file_path, "w") as file:
            json.dump(dict_to_json, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())
        except Exception:
            pass
