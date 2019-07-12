import pytest

from airport.airport import *


@pytest.fixture
def get_airship():
    airship = {
        'name': 'Chernivtsi',
        'size': SMALL
    }
    return airship


def test_can_land(get_airship):
    airship = get_airship
    airport = Airport()
    assert airport.can_land(airship)
