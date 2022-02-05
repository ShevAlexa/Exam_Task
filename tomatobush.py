from tomato import Tomato


class TomatoBush:
    def __init__(self, number):
        self.tomatoes = [Tomato(index) for index in range(number)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    def status_all(self):
        if self.tomatoes:
            for tomato in self.tomatoes:
                tomato.status()
        else:
            print("All tomatoes were harvested!")
