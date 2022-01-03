import pygame
import os

class Page(object):

    pygame.display.set_caption("BubbleMath")
    def __init__(self):
        self.PAGE_W = 1000
        self.PAGE_H = 720
        self.screen = pygame.display.set_mode((self.PAGE_W,self.PAGE_H))
        self.page_id = 0
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('background.png')), (self.PAGE_W, self.PAGE_H))
        self.run_page = True
        self.display = pygame.Surface((self.PAGE_W, self.PAGE_H))
        self.clock = pygame.time.Clock()

    def display_menu(self):
        self.run_page = True
        while self.run_page:
            #self.screen.blit(self.background, (0, 0))
            #self.window.fill(self.background_colour)
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check if Rage Quit
                    self.run_page = False

    # Draw the text ---------------------------------------------- #
    def draw_text(self,text, size, font, color, surface, x, y):
        font = pygame.font.Font(font, size)
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        surface.blit(textobj, (x, y))

    def draw_page(self):
        self.screen.blit(self.background, (0, 0))
        #self.screen.fill(self.background)

    def handle_page(self):
        return self