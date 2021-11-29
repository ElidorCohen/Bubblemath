class Page():
    def __init__(self, screen, w, h, background):
        self.screen = screen
        self.screen_w = w
        self.screen_h = h
        self.background = background
        
class MainMenu(Page):
    def __init__(self, login_image, register_image, login_button ,register_button, screen, w, h, background):
        Page.__init__(self, screen, w, h, background)
        self.page_id = 0
        self.run_MainMenu = True
        self.login_image = login_image
        self.register_image = register_image
        self.login_button = login_button
        self.register_button = register_button


