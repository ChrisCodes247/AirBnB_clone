#!/usr/bin/env python3

from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place

    Attributes:
        city_id (str): id of the city
        User_id (str): the User.id
        name (str): name of place
        description (str): brief explanation of the place
        number_rooms (int): number of rooms
        number_bathrooms(int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): price for a night
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (str(list)): list of Amenity.id

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
