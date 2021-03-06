from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = (0)
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"El puntaje es: {self.score}", font=("Arial",24,"normal"), align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write("juego terminado", font=("Arial",24,"normal"), align="center")
