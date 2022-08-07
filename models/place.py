#!/usr/bin/python3
"""module that creates Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    class Place that inherits from BaseModel
    Attributes:
    city_id: string - empty string: City.id
    user_id: string - empty string: User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list: list of Amenty.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amentiy_ids = ["", ""]

    def __init__(self, *args, **kwargs):
        """creates new instance"""

        super().__init__(self, *args, **kwargs)
