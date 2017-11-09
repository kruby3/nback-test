import pygame

#this needs to be before any pygame stuff
import sys

pygame.init()

import Settings
from SceneManager import SceneManager

def main():
    screen = pygame.display.set_mode((Settings.screenWidth, Settings.screenHeight), pygame.FULLSCREEN)
    pygame.display.set_caption("NBack Test")
    timer = pygame.time.Clock()
    running = True

    manager = SceneManager()

    startTestTicks = pygame.time.get_ticks()

    while running:
        timer.tick(60)

        #Event Handling
        events = []
        for event in pygame.event.get():
            events.append(event)
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.VIDEORESIZE:
                #screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)


        manager.scene.handle_events(events)

        #Updating
        seconds = float(pygame.time.get_ticks() - startTestTicks) / 1000
        manager.scene.update(seconds)


        manager.scene.render(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__" or __name__ == "main":
    main()