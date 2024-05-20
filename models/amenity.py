#!/usr/bin/python3
"""The Amenity Class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the Amenity Class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
