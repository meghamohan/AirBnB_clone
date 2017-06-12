#!/usr/bin/python3
"""
User Class
"""
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """ User Classes that inherits from BaseModel
    initializes email, password, first_name and last_name """

    def __init__(self, *args, **kwargs):
        """inherits the superclass"""
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""
