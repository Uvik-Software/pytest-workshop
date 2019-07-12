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
        if airship['size'] not in [LARGE, MEDIUM, SMALL]:
            return False
        if airship['size'] == LARGE:
            return False
        if airship['size'] == MEDIUM:
            return self.parking_slots - self.slots_taken >= 2
        if airship['size'] == SMALL:
            return self.parking_slots - self.slots_taken >= 1
        return True

    def land(self, airship):
        if not self.can_land(airship):
            return False

        if airship['size'] == SMALL:
            self.slots_taken += 1
            self.airships_parked.append(airship)
        else:
            self.slots_taken += 2
            self.airships_parked.append(airship)
        return True

    def get_parked_airships(self):
        return self.airships_parked
