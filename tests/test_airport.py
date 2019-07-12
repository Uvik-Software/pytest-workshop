import pytest

from airport.airport import *


def test_can_land(get_airship, airport):
    airship = get_airship("Chernivtsi", SMALL)
    assert airport.can_land(airship)
    assert not airport.can_land(get_airship("Chernivtsi", LARGE))
    with pytest.raises(Exception) as exc:
        assert airport.can_land(get_airship("", SMALL))
    assert str(exc.value) == "Unknown airship, please provide your name if you want to land"
