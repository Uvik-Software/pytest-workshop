import pytest

from airport.airport import *


@pytest.fixture
def get_airship():

    def construct_airship(name, size):
        airship = {
            'name': name,
            'size': size
        }
        return airship

    return construct_airship


def test_can_land(get_airship):
    airship = get_airship("Chernivtsi", SMALL)
    airport = Airport()
    assert airport.can_land(airship)
