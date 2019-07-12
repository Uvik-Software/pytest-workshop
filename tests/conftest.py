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


@pytest.fixture
def airport():
    return Airport()
