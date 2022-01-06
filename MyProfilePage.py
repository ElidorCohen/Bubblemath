import pygame
from pymongo.database import Database
from User import UserType
import button
import os
from Database import Database as database, Report
from Page import Page
import MainPage
import MainMenu
from User import UserType
from InputBox import InputBox

REPORT_Y_OFFSET = 30

class MyProfile(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('myprofile.png')), (self.PAGE_W, self.PAGE_H))
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.edit_image = pygame.image.load('edit.png').convert_alpha()
        self.return_button = button.Button(20, 15, self.return_image, 0.3)
        self.edit_button = button.Button(850, 15, self.edit_image, 0.3)
        self.user = database.getUser(database.user_id)
        self.reports = database.getReports()
        
        self.time_input = InputBox(700, 350, 140, 27)
        self.admin_message_input = InputBox(380, 550, 140, 27)
        self.input_boxes = [self.admin_message_input, self.time_input]
        self.send_image = pygame.image.load('send_admin.png').convert_alpha()
        self.send_button = button.Button(430, 590, self.send_image, 0.2)
        self.send_update_image = pygame.image.load('send_update.png').convert_alpha()
        self.send_update_button = button.Button(40, 650, self.send_update_image, 0.2)
        self.settings_image = pygame.image.load('update_settings.png').convert_alpha()
        self.settings_button = button.Button(710, 400, self.settings_image, 0.2)

    def draw_page(self):
        super(MyProfile,self).draw_page()
        self.screen.blit(self.background, (0, 0))
        self.draw_text('Name: {} ({})'.format(self.user.full_name,self.user.user_type), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 170)
        if(database.user_type == UserType.student.name):
            self.draw_text('score: {}'.format(self.user.score), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 300)
            self.draw_text('Institute: {}'.format(self.user.institute), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 220)
        elif(database.user_type == UserType.counselor.name):
            self.draw_text('Institute: {}'.format(self.user.institute), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 220)
        elif(database.user_type == UserType.admin.name):
            self.draw_text('Admin Message:', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 380, 500)
            self.draw_text('Change Time:', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 700, 300)
            self.send_button.draw(self.screen)
            self.settings_button.draw(self.screen)
            self.send_update_button.draw(self.screen)
            if(self.reports is not None):
                self.draw_reports()
            

        self.return_button.draw(self.screen)
        self.edit_button.draw(self.screen)

    def draw_reports(self):
        self.draw_text('Reports:', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 400,200)
        count = 0
        for i in self.reports:
            self.draw_text('{}'.format(i), 25, 'david.ttf', (0, 0, 0), self.screen, 100, REPORT_Y_OFFSET * count + 250)
            count = count + 1 

    def handle_page(self):
        for event in pygame.event.get():
            if self.return_button.is_clicked(event):
                return MainMenu.MainMenu()
            if self.edit_button.is_clicked(event):
                return MainPage.MainPage()
            if self.send_button.is_clicked(event):
                pass
            if self.send_update_button.is_clicked(event):
                pass
            if event.type == pygame.QUIT:
                pygame.quit()
            for box in self.input_boxes:
                box.handle_event(event)
        if(database.user_type == UserType.admin.name):
            for box in self.input_boxes:
                box.update()
            for box in self.input_boxes:
                box.draw(self.screen)
        return self
