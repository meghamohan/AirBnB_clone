#!/usr/bin/python3
"""City module that creates state class a subclass of basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """inherits the superclass"""
        super().__init__(*args, **kwargs)
    name = ""
    state_id = ""
