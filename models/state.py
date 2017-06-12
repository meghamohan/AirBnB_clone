#!/usr/bin/python3
"""State module that creates state class a subclass of basemodel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = ""
