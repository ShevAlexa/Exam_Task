class Tomato:
    states = {0: "green",
              1: "yellow",
              2: "red"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < len(Tomato.states) - 1:
            self._state += 1
            print(f"Tomato {self._index} is {Tomato.states[self._state]}")
        else:
            print("All tomatoes riped")

    def is_ripe(self):
        if self._state == len(Tomato.states) - 1:
            return True
        return False

    def status(self):
        print(f"Tomato {self._index} is {Tomato.states[self._state]}")
