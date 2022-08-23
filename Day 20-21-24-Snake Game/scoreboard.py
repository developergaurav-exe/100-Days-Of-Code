from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.score = 0
        self.high_score = 0
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
        self.score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over.", align= ALIGN, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
        
