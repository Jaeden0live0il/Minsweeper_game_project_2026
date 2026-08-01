import pygame as pg 
import time
import numpy
import random

def chooseMines():



    #select random mines and make it into an array
    numMines = 40
    selectedMines = [random.randint(1, 252)]
    while numMines != 0:
        numMines -= 1
            
        currentMine = random.randint(1, 252)
        for z in range(len(selectedMines)):
            if currentMine == selectedMines[z]:
                currentMine = random.randint(1,252)
                numMines += 1
                break
                    
        selectedMines.append(currentMine)  
    return selectedMines
chosenMines = chooseMines()
#print statement is just for debugging mines, to be removed
print(chosenMines)
firstM = True

#Sprite management for tiles and mines
class Tiles(pg.sprite.Sprite):
    def __init__(self, x, y, color, id):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 25, y + 25)
        
        self.id = id
        
    
    def updateColor(self):
        global chooseMines
        if self.id in chosenMines:
            self.image.fill((250, 1, 0))
        else:
            self.image.fill((210, 180, 140))

    #returns true if a sprite was clicked
    def wasClicked(self):
        coords = pg.mouse.get_pos()
        if (coords[0] > self.rect.center[0] - 25 and coords[0] < self.rect.center[0] + 25) and (coords[1] > self.rect.center[1] - 25 and coords[1] < self.rect.center[1] + 25):
            return True
        else:
            return False

    #call for updating mines when clicked      
    def signaled(self):
        global firstM
        global chosenMines

        if self.wasClicked():
            #roll again if first click is a mine
            if firstM:
                x = 0
                while x < len(chosenMines):
                    if chosenMines[x] == self.id:
                        chosenMines = chooseMines()
                        x = 0
                    else:
                        x += 1
                    
                firstM = False
            self.updateColor()

#make a group object to hold tile sprites
mineField = []
mineField = pg.sprite.Group()

#initialize array/grid fo kabooms 
temp2D = numpy.arange(1, 253, 1).reshape(14, 18)
count = 0
for y in range(14):
    
    for x in range(18):
        
        if y % 2 == 0:
            if x % 2 == 0:
                count += 1
                mineField.add(Tiles(x * 50, y * 50 + 100, (0, 100, 0), count))
                
            else: 
                count += 1
                mineField.add(Tiles(x * 50, y * 50 + 100, (0, 250, 0), count))
                
        else:
            if x % 2 == 0:
                count += 1
                mineField.add(Tiles(x * 50, y * 50 + 100, (0, 250, 0), count))
                
            else:
                count += 1
                mineField.add(Tiles(x * 50, y * 50 + 100, (0, 100, 0), count))


# fps control (60 fps)
clock = pg.time.Clock()
clock.tick(60)

#game loop + screen
run = True
pg.init()
screen = pg.display.set_mode((900, 800))

while run == True:

    #menu on top
    pg.draw.rect(screen, (200, 200, 200), (0, 0, 900 , 100))
    #upate screen
    mineField.update()
    mineField.draw(screen)


    for event in pg.event.get():
        # Closes if u click x
        if event.type == pg.QUIT:
            run = False
        #mouse button interaction
        if event.type == pg.MOUSEBUTTONDOWN:
            for tile in mineField:   
                tile.signaled()        

    pg.display.flip() 

pg.quit()
