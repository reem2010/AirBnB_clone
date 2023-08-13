#!/usr/bin/python3
"""Module inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class has public class attributes"""

    place_id = ""
    user_id = ""
    text = ""
