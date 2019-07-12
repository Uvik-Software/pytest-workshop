import pytest

from airport.airport import *


def test_can_land(get_airship, airport):
    airship = get_airship("Chernivtsi", SMALL)
    assert airport.can_land(airship)
