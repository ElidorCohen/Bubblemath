import pygame
import os
from Page import Page
import button
import MainMenu
from InputBox import InputBox

class MessagePage(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('myprofile.png')), (self.PAGE_W, self.PAGE_H))
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.return_button = button.Button(20, 15, self.return_image, 0.3)
        self.send_image = pygame.image.load('send_admin.png').convert_alpha()
        self.send_button = button.Button(430, 590, self.send_image, 0.2)
        self.to_input = InputBox(155, 167, 140, 32)
        self.message_input = InputBox(100, 250, 0, 100)
        self.input_boxes1 = [self.to_input, self.message_input]

    def draw_page(self):
        super(MessagePage,self).draw_page()
        self.screen.blit(self.background, (0, 0))
        self.draw_text('To : ' , 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 170)
        self.return_button.draw(self.screen)
        self.send_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            for box in self.input_boxes1:
                box.handle_event(event)
            if self.return_button.is_clicked(event):
                return MainMenu.MainMenu()
            if self.send_button.is_clicked(event):
                #database.sendReport(self.report_input.text)
                return MainMenu.MainMenu()
            if event.type == pygame.QUIT:
                pygame.quit()
        for box in self.input_boxes1:
            box.update()
        for box in self.input_boxes1:
            box.draw(self.screen)
        return self