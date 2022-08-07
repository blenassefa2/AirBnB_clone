#!/usr/bin/python3
"""module that creates state"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    class State that inherits from BaseModel
    Attributes:
    name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """creates new instance"""

        super().__init__(self, *args, **kwargs)
