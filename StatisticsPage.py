import pygame
from pymongo.database import Database
from User import UserType
import button
import os
from Database import Database as database
from Page import Page
import MainPage
import MainMenu
from InputBox import InputBox

class StatisticsPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('myprofile.png')), (self.PAGE_W, self.PAGE_H))
        self.send_feedback_image = pygame.image.load('send_feedback.png').convert_alpha()
        self.send_feedback_button = button.Button(800, 370, self.send_feedback_image, 0.15)
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.return_button = button.Button(20, 15, self.return_image, 0.3)
        self.user = database.getUser(database.user_id)
        self.institute = database.getInstitute(self.user.institute)
        self.feedback_input = InputBox(370, 370, 0, 32)
        self.grades_input = InputBox(600, 370, 0, 32)
        self.input_boxes1 = [self.feedback_input, self.grades_input]

    def draw_page(self):
        super(StatisticsPage,self).draw_page()
        self.screen.blit(self.background, (0, 0))
        self.draw_text('Statistics', 70, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 400, 20)
        self.draw_text('Number Of Student: {}'.format(self.institute.num_of_students), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 170)
        self.draw_text('Rank Of The Institute: {}'.format(self.institute.rank), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 220)
        self.draw_text('Students:', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 450, 285)
        self.draw_text('Feedback', 20, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 410, 340)
        self.draw_text('Grades', 20, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 650, 340)
        #self.draw_student(self)
        self.return_button.draw(self.screen)
        self.send_feedback_button.draw(self.screen)
    
    # def draw_student(self):
    #     count = 0
    #     for i in self.reports:
    #         self.draw_text('{}'.format(i), 25, 'david.ttf', (0, 0, 0), self.screen, 100, REPORT_Y_OFFSET * count + 250)
    #         count = count + 1 

    def handle_page(self):
        for event in pygame.event.get():
            for box in self.input_boxes1:
                box.handle_event(event)
            if self.return_button.is_clicked(event):
                return MainMenu.MainMenu()
            if event.type == pygame.QUIT:
                pygame.quit()
        for box in self.input_boxes1:
            box.update()
        for box in self.input_boxes1:
            box.draw(self.screen)
        return self
