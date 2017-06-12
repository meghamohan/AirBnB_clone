#!/usr/bin/python3
"""Place module that creates state class a subclass of basemodel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """inheirts the superclass"""
        super().__init__(*args, **kwargs)
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenities = []
