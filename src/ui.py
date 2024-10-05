import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import pygame
from src.database import *

class UI():
    str = ''
    current_str_p = []
    display_p = []
    userName = ""
    password = ""
    den1 = ""
    den2 = ""

    button = pygame.Rect(400, 450, 150, 50)

    button2 = pygame.Rect(300, 200, 400, 100)
    button3 = pygame.Rect(325, 230, 150, 50)
    button4 = pygame.Rect(500, 230, 150, 50)

    clock = pygame.time.Clock()
    fps = 60
    size = [200, 200]
    bg = [255, 255, 255]

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

    def render_background(self):
        bg = pygame.image.load("src/assets/background.jpg")
        self.parent_screen.blit(bg, (0,0))

    def show_game_over(self, score,sw):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        gameOver = font.render(f"Game is over {self.userName} !", True, (255, 255, 255))
        self.parent_screen.blit(gameOver, (200, 280))

        line1 = font.render(f"Your score is {score}.", True, (255, 255, 255))
        self.parent_screen.blit(line1, (200, 330))

        maxScore = editScore(self.userName,score)
        line2 = font.render(f"Your Max Score is {maxScore}.", True, (255, 255, 255,))
        self.parent_screen.blit(line2, (200, 380))

        rank = getRank(self.userName)
        line3 = font.render(f"Your rank is {rank[0]} among {rank[1]}.", True, (255, 255, 255,))
        self.parent_screen.blit(line3, (200, 430))

        if sw:
            line4 = font.render("Press ENTER to play again. Press Escape to exit!", True, (255, 255, 255))
            self.parent_screen.blit(line4, (200, 480))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.button.collidepoint(mouse_pos):
                    self.signin()
                    self.show_box(self.den1,self.den2)

                if self.button3.collidepoint(mouse_pos):
                    return False
                if self.button4.collidepoint(mouse_pos):
                    return True

            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass

    def show_box(self, message,slTest):

        self.render_background()
        font = pygame.font.SysFont('arial', 30)

        line1 = font.render("Welcome To NR320", True, (255, 255, 255))
        self.parent_screen.blit(line1, (400, 150))

        line2 = font.render("{} : ".format(slTest), True, (255, 255, 255))
        self.parent_screen.blit(line2, (400, 250))

        if slTest == "Login":
            pygame.draw.rect(self.parent_screen, [255, 0, 0], self.button)
            line3 = font.render("{} : ".format("Signin"), True, (255, 255, 255))
            self.parent_screen.blit(line3, (420, 450))

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

    def ask(self, question,slTest):
        "ask(screen, question) -> answer"
        pygame.font.init()
        current_str_un = []
        self.show_box(question + ": " + self.str.join(current_str_un), slTest)
        running = True
        while running:

            inkey = self.get_key()
            if inkey == K_BACKSPACE:
                current_str_un = current_str_un[0:-1]
            elif inkey == K_RETURN:
                break
            elif inkey == K_LSHIFT or inkey == K_RSHIFT:
                inkey = self.get_key()
                if inkey <= 127:
                    upper_case = inkey - 32
                    current_str_un.append(chr(upper_case))
            elif inkey <= 127:
                current_str_un.append(chr(inkey))
            self.show_box(question + ": " + self.str.join(current_str_un), slTest)
        return self.str.join(current_str_un)
        # password
        global display_p
        global current_str_p
        current_str_p = []
        display_p = []
        pro = ''.join(display_p)
        show_box(screen, question + ": " + pro, slTest)
        while 1:
            inkey = get_key()
            if inkey == K_BACKSPACE:
                current_str_p = current_str_p[0:-1]
                display_p = display_p[0:-1]
            elif inkey == K_RETURN:
                ##      print(display_p))
                break
            elif inkey == K_LSHIFT or inkey == K_RSHIFT:
                inkey = get_key()
                if inkey <= 127:
                    upper_case = inkey - 32
                    for character in current_str_p:
                        display_p.append(symbol)
                    pro = ''.join(display_p)
                    show_box.blit(screen, question + ": " + pro, slTest)
                    current_str_p.append(chr(upper_case))
            elif inkey <= 127:
                for character in current_str_p:
                    display_p.append(symbol)
                pro = ''.join(display_p)
                show_box.blit(screen, question + ": " + pro, slTest)
                current_str_p.append(chr(inkey))
        return display_p

    def exitQues(self):
        font = pygame.font.SysFont('arial', 30)

        pygame.draw.rect(self.parent_screen, [255, 255, 0], self.button2)

        pygame.draw.rect(self.parent_screen, [255, 0, 0], self.button3)
        l2 = font.render("yes", True, (255, 255, 255))
        self.parent_screen.blit(l2, (335, 230))

        pygame.draw.rect(self.parent_screen, [255, 0, 0], self.button4)
        l3 = font.render("no", True, (255, 255, 255))
        self.parent_screen.blit(l3, (520, 230))

        pygame.display.flip()
        return self.get_key()

    def login(self):
        self.den1 = "Username"
        self.den2 = "Login"
        self.userName = self.ask("Username", "Login")
        self.den1 = "Password"
        self.den2 = "Login"
        self.password = self.ask("Password", "Login")


        if not login(self.userName, self.password):
            self.login()
        else:
            if getOnline(self.userName):
                self.login()

        onlineOffline(self.userName,1)

    def signin(self):
        self.userName = self.ask("Username", "Signin")
        self.password = self.ask("Password", "Signin")
        if not checkForSignin(self.userName):
            signin(self.userName, self.password)
        else:
            self.signin()

    def startScreen(self):
        global display_p
        display_p = []
        createTable()
        self.login()
