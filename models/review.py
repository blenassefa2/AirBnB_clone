#!/usr/bin/python3
"""module that creates review"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    class Review that inherits from BaseModel
    Attributes:
    place_id: string - empty string
    user_id: string - empty string
    text: string - empty string
    """

    place_id = ""
    user_id = ""
    def __init__(self, *args, **kwargs):
        """creates new instance"""

        super().__init__(self, *args, **kwargs)
