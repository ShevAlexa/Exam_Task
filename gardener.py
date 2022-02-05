class Gardener:
    def __init__(self, plant, name="Alexei"):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} is working...")
        self._plant.grow_all()
        print(f"{self.name} ended work")

    def harvest(self):
        print(f"{self.name} is harvesting...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("It's excellent tomatoes!")
        else:
            print("Tomatoes not riped")

    def information(self):
        self._plant.status_all()

    @staticmethod
    def knowledge_base():
        print("Sow tomato seeds. Cultivate and carefully care for them. Wait for ripeness and collect delicious crops")
