from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score={self.score}", move=False, align='left', font=('Arial', 8, 'normal'),)



    def refresh(self):
        self.score +=1
        self.clear()
        self.write(f"Score={self.score}", move=False, align='left', font=('Arial', 8, 'normal'), )

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align='left', font=('Arial', 8, 'normal'), )
