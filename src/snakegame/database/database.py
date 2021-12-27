import pygame, pygame.font, pygame.event, pygame.draw, string
from pip._internal.utils.misc import ask
from pygame.locals import *
import uuid

string=''
current_string_p=[]
display_p=[]
symbol='*'

def get_event_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def show_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)

  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def main():
      global display_p
      display_p = []
      screen = pygame.display.set_mode((320, 240))
      print(ask(screen, "Username") + " was entered")
      x = ask(screen, "Password")
      for character in x:
          display_p.append(symbol)
      pro = ''.join(display_p)
      print(x + " was entered")
      print(pro)

if __name__ == '__main__':
      main()
