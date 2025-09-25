import uuid

class Vehicle:
    def __init__(self, is_functional):
        self.id = uuid.uuid4()
        self.is_functional = is_functional
        self.is_occupied = False

    def set_functional(self, is_functional):
        self.is_functional = is_functional

    def is_available(self):
        return self.is_functional and not self.is_occupied
