import pygame
from pygame.locals import *
import time
import random
import ui
import database

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)


class NeroCup:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("assets/neroCup.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("assets/husnu_bey.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move(self, dirc):
        self.direction = dirc


    def walk(self):
        #updating snake body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        #updating snake head
        if self.direction == 'left':
            self.x[0] -= SIZE

        if self.direction == 'right':
            self.x[0] += SIZE

        if self.direction == 'up':
            self.y[0] -= SIZE

        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_snake_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    colSW = True

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Codebasics Snake And Nero Cup Game")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.neroCup = NeroCup(self.surface)
        self.neroCup.draw()
        self.showScreen = ui.UI(self.surface)

    def play_background_music(self):
        pygame.mixer.music.load('assets/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("assets/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("assets/ding.mp3")

        pygame.mixer.Sound.play(sound)
        # pygame.mixer.music.stop()


    def reset(self):
        self.snake = Snake(self.surface)
        self.neroCup = NeroCup(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False



    def play(self):
        self.showScreen.render_background()
        self.snake.walk()
        self.neroCup.draw()
        self.display_score()
        pygame.display.flip()

        # snake eats nero cup
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.neroCup.x, self.neroCup.y):
                self.play_sound("ding")
                self.snake.increase_snake_length()
                self.neroCup.move()

        # snake collides with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound('crash')
            raise "Hit the boundry error"

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def login(self):
        self.showScreen.startScreen()

    def run(self, currentDirec):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause = True
                        sw = self.showScreen.exitQues()
                        if (not sw) and self.colSW:
                            self.showScreen.show_game_over(self.snake.length, False)
                            time.sleep(2)
                        running = sw
                        pause = not sw

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and currentDirec != "right":
                            self.snake.move("left")
                            currentDirec = "left"

                        if event.key == K_RIGHT and currentDirec != "left":
                            self.snake.move("right")
                            currentDirec = "right"

                        if event.key == K_UP and currentDirec != "down":
                            self.snake.move("up")
                            currentDirec = "up"

                        if event.key == K_DOWN and currentDirec != "up":
                            self.snake.move("down")
                            currentDirec = "down"

                elif event.type == QUIT:
                    pause = True
                    sw = self.showScreen.exitQues()
                    if (not sw) and self.colSW:
                        self.showScreen.show_game_over(self.snake.length, False)
                        time.sleep(2)
                    running = sw
                    pause = not sw
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.colSW = False
                self.showScreen.show_game_over(self.snake.length, True)
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    currentDirec = "down"
    game = Game()
    game.login()
    game.run(currentDirec)