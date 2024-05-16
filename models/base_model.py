#!/usr/bin/env python3

import datetime
import uuid

class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of an instance
        """
        return ("[{}] ({}) {}".format(self.__class__.name__, self.id, self.__dict__)

    def save(self):
        """
        Updates attribute with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()

        return (dict_rep)
