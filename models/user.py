#!/usr/bin/python3
"""Module that defines the User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the User Class. The User class inherits from the BaseModel class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
