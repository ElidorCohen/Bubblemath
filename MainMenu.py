import pygame
import button
from Page import Page
import MainPage
import MyProfilePage

class MainMenu(Page):
    def __init__(self):
        Page.__init__(self)
        self.play_image = pygame.image.load('play.png').convert_alpha()
        self.myProfile_image = pygame.image.load('my profile.png').convert_alpha()
        self.statistics_image = pygame.image.load('statistics.png').convert_alpha()
        self.report_image = pygame.image.load('report.png').convert_alpha()
        self.disconect_image = pygame.image.load('connect2.png').convert_alpha()
        self.notifictions_image = pygame.image.load('notifictions.png').convert_alpha()
        self.mail_image = pygame.image.load('mail.png').convert_alpha()
        
        self.play_button = button.Button(360, 300, self.play_image, 0.35)
        self.myProfile_button = button.Button(340, 400, self.myProfile_image, 0.35)
        self.statistics_button = button.Button(357, 500, self.statistics_image, 0.35) 
        self.report_button = button.Button(780, 645, self.report_image, 0.3)
        self.disconect_button = button.Button(1, 650, self.disconect_image, 0.3)
        self.notifictions_button = button.Button(930, 40, self.notifictions_image,0.7)
        self.mail_button = button.Button(30, 40, self.mail_image, 0.7)

    def draw_page(self):
        super(MainMenu,self).draw_page()
        self.draw_text('BubbleMath', 100, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 230, 150)
        self.play_button.draw(self.screen)
        self.myProfile_button.draw(self.screen)
        self.statistics_button.draw(self.screen)
        self.report_button.draw(self.screen)
        self.disconect_button.draw(self.screen)
        self.notifictions_button.draw(self.screen)
        self.mail_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            if self.play_button.is_clicked(event):
                print("play")
                #return Game.Game()
            if self.myProfile_button.is_clicked(event):
                print("my profile")
                return MyProfilePage.MyProfile()
            if self.statistics_button.is_clicked(event):
                print("statistics_button")
                #return MyProfile.MyProfile
            if self.report_button.is_clicked(event):
                print("report_button")
                #return MyProfile.MyProfile
            if self.disconect_button.is_clicked(event):
                print("disconect_buttone")
                return MainPage.MainPage()
            if self.notifictions_button.is_clicked(event):
                print("notifictions_button")
                #return MyProfile.MyProfile
            if self.mail_button.is_clicked(event):
                print("mail_button")
                #return MyProfile.MyProfile
            if event.type == pygame.QUIT:
                pygame.quit()
        return self