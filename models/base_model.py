#!/usr/bin/python3
import uuid
import datetime
"""Definition of class basemodel"""


class BaseModel:
    """Definition of class basemodel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat(sep='T')
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat(sep='T')

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
