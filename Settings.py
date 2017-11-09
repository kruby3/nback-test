import pygame

#Testing Conditions

#Total time of test in seconds
time = 10 * 60
#Seconds the letter is displayed on screen
secDisp = 2
#Seconds of pause between trials
secPause = 1

#Screen Dimensions
screenWidth = 800
screenHeight = 480
mid = (screenWidth // 2, screenHeight // 2)

#Fonts
letterFont = pygame.font.SysFont("arial", 120, True, False)
statusFont = pygame.font.SysFont("arial", 20, True, False)
bFont = pygame.font.SysFont("arial", 20, True, False)
smallInst = pygame.font.SysFont("arial", 20, True, False)


#Colors
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
green=[0,255,0]