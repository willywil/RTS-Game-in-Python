from player import Player
from enemy import Enemy
from power_building import Power_Building
from refinery_building import Refinery_Building



power_building = Power_Building("Solar Panels", 1000, 50, 1)
refinery_building = Refinery_Building("Stone Crusher", 1000, 50, 1, ["miner", "excuvator", "worker"])
player = Player("John Doe", 100, 0, 1, ["archer", "knight", "mage"])
enemy = Enemy("John Doe", 100, 0, 1, ["archer", "knight", "mage"])

def move_unit():
    print("unit move 5 spaces")

def build_structure():
    print("which do you want to build?")

def attack_enemy():
    print("you threw a brick at bob, ouch!!")
def end_turn():
    print("you have ended your turn")

def get_user_input():
    options = {
        "1": move_unit,
        "2": build_structure,
        "3": attack_enemy,
        "4": end_turn
    }
    print("Select an option:")
    print("1. Move unit")
    print("2. Build structure")
    print("3. Attack enemy")
    print("4. End turn")

    choice = None
    while choice not in ["1", "2", "3", "4"]:
        choice = input("> ")
        if choice in options:
            options[choice]()
            print("you have selected option", choice)
        else:
            print("Invalid option")
        print("Current options:", options)
    
    return choice
    


def update_game():
    # Get user input (e.g. mouse clicks, keyboard input)
    user_input = get_user_input()
    print(user_input)
    return 0
    """
    # Update game state based on user input
    update_game_state(user_input)

    # Update game objects (e.g. move units, animate sprites)
    update_game_objects()

    # Check for collisions between game objects
    check_collisions()

    # Check for victory or defeat conditions
    check_game_status()

    # Draw game objects to the screen
    draw_game_objects()
    """

update_game()

print("end Program")
