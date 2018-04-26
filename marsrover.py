# import sys.args
from rover import Rover


def main():
    grid = input().split(" ")

    while True:
        position = input().split(" ")
        commands = input()
        r = Rover(grid=grid, commands=commands, position=position)
        r.execute_commands()


if __name__ == "__main__":
    main()