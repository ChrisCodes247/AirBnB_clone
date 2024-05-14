#!/usr/bin/env python3

from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user

    Attributes:
        email (str): email of the user
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
