import pygame
import button
import InputBox
from Page import Page
import LoginPage
import RegisterPage

class MainPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.login_image = pygame.image.load('login.png').convert_alpha()
        self.register_image = pygame.image.load('Register.png').convert_alpha()
        self.login_button = button.Button(360, 400, self.login_image, 0.3)
        self.register_button = button.Button(360, 500, self.register_image, 0.3)
        
    def draw_page(self):
        super(MainPage,self).draw_page()
        self.draw_text('BubbleMath', 100, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 230, 200)
        self.login_button.draw(self.screen)
        self.register_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            if self.login_button.is_clicked(event):
                print("login")
                return LoginPage.LoginPage()
            if self.register_button.is_clicked(event):
                return RegisterPage.RegisterPage()
            if event.type == pygame.QUIT:
                pygame.quit()
        return self