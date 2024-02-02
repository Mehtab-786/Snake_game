from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score={self.score} ", align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER ", align="center", font=('Arial', 30, 'normal'))

    def score_update(self):
        self.score += 1
        self.clear()
        self.update_score()
