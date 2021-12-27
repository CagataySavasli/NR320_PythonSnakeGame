import pygame
import husnu_bey
import NeroCup
import ui

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