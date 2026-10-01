from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        try:
            with open("data.txt") as data:
                print(data.read())
                self.high_score = int(data.read())
        except:
            self.high_score=0
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score = {self.score}",align="center",font=("Arial",15,"normal"))
    
    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}",align="center",font=("Arial",15,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score+=1
        self.write_score()

    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align="center",font=("Arial",20,"normal"))