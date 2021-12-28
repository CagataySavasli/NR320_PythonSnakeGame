import pygame

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class husnu_bey:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/husnu_bey.jpg").convert()
        self.direct = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move(self, dirc):
        self.direct = dirc


    def move_on(self):
        #updating husnu_bey's body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        #updating husnu_bey's head
        if self.direct == 'left':
            self.x[0] -= SIZE

        if self.direct == 'right':
            self.x[0] += SIZE

        if self.direct == 'up':
            self.y[0] -= SIZE

        if self.direct == 'down':
            self.y[0] += SIZE

        self.draw()

        def draw(self):
            for i in range(self.length):
                self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

            pygame.display.flip()

        def increase_husnu_bey_length(self):
            self.length += 1
            self.x.append(-1)
            self.y.append(-1)
