from tkinter import *
from time import sleep
from playsound import playsound

from Apple import *
from Bowl import *
from Background import *

class Game_CatchApple:

    LIVES_BEGIN = 3

    def __init__(self, canvas):
        self.background = Background(canvas)
        self.bowl = Bowl(canvas)
        self.apples = [Apple(canvas) for i in range(1)]

        self.__score = 0
        self.__lives = Game_CatchApple.LIVES_BEGIN
        self.text_score = canvas.create_text(620, 30, text=f'SCORE: {self.__score}', fill='red', font=('Times', 20))
        self.text_lives = canvas.create_text(620, 70, text=f'LIVES: {self.lives}', fill='blue', font=('Times', 20))
        self.text_continue = canvas.create_text(350, 225, text=f'Press Space to continue', fill='blue', font=('Times', 20))
        self.text_gameover = canvas.create_text(350, 200, text=f'GAME OVER', fill='red', font=('Times', 30), state='hidden')
        self.text_restart = canvas.create_text(350, 250, text=f'Press Space to restart', fill='red', font=('Times', 20), state='hidden')

        self.__game_over = False
        self.__pause = True

        self.canvas = canvas
        self.canvas.bind_all('<KeyPress>', self.keyPress)

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        self.__score = new_score
        self.canvas.itemconfig(self.text_score, text=f'SCORE: {self.__score}')

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, new_lives):
        self.__lives = new_lives
        self.canvas.itemconfig(self.text_lives, text=f'LIVES: {self.__lives}')

    @property
    def game_over(self):
        return self.__game_over

    @game_over.setter
    def game_over(self, is_game_over):
        self.__game_over = is_game_over
        if is_game_over:
            state = 'normal'
        else:
            state = 'hidden'
        self.canvas.itemconfigure(self.text_gameover, state=state)
        self.canvas.itemconfigure(self.text_restart, state=state)

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, is_pause):
        self.__pause = is_pause
        if is_pause:
            state = 'normal'
        else:
            state = 'hidden'
        self.canvas.itemconfigure(self.text_continue, state=state)

    # Kiểm tra quả táo và cái bát chạm nhau
    def check_bowl_catched_apple(self, apple):
        x_apple, y_apple = apple.coords
        x_bowl, y_bowl = self.bowl.coords
        return (x_apple >= x_bowl and x_apple + 50 <= x_bowl + 120) \
        and (y_apple + 50 >= y_bowl and y_apple + 50 <= y_bowl + 37.5)

    # Sự kiện nhấn phím
    def keyPress(self, event):
        if self.pause:
            if event.keysym=='space':
                self.pause = False
                self.play()
        elif not self.game_over:
            if event.keysym=='Left':
                self.bowl.move(-(20 + self.score * 2))
            elif event.keysym=='Right':
                self.bowl.move(20 + self.score * 2)
            elif event.keysym=='p':
                self.pause = True
        else:
            if event.keysym=='space':
                self.restart()
    

    # Chơi game
    def play(self):
        while not self.game_over and not self.pause:
            for apple in self.apples:
                try:
                    apple.fall(self.score + 10)
                    if apple.y > 550:
                        apple.begin()
                        self.lives -= 1
                        if not self.lives:
                            self.game_over = True
                            break
                    elif self.check_bowl_catched_apple(apple):
                        playsound('music/vacham.wav', block=False)
                        apple.begin()
                        self.score += 1
                    self.canvas.update()
                except:
                    return
            sleep(0.05)

    # Chơi lại
    def restart(self):
        for apple in self.apples:
            apple.begin()
        self.score = 0
        self.lives = Game_CatchApple.LIVES_BEGIN
        self.game_over = False
        self.canvas.update()
        self.play()
