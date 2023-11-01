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
        self.__objects[index] = obj

    def save(self):
        with open(self.__file_path, "w") as file:
            for key, value in self.__objects.items():
                print()
                json.dump(value.to_dict(), file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                obj = BaseModel(json.load(file))
                self.new(obj)
        except Exception as e:
            print(e)
            pass
