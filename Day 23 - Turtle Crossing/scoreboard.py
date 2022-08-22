from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def level_up(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"Level: {self.score}", align='left', font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align='center', font=FONT)