from Button import Button
from EndScene import EndScene
from Scene import Scene
import pygame
import random
import Settings


class NBackScene(Scene):
    def __init__(self, nback):
        super(NBackScene, self).__init__()
        #Which nback test it is
        self.nback = nback
        self.spacePressed = False
        self.currLetter = getLetter()
        self.nbackLetter = '0'
        #History of all letters
        self.letters = []
        self.letters.append(self.currLetter)
        #Secconds since trial started
        self.trialTimer = 0
        #Seconds since delay period started
        self.delayTimer = 0
        #Number of trials taken
        self.numTrials = 0
        #Number of trials correct
        self.correctTrials = 0
        #Seconds since test started
        self.currTime = None
        self.startTime = None
        #True if in transition state between trials
        self.transitionTrial = False
        self.exitButton = Button((0, 0), (50, 50), pygame.Color("red"), "X", 1)



    def render(self, screen):
        screen.fill(Settings.white)

        #Instruction display
        i1 = Settings.smallInst.render(
            "Press SPACEBAR if current letter is the same as one shown {} trials ago".format(self.nback), True,Settings.black)
        i2 = Settings.smallInst.render(
            "You can quit at anytime by pressing the red button on the top left of the screen", True, Settings.black)

        screen.blit(i1, (Settings.mid[0] - i1.get_width() // 2, 10))
        screen.blit(i2, (Settings.mid[0] - i2.get_width() // 2, 30))


        self.exitButton.draw(screen)


        #If not in transition display letter and timer
        if not self.transitionTrial:
            displayLetter(screen, self.currLetter)
            #displayTime(screen, str(Settings.secDisp - self.trialTimer))
            drawProgressBar(screen, self.trialTimer)




    def update(self, currTime):
        if self.transitionTrial:
            self.updateDelay(currTime)
        else:
            self.updateTrial(currTime)

    def updateTrial(self, currTime):
        #Ensures first trial starts at correct time
        if self.currTime is None:
            self.currTime = currTime
        if self.startTime is None:
            self.startTime = currTime

        self.trialTimer = self.trialTimer + (currTime - self.currTime)
        #print(self.trialTimer)

        self.currTime = currTime

        timesUp = self.trialTimer > Settings.secDisp


        if self.currTime - self.startTime > Settings.time:

            accuracy = float(self.correctTrials) / (self.numTrials + 1)
            self.manager.go_to(EndScene(self.nback, accuracy, self.currTime - self.startTime, True))

        if (timesUp or self.spacePressed):
            #Check if correct action was taken (press space, or wait)
            if not (self.numTrials - self.nback < 0):
                correct = correctNBack(self.letters, self.nback, self.numTrials)
                if (timesUp and not correct) or (self.spacePressed and correct):
                    self.correctTrials += 1

            #Now in delay state
            self.transitionTrial = True
            self.spacePressed = False

    def updateDelay(self, currTime):
        #Update delay timer
        self.delayTimer = self.delayTimer + (currTime - self.currTime)
        #print(self.delayTimer)
        self.currTime = currTime
        #Check if delay state is over
        if self.delayTimer > Settings.secPause:
            self.transitionTrial = False
            self.nextTrial(currTime)


    def nextTrial(self,currTime):
        self.trialTimer = 0
        self.delayTimer = 0
        self.currTime = currTime
        self.currLetter = getLetter()
        self.letters.append(self.currLetter)
        self.numTrials += 1
        self.spacePressed = False

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.spacePressed = True
            if self.exitButton.isHit(e):
                accuracy = float(self.correctTrials) / (self.numTrials + 1)
                self.manager.go_to(EndScene(self.nback, accuracy, self.currTime - self.startTime, False))



def getLetter():
    alphabet = ["A","B","C","D"]
    return random.choice(alphabet)

def displayLetter(screen,aStr):
    text = Settings.letterFont.render(aStr, True, Settings.black)
    screen.blit(text, (Settings.mid[0] - text.get_width() // 2, Settings.mid[1] - text.get_height() // 2))

def displayTime(screen, time):
    text = Settings.statusFont.render(time, True, Settings.black)
    screen.blit(text, (Settings.mid[0] - text.get_width() // 2, 10))

def correctNBack(letters,nback,trial):
    nBackIndex = trial - nback

    if letters[trial] is letters[nBackIndex]:
        return True
    else:
        return False

def drawProgressBar(screen, time):
    width = 100
    topLeft = (Settings.mid[0] - (width / 2) , Settings.mid[1] - 150)

    timeWidth = (float(time) / Settings.secDisp) * width
    size = (width - timeWidth, 25)
    rect = pygame.Rect(topLeft, size)
    image = pygame.Surface(rect.size)
    image.fill(Settings.black)
    screen.blit(image,rect)


