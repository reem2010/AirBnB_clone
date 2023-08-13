#!/usr/bin/python3
"""Module inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class has public class attribute(State_id - name)"""

    state_id = ""
    name = ""
