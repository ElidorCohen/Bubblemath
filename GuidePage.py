import pygame
import os
from Page import Page
import button
import MainMenu

class GuidePage(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('Guide_screen.png')), (self.PAGE_W, self.PAGE_H))
        self.understand_image = pygame.image.load('understand.png').convert_alpha()
        self.understand_button = button.Button(840, 650, self.understand_image, 0.2)

    def draw_page(self):
        super(GuidePage,self).draw_page()
        self.screen.blit(self.background, (0, 0))
        self.understand_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            if self.understand_button.is_clicked(event):
                return MainMenu.MainMenu()
            if event.type == pygame.QUIT:
                pygame.quit()
        return self
