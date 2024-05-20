#!/usr/bin/python3
"""The Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the Review Class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
