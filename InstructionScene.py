from ControlScene import ControlScene
from NBackScene import NBackScene
from Scene import Scene
from Button import Button
import Settings
import pygame




class InstructionScene(Scene):

    def __init__(self, nback):
        super(InstructionScene, self).__init__()
        self.nBack = nback

    def render(self, screen):
        screen.fill(Settings.white)

        # For control group
        if self.nBack == 0:
            title = Settings.statusFont.render("Please wait and look at the '+' on the screen", True, Settings.black)
            i2 = Settings.statusFont.render(
                "You can quit at anytime by pressing the red button on the top left of the screen", True,
                Settings.black)
            i3 = Settings.statusFont.render(
                "If you understand press the SPACEBAR to begin. If not ask a lab attendant for clarification", True,
                Settings.black)
            screen.blit(title, ((Settings.screenWidth // 2) - title.get_width() // 2, 10))
            screen.blit(i2, ((Settings.screenWidth // 2) - i2.get_width() // 2, 30))
            screen.blit(i3, ((Settings.screenWidth // 2) - i3.get_width() // 2, 50))


        else:
            title = Settings.statusFont.render("N-back working memory task", True, Settings.black)
            i1 = Settings.statusFont.render(
                "You will be shown a sequence of letters. Each letter will be shown for " + str(Settings.secDisp) + " seconds", True,
                Settings.black)
            i2 = Settings.statusFont.render("If the same letter was displayed " + str(
                self.nBack) + " trials ago, Press the SPACEBAR. Otherwise wait for the next letter", True, Settings.black)
            i3 = Settings.statusFont.render("You can quit at anytime by pressing the red button on the top left of the screen", True, Settings.black)
            i4 = Settings.statusFont.render(
                "If you understand press the SPACEBAR to begin. If not ask a lab attendent for clarification", True, Settings.black)

            screen.blit(title, (Settings.mid[0] - title.get_width() // 2, 10))
            screen.blit(i1, (Settings.mid[0] - i1.get_width() // 2, 30))
            screen.blit(i2, (Settings.mid[0] - i2.get_width() // 2, 50))
            screen.blit(i3, (Settings.mid[0] - i3.get_width() // 2, 70))
            screen.blit(i4, (Settings.mid[0] - i4.get_width() // 2, 90))

    def update(self, seconds):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                if self.nBack is 0:
                    self.manager.go_to(ControlScene())
                else:
                    self.manager.go_to(NBackScene(self.nBack))

