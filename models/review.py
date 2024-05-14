#!/usr/bin/env python3

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review

    Attributes:
        place_id (str): id of the place
        user_id (str): id of the user
        text (str): the review itself

    """

    place_id = ""
    user_id = ""
    text = ""
