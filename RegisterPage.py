import pygame
from User import UserType
import button
from InputBox import InputBox
from Page import Page
import MainPage
from Database import Database as database

class RegisterPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.done_image = pygame.image.load('done.png').convert_alpha()
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.done_button = button.Button(500, 500, self.done_image, 0.3)
        self.return_button = button.Button(5, 640, self.return_image, 0.3)
        self.user_input = InputBox(250, 170, 140, 32)
        self.password_input = InputBox(250, 220, 140, 32)
        self.institute_input = InputBox(250, 260, 140, 32)
        self.id_input = InputBox(250, 300, 140, 32)
        self.gender_input = InputBox(250, 340, 140, 32)
        self.age_input = InputBox(250, 380, 140, 32)
        self.user_type = None
        self.student_image = pygame.image.load('student.png').convert_alpha()
        self.counselor_image = pygame.image.load('counselor.png').convert_alpha()
        self.input_boxes1 = [self.user_input, self.password_input, self.institute_input, self.id_input, self.gender_input, self.age_input]
        self.student_button = button.Button(260, 420, self.student_image, 0.10)
        self.counselor_button = button.Button(360, 420, self.counselor_image, 0.10)

    def draw_page(self):
        super(RegisterPage,self).draw_page()
        self.draw_text('Register', 70, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 430, 30)  # x , y
        self.draw_text('Name: ', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 170)
        self.draw_text('Password: ', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 220)
        self.draw_text('Institute: ', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 260)
        self.draw_text('Id: ', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 300)
        self.draw_text('Gender: ', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 340)
        self.draw_text('Age: ', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 380)
        self.draw_text('userType: ', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 420)
        self.done_button.draw(self.screen)
        self.return_button.draw(self.screen)
        self.student_button.draw(self.screen)
        self.counselor_button.draw(self.screen)
     
    def handle_page(self):
        for event in pygame.event.get():
            for box in self.input_boxes1:
                box.handle_event(event)
            if self.student_button.is_clicked(event):
                self.user_type = UserType.student
            if self.counselor_button.is_clicked(event):
                self.user_type = UserType.counselor
            if self.done_button.is_clicked(event):
                registered = self.database.register(self.user_input.text, self.user_input. self.text, self.user_input.text, self.password_input.text, self.gender_input.text, self.institute_input.text, self.age_input.text, self.id_input.text)
                if registered:
                    return #Guide.Guide()
            if self.return_button.is_clicked(event):
                print("return")
                return MainPage.MainPage()
            if event.type == pygame.QUIT:
                pygame.quit()
        for box in self.input_boxes1:
            box.update()
        for box in self.input_boxes1:
            box.draw(self.screen)
        return self

                
