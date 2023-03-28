import random

class Player:
    def __init__(self, name):
        self.name = name
        self.resources = 100
        self.units = []

class Unit:
    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.health = 100
        self.damage = 10
        self.position = (0, 0) # initial position of the unit on the player field

class Game:
    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.field = [[None for _ in range(20)] for _ in range(20)]
        self.turn = 1 # player 1 goes first

    def run(self):
        while True:
            self.print_field()
            player = self.get_current_player()
            print(f"{player.name}'s turn")
            command = input("Enter command: ")
            if command == "quit":
                break
            elif command == "add unit":
                self.add_unit(player)
            elif command == "move unit":
                self.move_unit(player)
            elif command == "end turn":
                self.end_turn()
            else:
                print("Invalid command")

    def print_field(self):
        for row in self.field:
            for cell in row:
                if cell is None:
                    print(".", end="")
                else:
                    print(cell.name[0], end="")
            print()

    def get_current_player(self):
        if self.turn == 1:
            return self.player1
        else:
            return self.player2

    def add_unit(self, player):
        if player.resources < 50:
            print("Not enough resources")
            return
        unit = Unit(f"{player.name} Unit", player)
        player.units.append(unit)
        player.resources -= 50
        x, y = self.get_random_empty_cell()
    unit.position = (x, y)
    self.field[x][y] = unit

def move_unit(self, player):
    unit = self.get_unit_by_input(player)
    if not unit:
        return
    x, y = self.get_position_by_input()
    if not self.is_empty_cell(x, y):
        print("Cell is not empty")
        return
    unit.position = (x, y)
    self.field[x][y] = unit
    self.field[unit.position[0]][unit.position[1]] = None

def end_turn(self):
    self.turn = 3 - self.turn # switch player turn

def get_random_empty_cell(self):
    while True:
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        if self.is_empty_cell(x, y):
            return x, y

def is_empty_cell(self, x, y):
    return self.field[x][y] is None

def get_unit_by_input(self, player):
    name = input("Enter unit name: ")
    for unit in player.units:
        if unit.name == name:
            return unit
    print("Unit not found")
    return None

def get_position_by_input(self):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    return x, y

class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.units = []
        self.resources = 100

    def add_unit(self, unit):
        if self.resources < unit.cost:
            print("Not enough resources")
            return False
        self.units.append(unit)
        self.resources -= unit.cost
        return True

class Unit:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.position = None

class Game:
    def __init__(self):
        self.players = []
        self.field = [[None for _ in range(20)] for _ in range(20)]
        self.turn = 1

    def add_player(self, player):
        self.players.append(player)

    def play(self):
        while True:
            self.print_field()
            player = self.players[self.turn - 1]
            if player.is_computer:
                self.computer_turn(player)
            else:
                self.human_turn(player)
            if not self.is_game_over():
                self.end_turn()
            else:
                self.print_field()
                winner = self.get_winner()
                print(f"Game over! {winner.name} wins!")
                break

    def human_turn(self, player):
        print(f"{player.name}'s turn")
        while True:
            print(f"Resources: {player.resources}")
            action = input("Enter action (add/move/end): ")
            if action == "add":
                self.add_unit(player)
            elif action == "move":
                self.move_unit(player)
            elif action == "end":
                break
            else:
                print("Invalid action")

    def computer_turn(self, player):
        print(f"{player.name}'s turn")
        self.add_unit(player)
        self.move_unit(player)

    def add_unit(self, player):
        name = input("Enter unit name: ")
        cost = int(input("Enter unit cost: "))
        damage = int(input("Enter unit damage: "))
        unit = Unit(name, cost, damage)
        if player.add_unit(unit):
            self.place_unit(unit)

    def place_unit(self, unit):
        x, y = self.get_random_empty_cell()
        unit.position = (x, y)
        self.field[x][y] = unit

    def move_unit(self, player):
        unit = self.get_unit_by_input(player)
        if not unit:
            return
        x, y = self.get_position_by_input()
        if not self.is_empty_cell(x, y):
            print("Cell is not empty")
            return
        unit.position = (x, y)
        self.field[x][y] = unit
        self.field[unit.position[0]][unit.position[1]] = None

    def end_turn(self):
        self.turn = 3 - self.turn # switch player turn
        for player in self.players:
            player.resources += 10
            for unit in player.units:
                if unit.position is not None:
                    for x, y in self.get_adjacent_cells(unit.position):
                        other_unit = self.field[x][y]
                        if other_unit is not None and other_unit.position is not None and other_unit.position != unit.position:
                            self.combat(unit, other_unit)

    def get_random_empty_cell(self):
        while True:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
            if self.is_empty_cell(x, y):
                return x, y

    def is_empty_cell(self, x,y):
        return self.field[x][y]

    def get_unit_by_input(self, player):
        name = input("Enter unit name: ")
        for unit in player.units:
            if unit.name == name:
                return unit
        print("Unit not found")
        return None

def get_position_by_input(self):
    x = int(input("Enter x position: "))
    y = int(input("Enter y position: "))
    return x, y

def get_adjacent_cells(self, position):
    x, y = position
    return [(i, j) for i in range(max(x-1, 0), min(x+2, 20)) for j in range(max(y-1, 0), min(y+2, 20))]

def combat(self, attacker, defender):
    print(f"{attacker.name} attacks {defender.name}")
    defender_hp = defender.cost
    defender_hp -= attacker.damage
    if defender_hp <= 0:
        print(f"{defender.name} dies")
        self.field[defender.position[0]][defender.position[1]] = None
        defender.position = None
        attacker.position = defender.position

def is_game_over(self):
    for player in self.players:
        if len(player.units) == 0:
            return True
    return False

def get_winner(self):
    for player in self.players:
        if len(player.units) > 0:
            return player

def print_field(self):
    print("   " + " ".join([str(i) for i in range(20)]))
    for i in range(20):
        row = []
        for j in range(20):
            unit = self.field[i][j]
            if unit is None:
                row.append(".")
            else:
                row.append(unit.name[0])
        print(f"{i:2d} {' '.join(row)}")
    print()

player1 = Player("Player 1")
player2 = Player("Player 2", is_computer=True)
game = Game()
game.add_player(player1)
game.add_player(player2)
game.play()

