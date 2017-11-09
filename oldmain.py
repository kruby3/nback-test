#white screen btw trials
#change to set time for test 10 min

import random
import pygame

pygame.init()

#important stuff
#nBack = 2
numTests = 22
secDisp = 2
time = 10 * 60
letters = []

numCorrect = 0


#not important stuff
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
green=[0,255,0]
font = pygame.font.SysFont(None, 120, True, False)
statusFont = pygame.font.SysFont(None, 20, True, False)
bFont = pygame.font.SysFont(None, 40, True, False)
screenWidth = 800
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
clock = pygame.time.Clock()


def getLetter():
    alphabet = ["A","B","C","D"]
    return random.choice(alphabet)

def displayMid(aStr):
    text = font.render(aStr, True, black)
    screen.blit(text, ((screenWidth / 2) - text.get_width() // 2, (screenHeight / 2) - text.get_height() // 2))

def newTest():
    screen.fill(white)
    letter = getLetter()
    letters.append(letter)
    displayMid(letter)
    return letter

def isCorrect(nBack, letter, testNum):
    nbackL = letters[testNum - nBack]
    if nbackL is letter:
        return True
    else:
        return False

def displayStatus(seconds):
    pygame.draw.rect(screen, white, (0,0,screenWidth,100))
    sText = font.render(str(seconds),True, black)
    screen.blit(sText,((screenWidth // 2) - sText.get_width() // 2, 10))

def introScreen(nBack):
    screen.fill(white)

    #For control group
    if nBack == 0:
        title = statusFont.render("Please wait and look at the '+' on the screen", True, black)
        i3 = statusFont.render(
            "If you understand press the SPACEBAR to begin. If not ask a lab attendent for clarification", True, black)
        screen.blit(i3, ((screenWidth // 2) - i3.get_width() // 2, 90))
        screen.blit(title, ((screenWidth // 2) - title.get_width() // 2, 10))
        pygame.display.flip()
        return

    title = statusFont.render("N-back working memory task", True, black)
    i1 = statusFont.render("You will be shown a sequence of letters. Each letter will be shown for " + str(secDisp) + " seconds", True, black)
    i2 = statusFont.render("If the same letter was displayed " + str(nBack) + " trials ago, Press the SPACEBAR. Otherwise wait for the next letter", True, black)
    i3 = statusFont.render("If you understand press the SPACEBAR to begin. If not ask a lab attendent for clarification", True, black)

    screen.blit(title,((screenWidth // 2) - title.get_width() // 2, 10))
    screen.blit(i1, ((screenWidth // 2) - i1.get_width() // 2, 50))
    screen.blit(i2, ((screenWidth // 2) - i2.get_width() // 2, 70))
    screen.blit(i3, ((screenWidth // 2) - i3.get_width() // 2, 90))

    pygame.display.flip()


def setUpScreen():
    screen.fill(white)
    title = statusFont.render("WAIT FOR LAB INSTRUCTOR to select n-back test", True, black)
    screen.blit(title, ((screenWidth // 2) - title.get_width() // 2, 10))

    b1 = Button((100, 100), (120, 80), pygame.Color("blue"), "1", 1)
    b2 = Button((250, 100), (120, 80), pygame.Color("blue"), "2", 2)
    b3 = Button((400, 100), (120, 80), pygame.Color("blue"), "3", 3)
    b4 = Button((550, 100), (120, 80), pygame.Color("blue"), "Control", 0)
    buttons = [b1, b2, b3, b4]
    for button in buttons:
        button.draw(screen)
    pygame.display.flip()
    return buttons


def control():
    screen.fill(white)
    displayMid('+')

    startTestTicks = pygame.time.get_ticks()
    secondsElapsed = 0
    pygame.display.flip()
    #print(time)
    #pygame.time.wait(time * 1000)
    while secondsElapsed < time:
        secondsElapsed = (pygame.time.get_ticks() - startTestTicks) / 1000
        displayMid('+')

    screen.fill(white)
    title = statusFont.render("Complete, please notify lab instructor", True, black)
    screen.blit(title, ((screenWidth // 2) - title.get_width() // 2, 10))

    pygame.display.flip()

def overScreen(nback, result):
    screen.fill(white)
    title = statusFont.render("Complete, please notify lab instructor, Do not exit", True, black)
    if nback != 0:
        i1 = statusFont.render(str(nback) +"-back test", True,  black)
    else:
        i1 = statusFont.render("Control group", True, black)

    i2 = statusFont.render("Accuracy: " + str(result), True, black)

    screen.blit(title, ((screenWidth // 2) - title.get_width() // 2, 10))
    screen.blit(i1, ((screenWidth // 2) - i1.get_width() // 2, 50))
    screen.blit(i2, ((screenWidth // 2) - i2.get_width() // 2, 70))
    pygame.display.flip()

def main():

    nBack = 0
    result = 0

    running = True
    setUp = True
    intro = False
    test = False
    over = False

    while running:

        #QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #SetUp Screen
        if setUp:
            buttons = setUpScreen()

            for button in buttons:
                if button.isHit(event):
                    nBack = button.getInt()
                    setUp = False
                    intro = True

        #Intro Screen
        if intro:
            introScreen(nBack)
            for event in pygame.event.get():
                # Hit spacebar
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        intro = False
                        test = True

        #n-back test
        if test:
            if nBack == 0:
                control()
            else:
                result = runTest(nBack)
            test = False
            over = True

        if over:
            overScreen(nBack, result)









def runTest(nBack):
    introScreen(nBack)

    screen.fill(white)
    test = 0
    numCorrect = 0

    letter = newTest()

    startTestTicks = pygame.time.get_ticks()
    secondsElapsed = 0
    startTrialTicks = pygame.time.get_ticks()

    while secondsElapsed < time:
        clock.tick(60)

        hit = False

        #Check input
        for event in pygame.event.get():
            #Quit
            if event.type == pygame.QUIT:
                pygame.quit()
            #Hit spacebar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hit = True
        secondsElapsed = (pygame.time.get_ticks() - startTestTicks) / 1000
        secondsRemaining = (pygame.time.get_ticks() - startTrialTicks) / 1000
        displayStatus(int(secDisp - secondsRemaining))

        target = False
        if test - nBack >= 0:
            target = isCorrect(nBack, letter, test)
           # print target


        if secondsRemaining > secDisp:
            #print("out of time")
            if test - nBack < 0:
                screen.fill(white)
            elif not target:
                screen.fill(white)
                numCorrect += 1
            else:
                screen.fill(white)

            pygame.display.flip()
            pygame.time.wait(1000)
            startTrialTicks = pygame.time.get_ticks()
            letter = newTest()
            test += 1

        elif hit:
            #print("hit space")
            if not target:
                screen.fill(white)
            else:
                screen.fill(white)
                numCorrect += 1

            pygame.display.flip()
            pygame.time.wait(1000)
            startTrialTicks = pygame.time.get_ticks()
            letter = newTest()
            test += 1

        pygame.display.flip()

    result = float(numCorrect + nBack) / test
    return result


class Button(object):
    def __init__(self, topleft, size, color, text, returnInt):
        self.rect = pygame.Rect(topleft, size)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(color)
        self.returnInt = returnInt
        self.text = bFont.render(text , True, white)
        self.topleft = topleft
        self.size = size

    def isHit(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def getInt(self):
        return self.returnInt

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        textPos = (self.topleft[0] + (self.size[0] // 2) - (self.text.get_width() // 2), self.topleft[1] + (self.size[1] // 2))
        screen.blit(self.text, textPos)




if __name__ == "__main__" or __name__ == "main":
    main()