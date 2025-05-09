import random  # Used to generate variable attack and healing values for unpredictability in combat

# Design Note
# This program uses functions to organize code into reusable pieces (e.g., player_turn, enemy_turn).
# This avoids repeating code, keeps the game structured, and made it easier for me to update or expand later.

# Using "class Character" here keeps track of player/enemy stats and behavior neatly, rather than using scattered variables.
class Character:
    def __init__(self, name, hp, attack_power, heal_amount):
        # Sets starting values for each character (player or enemy)
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.heal_amount = heal_amount
        self.action = None  # Stores the action chosen this turn
        self.can_attack_next_turn = True  # Used to handle stagger status

    def is_alive(self):
        # Check if character is still alive (HP > 0)
        return self.hp > 0

    def choose_action(self, is_player=True):
        # Determines and stores the action for the current turn
        if not self.can_attack_next_turn:
            print(f"{self.name} is staggered and must recover this turn!")
            self.action = "none"
            return

        if is_player:
            print("\nYour Turn!")
            print("1. Attack")
            print("2. Heal")
            print("3. Defend")
            choice = input("Choose an action: ")
            if choice == "1":
                print(f"{self.name} prepares to strike!")
                self.action = "attack"
            elif choice == "2":
                self.action = "heal"
            elif choice == "3":
                self.action = "defend"
            else:
                print("Invalid choice. You fumble and lose your turn.")
                self.action = "none"
        else:
            # Enemy AI: skips attack if staggered, avoids heal at full health
            options = ["attack", "defend"]
            if self.hp < self.max_hp:
                options.append("heal")
            self.action = random.choice(options)

    def attack(self, target, target_defending):
        # Attacks target; if they're defending, attacker becomes staggered
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        if target_defending:
            print(f"{self.name} is staggered and cannot act next turn!")  # Stagger effect applied
            self.can_attack_next_turn = False
            damage = 1
            print(f"{target.name} braces and reduces the damage to 1!")  # Now shown after defense message
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.hp = max(0, target.hp - damage)  # Ensures HP doesn’t go below 0

    def heal(self):
        # Restores a random amount of HP (capped at max HP)
        heal_value = random.randint(self.heal_amount - 2, self.heal_amount + 2)
        self.hp = min(self.max_hp, self.hp + heal_value)
        print(f"{self.name} heals for {heal_value} HP!")

    def reset_health(self):
        # Fully restores health and resets stagger status between fights
        self.hp = self.max_hp
        self.can_attack_next_turn = True


def resolve_turn(player, enemy):
    # Executes both player and enemy actions simultaneously
    player_defending = player.action == "defend"
    enemy_defending = enemy.action == "defend"
    player_healing = player.action == "heal"
    enemy_healing = enemy.action == "heal"

    # Defend messages shown first, before effects like reduced damage
    if player_defending:
        print(f"{player.name} is defending this turn!")
    if enemy_defending:
        print(f"{enemy.name} is defending this turn!")

    # Resolve attacks
    if player.action == "attack":
        player.attack(enemy, enemy_defending)
    if enemy.action == "attack":
        enemy.attack(player, player_defending)

    # Resolve healing
    # - Heal vs Attack = Heal fails
    # - Heal vs Defend = Heal doubles
    if player_healing:
        if enemy.action == "attack":
            print(f"{player.name} tried to heal but was interrupted! No health was gained.")
        elif enemy.action == "defend":
            original_hp = player.hp
            player.heal()
            print(f"{player.name}'s healing was empowered by the defensive pause!")  # New effect description
            additional_heal = min(player.max_hp - player.hp, original_hp + (player.hp - original_hp))
            player.hp = min(player.max_hp, player.hp + additional_heal)
        else:
            player.heal()

    if enemy_healing:
        if player.action == "attack":
            print(f"{enemy.name} tried to heal but was interrupted! No health was gained.")
        elif player.action == "defend":
            original_hp = enemy.hp
            enemy.heal()
            print(f"{enemy.name}'s healing was empowered by the defensive pause!")  # New effect description
            additional_heal = min(enemy.max_hp - enemy.hp, original_hp + (enemy.hp - original_hp))
            enemy.hp = min(enemy.max_hp, enemy.hp + additional_heal)
        else:
            enemy.heal()

    # Reset stagger status unless attack was defended
    if player.action != "attack" or not enemy_defending:
        player.can_attack_next_turn = True
    if enemy.action != "attack" or not player_defending:
        enemy.can_attack_next_turn = True

# Displays the game title neatly
def game_loop():
    line_width = 37
    title = "KNIGHT'S TRIAL"
    print("=" * line_width)
    print(title.center(line_width))
    print("=" * line_width)

    # Creates the player character
    player = Character("Knight", hp=30, attack_power=7, heal_amount=5)

    # Defines a sequence of enemies with increasing difficulty
    enemies = [
        Character("Goblin", hp=20, attack_power=5, heal_amount=3),       # Easy
        Character("Orc", hp=30, attack_power=7, heal_amount=4),          # Medium
        Character("Dark Knight", hp=40, attack_power=9, heal_amount=5)   # Hard
    ]

    print("\nWelcome, brave Knight, to the Knight's Trial!\n")
    total_turns = 0  # Total turns across all fights

    for i, enemy in enumerate(enemies):
        # Using enumerate lets us access both the enemy and its position in the list,
        # which makes it easier to track battle number or scale of difficulty if I so needed.
        print(f"\nA hostile {enemy.name} appears!")
        battle_turns = 0  # Tracks how many turns this specific battle takes

        while player.is_alive() and enemy.is_alive():
            # Show both player and enemy HP before each turn and keeps track of this
            print(f"\n{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
            player.choose_action(is_player=True)
            enemy.choose_action(is_player=False)
            resolve_turn(player, enemy)
            battle_turns += 1
            total_turns += 1

        # Victory pathing
        if player.is_alive():
            print(f"\nYou have defeated the {enemy.name} in {battle_turns} turns!")
            print("The knight has triumphed and rests for the night before the next day’s battle...\n")
            player.reset_health()
            print(f"Your health is fully restored. Prepare for the next battle!\n")
        else:
            print("\nYou were defeated in battle. The trial ends here.")
            return  # Exit game loop if player dies

    # Final victory screen
    print(f"\nVICTORY! You have conquered the Knight's Trial in {total_turns} total turns!")
    print("Your legend will be told for generations. Well fought, brave Knight!\n")


# Starts the game if run directly
if __name__ == "__main__":
    game_loop()
