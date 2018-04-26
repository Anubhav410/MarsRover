from rover import Rover
import pytest
from exceptions import InvalidGrid, RoverHasFallen

def test_movement():
    grid = [5, 5]
    rover_position = [1, 2, "N"]
    commands = "LMLMLMLMM"


    rover = Rover(grid=grid, commands=commands, position=rover_position)
    rover.execute_commands()

    assert rover.pos_x == 1
    assert rover.pos_y == 3
    assert rover.facing == 'N'

    grid = [5, 5]
    rover_position = [3, 3, "E"]
    commands = "MMRMMRMRRM"

    rover = Rover(grid=grid, commands=commands, position=rover_position)
    rover.execute_commands()

    assert rover.pos_x == 5
    assert rover.pos_y == 1
    assert rover.facing == 'E'


def test_right_turn():
    grid = [5, 5]
    rover_position = [3, 3, "E"]
    commands = "MMRMMRMRRM"

    rover = Rover(grid=grid, commands=commands, position=rover_position)
    rover.turn("R")
    assert rover.facing == "S"

    rover.turn("R")
    assert rover.facing == "W"

    rover.turn("R")
    assert rover.facing == "N"


def test_left_turn():
    grid = [5, 5]
    rover_position = [3, 3, "E"]
    commands = "MMRMMRMRRM"

    rover = Rover(grid=grid, commands=commands, position=rover_position)
    rover.turn("L")
    assert rover.facing == "N"

    rover.turn("L")
    assert rover.facing == "W"

    rover.turn("L")
    assert rover.facing == "S"

def test_fallen_rover():
    grid = [5, 5]
    rover_position = [3, 3, "E"]
    commands = "MMRMMRMRRMMMMMMM"
    rover = Rover(grid=grid, commands=commands, position=rover_position)
    with pytest.raises(RoverHasFallen):
        rover.execute_commands()

def test_invalid_grid_commands():
    grid = [-5, 5]
    rover_position = [3, 3, "E"]
    commands = "MMRMMRMRRMMMMMMM"
    with pytest.raises(InvalidGrid):
        rover = Rover(grid=grid, commands=commands, position=rover_position)


