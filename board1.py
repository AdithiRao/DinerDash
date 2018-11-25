import pygame
from pygamegame import PygameGame
from player import Player
import time


class Board1(PygameGame):
    def __init__(self):
        super().__init__(self)
        background = pygame.image.load("images/background1.png")
        self.background = pygame.transform.scale(background, (893, 627))
        self.character = Player(300,300)
        self.drawingChar = self.character.image
        self.greenArrow = pygame.image.load("images/greenArrow.png")
        self.greenArrow = pygame.transform.scale(self.greenArrow, (80, 60))
        self.trashCan = pygame.image.load("images/trashCan.png")
        self.trashCan = pygame.transform.scale(self.trashCan, (100, 80))
        self.pan1 = False
        self.pan2 = False
        self.images ={"images/juice.png": "juice", "images/coffee.png": "coffee",\
        "images/sushi.png": "sushi", "images/nachos.png": "nachos", \
        "images/steak.png": "steak", "images/cabbage.png": "cabbage", \
        "images/uncookedSteak.png": "uncookedSteak", "images/springRolls.png": "springRolls"}
        self.cookedFood = {"cabbage": "springRolls", "uncookedSteak": "steak"}
        self.time = 0
        self.firstClicks = {'firstClickJ1': False, 'firstClickJ2': False, 'firstClickC1': False,\
            'firstClickC2': False, 'firstClickCook1': False, 'firstClickCook2': False, \
            'firstClickS': False, 'firstClickN': False, 'firstClickUS': False, 'firstClickV': False}
        self.doneWaitings = {'firstClickJ1': False, 'firstClickJ2': False, 'firstClickC1': False,\
            'firstClickC2': False, 'firstClickCook1': False, 'firstClickCook2': False, \
            'firstClickS': False, 'firstClickN': False, 'firstClickUS': False, 'firstClickV': False}

    def armChecking(self, food, holding):
        print(self.character.arm1 == None)
        print(self.drawingChar == self.character.image)
        if self.character.arm1 == None and self.drawingChar == self.character.image \
        or ((self.pan1 == True or self.pan2 == True) and \
        len(self.character.holding) == 1):
            print("hi")
            if (self.pan1 == True or self.pan2 == True) and len(self.character.holding) == 1:
                self.character.holding.pop()
            self.drawingChar = self.character.imageOneArm
            self.character.arm1 = food
            self.character.holding.extend([holding])
        elif (self.character.arm2 == None and self.character.arm1 != None \
        and self.drawingChar == \
        self.character.imageOneArm) or (self.pan1 == True or self.pan2 == True
        and len(self.character.holding) == 2):
            self.drawingChar = self.character.imageTwoArm
            if len(self.character.holding) == 2 and self.character.holding[0] in self.cookedFood:
                self.character.arm1 = food
                self.character.holding[0] = holding
            elif len(self.character.holding) == 2 and self.character.holding[1] in self.cookedFood:
                self.character.arm2 = food
                self.character.holding[1] = holding
            else:
                self.character.arm2 = food
                self.character.holding.extend([holding])

    def cooking(self):
        if self.character.holding[0] in self.cookedFood:
            imgFile = "images/" + str(self.cookedFood[self.character.holding[0]]) + ".png"
            self.armChecking(imgFile, self.cookedFood[self.character.holding[0]])
        elif len(self.character.holding) == 2 and self.character.holding[1] in self.cookedFood:
            imgFile = "images/" + str(self.cookedFood[self.character.holding[1]]) + ".png"
            self.armChecking(imgFile, self.cookedFood[self.character.holding[1]])

    def clicking(self, click, image, holding):
        if self.firstClicks[click] == True and self.doneWaitings[click] == True:
            self.armChecking(image, holding)
            self.firstClicks[click] = False
            self.doneWaitings[click] = False
        self.firstClicks[click] = True

    def trash(self):
        if self.character.arm1 != None:
            self.character.arm1 = None
        if self.character.arm2 != None:
            self.character.arm2 = None
        self.drawingChar = self.character.image
        self.character.holding = []

    def mousePressed(self, x, y):
        #machine 1: juice
        if 0 < x < self.width//11 and 0 < y < self.height//5:
            self.moveTo(0, 80)
            self.clicking('firstClickJ1',  "images/juice.png", "juice")
        #machine 2: juice
        elif self.width//11 < x <2*self.width//11 and 0 < y < self.height//5:
            self.moveTo(80, 80)
            self.clicking('firstClickJ2',  "images/juice.png", "juice")
        #machine 1: coffee
        elif 300 < x < 358 and 30 < y < 115:
            self.moveTo(300, 80)
            self.clicking('firstClickC1',  "images/coffee.png", "coffee")
        #machine 2: coffee
        elif 387 < x < 450 and 30 < y < 115:
            self.moveTo(390, 80)
            self.clicking('firstClickC2',  "images/coffee.png", "coffee")
        #pan 1
        elif 522 < x < 572 and 75 < y < 102:
            self.moveTo(520, 80)
            if self.character.holding != []:
                self.pan1 = True
                if self.firstClicks['firstClickCook1'] == True and self.doneWaitings['firstClickCook1'] == True:
                    self.cooking()
                    self.pan1 = False
                    self.firstClicks['firstClickCook1'] = False
                    self.doneWaitings['firstClickCook1'] = False
                self.firstClicks['firstClickCook1'] = True
        #pan 2
        elif 637 < x < 690 and 75 < y < 102:
            self.moveTo(635, 80)
            if self.character.holding != []:
                self.pan2 = True
                if self.firstClicks['firstClickCook1'] == True and self.doneWaitings['firstClickCook1'] == True:
                    self.cooking()
                    self.pan2 = False
                    self.firstClicks['firstClickCook1'] = False
                    self.doneWaitings['firstClickCook1'] = False
                self.firstClicks['firstClickCook1'] = True
        #sushi
        elif 20 < x < 158 and self.height-150 < y < self.height-100:
            self.moveTo(50, self.height-150)
            self.clicking('firstClickS',  "images/sushi.png", "sushi")
        #nachos
        elif 250 < x < 335 and self.height-150 < y < self.height-100:
            self.moveTo(250, self.height-150)
            self.clicking('firstClickN',  "images/nachos.png", "nachos")
        #meat
        elif 518 < x < 596 and self.height-170 < y < self.height-100:
            self.moveTo(520, self.height-170)
            self.armChecking("images/uncookedSteak.png", "uncookedSteak")
        #veggies
        elif 710 < x < 805 and self.height-150 < y < self.height-100:
            self.moveTo(730, self.height-150)
            self.armChecking("images/cabbage.png", "cabbage")
        elif 780 < x < 880 and 200 < y < 280:
            self.moveTo(780, 240)
            self.trash()


    def redrawAll(self, screen):
        background = pygame.image.load("images/background1.png")
        self.background = pygame.transform.scale(background, (893, 627))
        screen.blit(self.background, (-0, 0))
        screen.blit(self.greenArrow, (810, 300))
        screen.blit(self.trashCan, (780, 200))

    def moveTo(self, x2,y2):
        self.character.x = x2
        self.character.y = y2

    def timerFired(self, dt):
        self.time += 1
        for click in self.firstClicks:
            if self.firstClicks[click] == True:
                start = time.time()
                if self.time % 10 == 0:
                    self.doneWaitings[click] = True
                elif self.doneWaitings[click] == False:
                    pass
                    # print(time.time() - start)
