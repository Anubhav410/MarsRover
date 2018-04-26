class RoverHasFallen(Exception):
    def __init__(self):
        message = "Rover fell off the plateau"
        super(RoverHasFallen, self).__init__(message)


class InvalidGrid(Exception):
    def __init__(self):
        message = "Invalid Grid parameters"
        super(InvalidGrid, self).__init__(message)


