import pygame

import Settings
from EndScene import EndScene
from Button import Button


class ControlScene(object):


    def __init__(self):
        self.trialTimer = 0
        self.currTime = None
        self.exitButton = Button((0, 0), (50, 50), pygame.Color("red"), "X", 1)
        self.controlText = Settings.letterFont.render('+', True, Settings.black)
        self.startTime = None


    def render(self, screen):
        screen.fill(Settings.white)
        self.exitButton.draw(screen)
        screen.blit(self.controlText, (Settings.mid[0] - self.controlText.get_width() // 2, Settings.mid[1] - self.controlText.get_height() // 2))

        # Instruction display
        i1 = Settings.smallInst.render("Please wait and look at the '+' on the screen", True, Settings.black)
        i2 = Settings.smallInst.render(
            "You can quit at anytime by pressing the red button on the top left of the screen", True,
            Settings.black)

        screen.blit(i1, (Settings.mid[0] - i1.get_width() // 2, 10))
        screen.blit(i2, (Settings.mid[0] - i2.get_width() // 2, 30))

    def update(self, currTime):
        if self.currTime is None:
            self.currTime = currTime
        if self.startTime is None:
            self.startTime = currTime

        self.trialTimer = self.trialTimer + (currTime - self.currTime)

        self.currTime = currTime

        if self.currTime - self.startTime > Settings.time:
            self.manager.go_to(EndScene(0, 1, self.currTime, True))

    def handle_events(self, events):
        for e in events:
            if self.exitButton.isHit(e):
                self.manager.go_to(EndScene(0, 1, self.currTime, False))