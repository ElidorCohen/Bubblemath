import pygame
from pymongo.database import Database
from User import UserType
import button
import os
from Database import Database as database
from Page import Page
import MainPage
import MainMenu

class StatisticsPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('myprofile.png')), (self.PAGE_W, self.PAGE_H))
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.return_button = button.Button(20, 15, self.return_image, 0.3)
        self.user = database.getUser(database.user_id)
        self.institute = database.getInstitute(self.user.institute)

    def draw_page(self):
        super(StatisticsPage,self).draw_page()
        self.screen.blit(self.background, (0, 0))
        self.draw_text('Statistics', 70, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 400, 20)
        self.draw_text('Number Of Student: {}'.format(self.institute.num_of_students), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 170)
        self.draw_text('Rank Of The Institute: {}'.format(self.institute.rank), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 220)
        self.return_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            if self.return_button.is_clicked(event):
                return MainMenu.MainMenu()
            if event.type == pygame.QUIT:
                pygame.quit()
        return self
