import turtle
import pandas as pd
import time


class Game:

    def __init__(self):
        self.score = 0
        self.start = 0
        self.game_on = True
        self.data = pd.read_csv("50_states.csv")
        self.states = self.data["state"].to_list()
        self.timer_window = turtle.Screen()
        self.setup_screen()
        self.game()

        turtle.mainloop()



    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.setup(750, 550)
        self.screen.title("U.S. States Quiz")
        self.screen.addshape("blank_states_img.gif")
        turtle.shape("blank_states_img.gif")
        turtle.tracer(0)
        self.screen.onkey(self.close_game, "Escape")
        self.screen.listen()


    def close_game(self):
        self.game_on = False
        turtle.bye()


    def game(self):
        self.start = time.time()
        while self.game_on:

            answer = turtle.textinput("{}/50 states".format(self.score), "Enter the state").title()

            if answer == "Exit":
                self.game_on = False
                break
            if answer in self.states:
                self.states.remove(answer)
                self.score += 1

                x, y = self.data[self.data["state"] == answer].x.item(), self.data[self.data["state"] == answer].y.item()
                self.write_state(answer, x, y)

                time.sleep(0.01)
                self.screen.update()

            if self.score == 50:
                print("Congratulations!")
                self.game_on = False


    def write_state(self, answer, x, y):
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(answer, align="center")