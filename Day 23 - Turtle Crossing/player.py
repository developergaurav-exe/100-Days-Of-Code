from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__('turtle')
        self.new_level()

    def new_level(self):
            self.penup()
            self.goto(STARTING_POSITION)
            self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)
