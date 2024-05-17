#!/usr/bin/python3
# Module that defines the User Class
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''