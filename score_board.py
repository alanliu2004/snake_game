from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)


    def eat(self):
        self.clear()
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)








