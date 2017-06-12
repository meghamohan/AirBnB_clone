#!/usr/bin/python3
"""Amenity module that creates state class a subclass of basemodel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """inherits the superclass"""
        super().__init__(*args, **kwargs)

    name = ""
