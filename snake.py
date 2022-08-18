from turtle import Turtle

# CONSTANTS written in Capital
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            t = Turtle(shape='square')
            t.color("white") # t.color instead of pencolor as it doesn't colors fillcolor
            t.penup()
            t.setpos(x, 0)
            self.segments.append(t) # storing all the turtles in the list: segments
            x -= 20

    def move(self):
        for t in range(len(self.segments)-1, 0, -1):
            self.segments[t].goto(self.segments[t-1].xcor(),
                                  self.segments[t-1].ycor()) # this line makes sure all other snake segments follow head
        self.head.forward(20) # always going to move 20 pixels

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
