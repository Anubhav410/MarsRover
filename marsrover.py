# import sys.args
from rover import Rover


def main():
    grid = input().split(" ")

    while True:
        position = input().split(" ")
        commands = input()
        r = Rover(grid=grid, commands=commands, position=position)
        r.execute_commands()


def validate_rover_position(rover, grid):
    pass

def validate_grid_position():
    pass

def read_input():
    '''
    this will read input
    :return: grid array , list of rovers with starting positions
    '''



if __name__ == "__main__":
    main()