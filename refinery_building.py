refinery_building = {
    "name": "Stone Crusher",
    "health": 1000,
    "gold": 50,
    "level": 1,
    "units": ["miner", "excuvator", "worker"]
}

class Refinery_Building:
    def __init__(self, name, health, gold, level, units):
        self.name = name
        self.health = health
        self.gold = gold
        self.level = level
        self.units = units