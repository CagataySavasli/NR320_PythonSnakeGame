import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import uuid

class UI():
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.parent_screen.blit(bg, (0,0))

    def show_game_over(self, score):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {score}", True, (255, 255, 255))
        self.parent_screen.blit(line1, (200, 300))

        line2 = font.render("Press ENTER to play again. Press Escape to exit!", True, (255, 255, 255))
        self.parent_screen.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    str = ''
    current_str_p = []
    display_p = []
    userPass = [["ata","ala"],["cago,sago"]]

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass

    def show_box(self, message):
        "Print a message in a box in the middle of the screen"
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render("Welcome To NR320", True, (255, 255, 255))
        self.parent_screen.blit(line1, (400, 150))
        line2 = font.render("Login : ", True, (255, 255, 255))
        self.parent_screen.blit(line2, (400, 250))
        fontobject = pygame.font.Font(None, 18)
        pygame.draw.rect(self.parent_screen, (0, 0, 0),
                         ((self.parent_screen.get_width() / 2) - 100,
                          (self.parent_screen.get_height() / 2) - 10,
                          200, 20), 0)
        pygame.draw.rect(self.parent_screen, (255, 255, 255),
                         ((self.parent_screen.get_width() / 2) - 102,
                          (self.parent_screen.get_height() / 2) - 12,
                          204, 24), 1)

        if len(message) != 0:
            self.parent_screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                        ((self.parent_screen.get_width() / 2) - 100, (self.parent_screen.get_height() / 2) - 10))
        pygame.display.flip()
