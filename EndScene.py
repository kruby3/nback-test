import pygame

import Settings
from Button import Button
from Scene import Scene
import StartScene


class EndScene(Scene):

    def __init__(self, nback, accuracy, time, didWait):
        super(EndScene, self).__init__()
        self.buttons = []
        self.nback = nback
        self.accuracy = accuracy
        self.time = time
        self.didWait = didWait
        self.exitButton = Button((0, 0), (50, 50), pygame.Color("red"), "X", 1)

    def render(self, screen):
        screen.fill(Settings.white)
        title = Settings.statusFont.render("Complete, please notify lab instructor, Do not exit", True, Settings.black)
        if self.nback != 0:
            i1 = Settings.statusFont.render(str(self.nback) + "-back test", True, Settings.black)
        else:
            i1 = Settings.statusFont.render("Control group", True, Settings.black)

        i2 = Settings.statusFont.render("Accuracy: " + str(self.accuracy), True, Settings.black)
        min = self.time / 60
        sec = self.time % 60
        i3 = Settings.statusFont.render("Time: {:0>2}:{:0>2}".format(int(min),int(sec)), True, Settings.black)
        i4 = Settings.statusFont.render("Did delay gratification? %s" % (str(self.didWait)), True, Settings.black)


        screen.blit(title, (Settings.mid[0] - title.get_width() // 2, 10))
        screen.blit(i1, (Settings.mid[0] - i1.get_width() // 2, 50))
        screen.blit(i2, (Settings.mid[0] - i2.get_width() // 2, 90))
        screen.blit(i3, (Settings.mid[0] - i3.get_width() // 2, 130))
        screen.blit(i4, (Settings.mid[0] - i4.get_width() // 2, 170 ))

        self.exitButton.draw(screen)

    def update(self, seconds):
        pass

    def handle_events(self, events):
        for e in events:
            if self.exitButton.isHit(e):
                raise SystemExit