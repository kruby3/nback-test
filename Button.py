import pygame
import Settings

class Button(object):
    def __init__(self, topleft, size, color, text, returnInt):
        self.rect = pygame.Rect(topleft, size)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(color)
        self.returnInt = returnInt
        self.text = Settings.bFont.render(text , True, Settings.white)
        self.topleft = topleft
        self.size = size


    def isHit(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def getInt(self):
        return self.returnInt

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        textPos = (self.topleft[0] + (self.size[0] // 2) - (self.text.get_width() // 2), self.topleft[1] + (self.size[1] // 2))
        screen.blit(self.text, textPos)
