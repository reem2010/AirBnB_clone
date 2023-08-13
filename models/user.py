#!/usr/bin/python3
"""This module for BaseModel"""
import uuid
import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """class user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
