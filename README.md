# Tic Tac Toe Game

A simple command-line implementation of the classic **Tic Tac Toe** game, written in Python. This project demonstrates object-oriented programming concepts, including encapsulation, inheritance, and modularity. The game supports both human and random AI players.


- [Tic Tac Toe Game](#tic-tac-toe-game)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Installation and Usage](#installation-and-usage)
  - [License](#license)

---

## Features

- **Two Players**: Human vs Human or Human vs Random.
- **Random AI Player**: The random player chooses moves randomly.
- **Game Logging**: Saves the winner and first player to a CSV file for tracking game outcomes.

---

## Project Structure

```
tic_tac_toe/
├── main.py                # Entry point to start the game
├── models/                # Core game classes
│   ├── __init__.py
│   ├── board.py           # Handles the game board and logic
│   ├── player.py          # Manages human and AI players
├── utils/                 # Support functions
│   ├── __init__.py
│   ├── game_logic.py      # Orchestrates the game flow
│   ├── game_data.py       # Stores game outcomes in a CSV file
├── data/                  # Stores generated game data
│   ├── game_data.csv      # Records first player and winner
├── .gitignore             # Specifies ignored files and directories
├── README.md              # Project documentation
├── requirements.txt       # Required packages for the project
```

---

## Installation and Usage

**Get Code**
```
git clone https://github.com/luyaoniu-uw/TECHIN509-Assignment-Week10.git
```
**Build Environment**
```
cd TECHIN509-Assignment-Week10
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
**Customization**

Customize the maximum number of attempts of AI player by changing `max_attempts`.



## License

This project is licensed under the MIT License. See the LICENSE file for details.

