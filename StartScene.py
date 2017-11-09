from InstructionScene import InstructionScene
from Scene import Scene
from Button import Button
import Settings
import pygame




class StartScene(Scene):

    def __init__(self):
        super(StartScene, self).__init__()
        self.buttons = []

    def render(self, screen):
        screen.fill(Settings.white)
        title = Settings.statusFont.render("WAIT FOR LAB INSTRUCTOR to select n-back test", True, Settings.black)
        screen.blit(title, (Settings.mid[0] - title.get_width() // 2, 10))

        b1 = Button((Settings.mid[0] - 150, 90), (300, 80), pygame.Color("blue"), "1", 1)
        b2 = Button((Settings.mid[0] - 150, 180), (300, 80), pygame.Color("blue"), "2", 2)
        b3 = Button((Settings.mid[0] - 150, 270), (300, 80), pygame.Color("blue"), "3", 3)
        b4 = Button((Settings.mid[0] - 150, 360), (300, 80), pygame.Color("blue"), "Control", 0)
        self.buttons = [b1, b2, b3, b4]

        for button in self.buttons:
            button.draw(screen)

    def update(self, seconds):
        pass

    def handle_events(self, events):
        for event in events:
            for button in self.buttons:
                if button.isHit(event):
                    nBack = button.getInt()
                    self.manager.go_to(InstructionScene(nBack))

