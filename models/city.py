#!/usr/bin/python3
"""module that creates city"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class City that inherits from BaseModel
    Attributes:
    state_id: string - empty string
    name: string - empty string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """creates new instance"""

        super().__init__(self, *args, **kwargs)
