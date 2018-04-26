from exceptions import RoverHasFallen, InvalidGrid

FACING = ["N", "E", "S", "W"]


class Rover:
    grid = []
    commands = []
    pos_x = ""
    pos_y = ""
    facing = ""

    def __init__(self, grid, commands, position):
        self.grid = list(map(int, grid))
        self.commands = list(commands)
        self.pos_x = int(position[0])
        self.pos_y = int(position[1])
        self.facing = position[2]

        self.validate_grid()

    def validate_grid(self):
        if self.grid[0] < 0 or self.grid[1] < 0:
            raise InvalidGrid()

    def execute_commands(self):
        # its either going to be 'M', or one of the direction commands
        for command in self.commands:
            if command == 'M':
                self.move()
            else:
                self.turn(command)
        print("Final Position {x} {y} {facing}".format(x=self.pos_x, y=self.pos_y, facing=self.facing))

    def move(self):
        if self.facing == "N":
            self.pos_y += 1
        if self.facing == "S":
            self.pos_y -= 1
        if self.facing == "E":
            self.pos_x += 1
        if self.facing == "W":
            self.pos_x -= 1

        self.validate_rover_position()

    def turn(self, direction):
        current_facing_index = FACING.index(self.facing)
        if direction == "L":
            current_facing_index = (current_facing_index - 1) % 4
        elif direction == "R":
            current_facing_index = (current_facing_index + 1) % 4

        self.facing = FACING[current_facing_index]

    def validate_rover_position(self):
        if self.pos_x > self.grid[0] or self.pos_y > self.grid[1]:
            raise RoverHasFallen
