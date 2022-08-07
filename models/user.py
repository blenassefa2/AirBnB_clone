#!/usr/bin/python3
"""module that creates user"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel
    Attributes:
    email: string - empty string
    last_name: string - empty string
    password: string - empty string
    first_name: string - empty string
    """

    email = ""
    first_name = ""
    last_name = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """creates new instance"""

        super().__init__(self, *args, **kwargs)
