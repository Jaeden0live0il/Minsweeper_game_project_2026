import pygame as pg 
import time
import numpy

#Sprite management for tiles and mines
class Tiles(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 25, y + 25)

#make a group object to hold tile sprites
tileGroup = pg.sprite.Group()

#initialize array/grid fo kabooms 
temp2D = numpy.arange(1, 253, 1).reshape(14, 18)
mineField = []

for y in range(14):
    
    for x in range(18):
                   
        if y % 2 == 0:
            if x % 2 == 0:
                mineField.append(Tiles(x * 50, y * 50 + 100, (0, 100, 0)))
                tileGroup.add(Tiles(x * 50, y * 50 + 100, (0, 100, 0)))
            else: 
                mineField.append(Tiles(x * 50, y * 50 + 100, (0, 250, 0)))
                tileGroup.add(Tiles(x * 50, y * 50 + 100, (0, 250, 0)))
        else:
            if x % 2 == 0:
                mineField.append(Tiles(x * 50, y * 50 + 100, (0, 250, 0)))
                tileGroup.add(Tiles(x * 50, y * 50 + 100, (0, 250, 0)))
            else:
                mineField.append(Tiles(x * 50, y * 50 + 100, (0, 100, 0)))
                tileGroup.add(Tiles(x * 50, y * 50 + 100, (0, 100, 0)))
        
pg.init()
#leave 700 y pixels for mines and rest for menu
screen = pg.display.set_mode((900, 800))

# fps control (60 fps)
clock = pg.time.Clock()
clock.tick(60)

#game loop
run = True
while run == True:

    #menu top
    pg.draw.rect(screen, (200, 200, 200), (0, 0, 900 , 100))

    tileGroup.update()
    tileGroup.draw(screen)

    # Closes if u click x
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip() 

pg.quit()


