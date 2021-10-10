import random

class Hider:
    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance = [0, 0]
    
    def get_hint(self):
        hint = ""
        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "(>.<) Getting warmer!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting colder!"
        return hint

    def watch(self, location):
        self.distance.append(abs(location - self.location))
