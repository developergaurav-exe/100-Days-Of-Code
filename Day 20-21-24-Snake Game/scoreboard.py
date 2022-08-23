from operator import mod
from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('saved_data.txt') as f:
            self.high_score = int(f.read()) # have to convert to int to make it calcutable further

        self.color("white")
        self.penup()
        self.goto(0,270)
        
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGN, font= FONT)

    def reset_scoreboard(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('saved_data.txt', mode='w') as f:
                f.write(f"{self.high_score}") # write function can only write string

        self.score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over.", align= ALIGN, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
        
