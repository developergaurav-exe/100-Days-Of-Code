from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y) -> None:

        super().__init__('square')
        self.penup()
        self.setpos(x=x, y=y)
        self.color("red")
        self.turtlesize(5,1) # stretch_wid = 5*20 => 100 px and stretch_len = 1*20 => 20 px; so don't write pixels, write stretch ratio 

    def up(self):
        self.setpos(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        self.setpos(x=self.xcor(), y=self.ycor() - 20)