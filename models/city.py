#!/usr/bin/python3
"""The City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the City Class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
