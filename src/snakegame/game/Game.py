import pygame
from pygame.locals import *
import NeroCup
import husnu_bey
import ui
import time

SIZE = 40

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Codebasics husnu_bey And Nero Cup Game")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))
        self.husnu_bey = husnu_bey(self.surface)
        self.husnu_bey.draw()
        self.neroCup = NeroCup(self.surface)
        self.neroCup.draw()
        self.showScreen = ui.UI(self.surface)

    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)
        # pygame.mixer.music.stop()


    def reset(self):
        self.husnu_bey = husnu_bey(self.surface)
        self.neroCup = NeroCup(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.showScreen.render_background()
        self.husnu_bey.move_on()
        self.neroCup.draw()
        self.show_score()
        pygame.display.flip()

        #husnu_bey eats nero cup
        for i in range(self.husnu_bey.length):
            if self.is_collision(self.husnu_bey.x[i], self.husnu_bey.y[i], self.neroCup.x, self.neroCup.y):
                self.play_sound("ding")
                self.husnu_bey.increase_husnu_bey_length()
                self.neroCup.move()

        #husnu_bey collides with itself
        for i in range(3, self.husnu_bey.length):
            if self.is_collision(self.husnu_bey.x[0], self.husnu_bey.y[0], self.husnu_bey.x[i], self.husnu_bey.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

        #husnu_bey collides with the boundries of the window
        if not (0 <= self.husnu_bey.x[0] <= 1000 and 0 <= self.husnu_bey.y[0] <= 800):
            self.play_sound('crash')
            raise "Hit the boundry error"

    def show_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.husnu_bey.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def login_panel(self):
        self.showScreen.login_panel()

    def run(self, currentDirec):
        running = True
        pause = False
        self.login_panel()
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT and currentDirec != "right":
                            self.husnu_bey.move("left")
                            currentDirec = "left"

                        if event.key == K_RIGHT and currentDirec != "left":
                            self.husnu_bey.move("right")
                            currentDirec = "right"

                        if event.key == K_UP and currentDirec != "down":
                            self.husnu_bey.move("up")
                            currentDirec = "up"

                        if event.key == K_DOWN and currentDirec != "up":
                            self.husnu_bey.move("down")
                            currentDirec = "down"

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.showScreen.show_game_over(self.husnu_bey.length)
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    currentDirec = "down"
    game = Game()
    game.run(currentDirec)