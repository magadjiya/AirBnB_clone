#!/usr/bin/python3
"""The State Class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines the State Class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
