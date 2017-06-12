#!/usr/bin/python3
"""Review module that creates state class a subclass of basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """inherits the superclass"""
        super().__init__(*args, **kwargs)
    place_id = ""
    user_id = ""
    text = ""
