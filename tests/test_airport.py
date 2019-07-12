import pytest

from airport.airport import *


def test_can_land(get_airship, airport):
    assert airport.can_land(get_airship("Chernivtsi", SMALL))
    assert not airport.can_land(get_airship("Chernivtsi", LARGE))
    with pytest.raises(Exception) as exc:
        assert airport.can_land(get_airship("", SMALL))
    assert str(exc.value) == "Unknown airship, please provide your name if you want to land"


def test_land(get_airship, airport):
    assert airport.land(get_airship("Chernivtsi", SMALL))
    assert airport.land(get_airship("Chernivtsi", MEDIUM))
    assert not airport.land(get_airship("Chernivtsi", LARGE))
    assert len(airport.get_parked_airships()) == 2


def test_land_a_lot(get_airship, airport):
    assert airport.land(get_airship("Chernivtsi", SMALL))
    assert airport.land(get_airship("Chernivtsi", SMALL))
    assert airport.land(get_airship("Chernivtsi", SMALL))
    assert not airport.land(get_airship("Chernivtsi", MEDIUM))
    assert not airport.land(get_airship("Chernivtsi", MEDIUM))
    assert len(airport.get_parked_airships()) == 3


def test_land_enormous_airship(get_airship, airport):
    assert not airport.land(get_airship('Big Chernivtsi', 'enormous'))
    assert len(airport.get_parked_airships()) == 0
