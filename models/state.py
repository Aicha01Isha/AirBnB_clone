#!/usr/bin/python3

"""Defines a class State that inherits from BaseModel"""
from models.base_model import BaseModel
class State(BaseModel):
    """Class that defines properties of State.

    Attributes:
        name (string): name of state.
    """
    name = ""
    def __init__(self, *args, **kwargs):
        """Creates"""
        super().__init__(*args, **kwargs)
"""yes"""
