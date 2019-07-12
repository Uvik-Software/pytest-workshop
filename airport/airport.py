PARKING_SLOTS = 3
SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'


class Airport(object):

    def __init__(self, parking_slots=PARKING_SLOTS):
        self.airships_parked = []
        self.slots_taken = 0
        self.parking_slots = parking_slots

    def can_land(self, airship):
        if not airship['name']:
            raise Exception('Unknown airship, please provide your name if you want to land')
        if airship['size'] == LARGE:
            return False
        return True

    def land(self, airship):
        self.can_land(airship)

        if airship['size'] == SMALL:
            self.slots_taken += 1
            self.airships_parked.append(airship)
        else:
            self.slots_taken += 2
            self.airships_parked.append(airship)
        return True

    def get_parked_airships(self):
        return self.airships_parked
