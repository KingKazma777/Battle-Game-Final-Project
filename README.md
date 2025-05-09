# KNIGHT'S TRIAL

Knight's Trial is a beginner-friendly, text-based Python battle game where you, the player, face off against a series of enemies in turn-based combat. 
I built this as my final project for CIS111G: Computer Technologies, the game blends randomness with strategy and encourages thoughtful play over mindless button-mashing.

## REQUIREMENTS

To run Knight’s Trial, you’ll need the following:

- Python 3.7 or higher
  Download from: https://www.python.org/downloads/

- A basic code editor (optional but recommended):
  Examples: VS Code, PyCharm, Sublime Text, or even Notepad++

- A terminal or command prompt that can run .py files
  (This can be your system's built-in terminal or one inside your editor)

## HOW TO RUN THE GAME

1. Download or clone this repository
   Place the main script file (knights_trial.py) into a project folder.

2. Open the terminal in that folder (or use your editor's terminal).

3. Run the game using:
   python knights_trial.py

4. Play using the number keys when prompted.

## HOW TO PLAY

- You play as a Knight facing off against three enemies: a Goblin, an Orc, and the Dark Knight.
  
- The game is turn-based — on each turn, both you and your opponent choose an action:
  - Attack: Deal damage (random range based on your character)
  - Heal: Regain some HP (can’t overheal)
  - Defend: Blocks most incoming damage (reduces it to 1)
    
- If you attack and your opponent defends, you become staggered and lose your next turn.

## GAME RULES & MECHANICS

- Staggering:
  If you attack an opponent who defends, your character becomes staggered and must skip the next turn.

- Healing Rules:
  - If you try to heal while being attacked, your heal fails completely — you gain no HP.
  - If you heal while your opponent defends, your healing is doubled.

- Enemy rules:
  The enemy will only heal when injured and skips a turn if staggered as well.

- Victory Conditions:
  Defeat all three enemies without dying. If your HP drops to zero, the game ends.

## DEVELOPER'S NOTE

Honestly, one of the toughest parts of working on this project was getting the balance right. 
It was a real challenge figuring out how to make the random elements feel fun and fair while still allowing for strategic decision-making. 
I didn’t want the game to feel too easy or like you could just spam one move and win, but I also didn’t want it to be completely luck-based or frustrating.
Finding that middle ground, where each turn felt meaningful, and the outcomes still surprised me, took more thought than I expected, but I've learned a lot in the process and plan on refining this further. It's still a tough win right now, but good luck!

## SOURCES & INSPIRATION

This project was developed with help from course materials and personal research. All of the code was written and debugged by me, but some of the sources that I pulle dinspiration from and used as help with the design and logic of Knight’s Trial include:

- Al Sweigart. Automate the Boring Stuff with Python. No Starch Press, 2015.
- Real Python Tutorials. Object-Oriented Programming in Python.
  https://realpython.com/python3-object-oriented-programming/
- GeeksforGeeks. Turn-Based Games in Python – Structure and Logic.
  https://www.geeksforgeeks.org/python-simple-turn-based-game/
- Python Software Foundation. The Python Standard Library Documentation.
  https://docs.python.org/3/library/random.html
