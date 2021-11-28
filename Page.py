import pygame

class Page():
    def __init__(self):
        self.PAGE_W = 640
        self.PAGE_H = 480
        self.page_id = 0
        self.display = pygame.Surface((self.PAGE_W, self.PAGE_H))
        self.window = pygame.display.set_mode((self.PAGE_W, self.PAGE_H))
        self.clock = pygame.time.Clock()

    def blit_screen(self):
        self.game.window.blit(self.display, (0, 0))
        self.display.fill((255, 207, 132))
        pygame.display.flip()
        pygame.display.update()
        pygame.display.set_caption("BubbleMath")


    def display_menu(self):
        run_page = True
        while run_page:
            self.clock.tick(60)
            self.game.check_events()
            self.check_input()
            self.display = self.display = pygame.Surface((self.PAGE_W, self.PAGE_H))
            self.window = pygame.display.set_mode(((self.PAGE_W, self.PAGE_H)))
            pygame.Surface.blit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check if Rage Quit
                    run_page = False
            self.blit_screen()


