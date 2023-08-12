#!/usr/bin/python3

"""aicha"""

"""
This is review class that represents new reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review subclass that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""

"""yes yes yes """
