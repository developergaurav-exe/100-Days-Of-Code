from turtle import Turtle, xcor

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__('circle')
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1 
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1 
        self.ball_speed *= 0.9

    def reset_pos(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()
        