import pygame
import button
from Page import Page
import MainPage
import MyProfilePage
from Database import Database as database
from User import UserType
import StatisticsPage
import Game
import ReportPage
import MessagePage


class MainMenu(Page):
    def __init__(self):
        Page.__init__(self)
        self.play_image = pygame.image.load('play.png').convert_alpha()
        self.myProfile_image = pygame.image.load('my profile.png').convert_alpha()
        self.statistics_image = pygame.image.load('statistics.png').convert_alpha()
        self.report_image = pygame.image.load('report.png').convert_alpha()
        self.disconect_image = pygame.image.load('connect2.png').convert_alpha()
        self.update_image = pygame.image.load('update.png').convert_alpha()
        self.mail_image = pygame.image.load('mail.png').convert_alpha()
        self.share_image = pygame.image.load('share.png').convert_alpha()
        
        self.share_button = button.Button(890, 95, self.share_image, 0.18)
        self.play_button = button.Button(360, 300, self.play_image, 0.35)
        self.myProfile_button = button.Button(340, 400, self.myProfile_image, 0.35)
        self.statistics_button = button.Button(357, 500, self.statistics_image, 0.35) 
        self.report_button = button.Button(780, 645, self.report_image, 0.3)
        self.disconect_button = button.Button(1, 650, self.disconect_image, 0.3)
        self.update_button = button.Button(890, 40, self.update_image,0.2)
        self.mail_button = button.Button(30, 40, self.mail_image, 0.7)
        self.user = database.getUser(database.user_id)

    def draw_page(self):
        super(MainMenu,self).draw_page()
        self.draw_text('Welcome {}'.format(self.user.full_name), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 410, 20)
        self.draw_text('BubbleMath', 100, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 230, 150)
        self.draw_text('Admin Message', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 50, 300)
        self.draw_text('its here', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 20, 350)
        self.play_button.draw(self.screen)
        self.myProfile_button.draw(self.screen)
        if(database.user_type == UserType.counselor.name):
            self.statistics_button.draw(self.screen)
            self.report_button.draw(self.screen)
        self.disconect_button.draw(self.screen)
        self.update_button.draw(self.screen)
        self.mail_button.draw(self.screen)
        self.share_button.draw(self.screen)

    def handle_page(self):
        for event in pygame.event.get():
            if self.play_button.is_clicked(event):
                print("play")
                return Game.Game()
            if self.myProfile_button.is_clicked(event):
                print("my profile")
                return MyProfilePage.MyProfile()
            if self.statistics_button.is_clicked(event):
                print("statistics_button")
                return StatisticsPage.StatisticsPage()
            if self.report_button.is_clicked(event):
                print("report_button")
                return ReportPage.ReportPage()
            if self.disconect_button.is_clicked(event):
                print("disconect_buttone")
                database.disconnect()
                return MainPage.MainPage()
            if self.update_button.is_clicked(event):
                print("update_button")
                #return MyProfile.MyProfile
            if self.share_button.is_clicked(event):
                print("Share_button")
                pass
            if self.mail_button.is_clicked(event):
                print("mail_button")
                return MessagePage.MessagePage()
            if event.type == pygame.QUIT:
                pygame.quit()
        return self