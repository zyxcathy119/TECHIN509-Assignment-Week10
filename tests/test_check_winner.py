
import sys
import os
sys.path.append(".")

from models.board import Board


def test_check_winner():
    board = Board()

    # Test case 1: No winner
    board.grid = [
        ["X", "O", "X"],
        ["X", "X", "O"],
        ["O", "X", "O"]
    ]
    assert board.check_winner() == None

    # Test case 2: Horizontal winner
    board.grid = [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "]
    ]
    assert board.check_winner() == "X"

    # Test case 3: Vertical winner
    board.grid = [
        ["O", "X", " "],
        ["O", "X", " "],
        ["O", " ", "X"]
    ]
    assert board.check_winner() == "O"

    # Test case 4: Diagonal winner
    board.grid = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", "O", "X"]
    ]
    assert board.check_winner() == "X"

    # Test case 5: Another diagonal winner
    board.grid = [
        ["O", "X", "X"],
        ["X", "O", " "],
        ["X", " ", "O"]
    ]
    assert board.check_winner() == "O"

    # Test case 6: Empty board
    board.grid = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    assert board.check_winner() == None

    # Test case 7: Full board with no winner
    board.grid = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    assert board.check_winner() == None

    # Test case 8: Horizontal winner in the last row
    board.grid = [
        ["O", "X", " "],
        ["O", "X", " "],
        ["X", "X", "X"]
    ]
    assert board.check_winner() == "X"

    # Test case 9: Vertical winner in the last column
    board.grid = [
        ["X", "O", "O"],
        ["X", " ", "O"],
        [" ", "X", "O"]
    ]
    assert board.check_winner() == "O"

    # Test case 10: Diagonal winner from top-right to bottom-left
    board.grid = [
        ["X", "O", "O"],
        ["O", "O", "X"],
        ["O", "X", "X"]
    ]
    assert board.check_winner() == "O"