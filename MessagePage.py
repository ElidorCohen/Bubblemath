import pygame
import os
from Page import Page
import button
import MainMenu
from InputBox import InputBox
from Database import Database as database
from User import UserType
from Message import Message

MESSAGE_OFFSET = 30

class MessagePage(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('myprofile.png')), (self.PAGE_W, self.PAGE_H))
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.return_button = button.Button(20, 15, self.return_image, 0.3)
        self.send_image = pygame.image.load('send_admin.png').convert_alpha()
        self.send_button = button.Button(430, 590, self.send_image, 0.2)
        self.to_input = InputBox(100, 167, 140, 32)
        self.message_input = InputBox(100, 250, 0, 100)
        self.input_boxes1 = [self.to_input, self.message_input]
        self.messages = database.get_messages()
        self.feedbacks = database.get_feedbacks()

    def draw_page(self):
        super(MessagePage,self).draw_page()
        self.screen.blit(self.background, (0, 0))
        self.draw_text('To : ' , 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 50, 170)
        if database.user_type is not UserType.admin.name:
            self.draw_text('Messages/Feedback' , 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 500, 170)
            count = 0
            for msg in self.messages:
                self.draw_text('From {}: {}'.format(msg.from_user_name, msg.text), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 500, 200 + count * MESSAGE_OFFSET)
                count = count + 1
            for feed in self.feedbacks:
                self.draw_text('Feedback : {}, Grade: {}'.format(feed.text, feed.grade), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 500, 250 + count * MESSAGE_OFFSET)

        self.return_button.draw(self.screen)
        self.send_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            for box in self.input_boxes1:
                box.handle_event(event)
            if self.return_button.is_clicked(event):
                return MainMenu.MainMenu()
            if self.send_button.is_clicked(event):
                database.send_message(self.to_input.text, self.message_input.text)
                return MainMenu.MainMenu()
            if event.type == pygame.QUIT:
                pygame.quit()
        for box in self.input_boxes1:
            box.update()
        for box in self.input_boxes1:
            box.draw(self.screen)
        return self