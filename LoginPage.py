import pygame
import button
import os
from Database import Database as database
from InputBox import InputBox
from Page import Page
import MainPage
import MainMenu

class LoginPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.background_login = pygame.transform.scale(pygame.image.load(os.path.join('background_loginpage.png')), (self.PAGE_W, self.PAGE_H))
        self.connect_image = pygame.image.load('connect.png').convert_alpha()
        self.back_image = pygame.image.load('back.png').convert_alpha()
        self.connect_button = button.Button(395, 490, self.connect_image, 0.3)
        self.back_button = button.Button(10, 620, self.back_image, 0.7)
        self.user_id_input = InputBox(400, 400, 140, 27)
        self.pass_input = InputBox(400, 450, 140, 27)
        self.input_boxes = [self.user_id_input, self.pass_input]

    def draw_page(self):
        super(LoginPage,self).draw_page()
        self.screen.blit(self.background_login, (0, 0))
        self.draw_text('BubbleMath', 100, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 230, 200)
        self.draw_text('Name:', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 288, 400)
        self.draw_text('Password:', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 290, 450)
        self.connect_button.draw(self.screen)
        self.back_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            for box in self.input_boxes:
                box.handle_event(event)
            if self.connect_button.is_clicked(event):
                logged = database.login(self.user_id_input.text, self.pass_input.text)
                if logged:
                    return MainMenu.MainMenu()
                else:
                    print("ERROR LOGGING IN")
            if self.back_button.is_clicked(event):
                return MainPage.MainPage()
            if event.type == pygame.QUIT:
                pygame.quit()
        for box in self.input_boxes:
            box.update()
        for box in self.input_boxes:
            box.draw(self.screen)
        return self
