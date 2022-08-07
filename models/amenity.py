#!/usr/bin/python3
"""module that creates amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class Amenity that inherits from BaseModel
    Attributes:
    name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """creates new instance"""

        super().__init__(self, *args, **kwargs)
