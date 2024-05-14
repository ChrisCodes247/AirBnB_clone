#!/usr/bin/env python3

from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city

    Attributes:
        state_id (str): the id of the state
        name (str): the name of the city
    """

    state_id = ""
    name = ""
