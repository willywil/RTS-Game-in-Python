player = {
    "name": "John Doe",
    "health": 100,
    "gold": 0,
    "level": 1,
    "units": ["archer", "knight", "mage"]
}


class Player:
    def __init__(self, name, health, gold, level, units):
        self.name = name
        self.health = health
        self.gold = gold
        self.level = level
        self.units = units
