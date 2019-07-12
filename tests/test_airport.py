import pytest

from airport.airport import *




def test_can_land():
    airship = {
        'name': 'Chernivtsi',
        'size': SMALL
    }
    airport = Airport()
    assert airport.can_land(airship)
