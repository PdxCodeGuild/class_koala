# import pygame

# pygame.init()


# win = pygame.display.set_mode((1000, 500))

# pygame.display.set_caption('My Awsome Game')

# walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
# walkleft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
# bg = pygame.image.load('dungeon_bg.png')
# char = pygame.image.load('standing.png')


# clock = pygame.time.Clock()


# class player(object):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.vel = 5
#         self.jumping = False
#         self.jump_count = 10
#         self.left = False
#         self.right = False
#         self.walkcount = 0
#         self.standing = True
    
#     def draw(self,win):
#         if self.walkcount + 1 >= 27:
#             self.walkcount = 0 
#         if not (self.standing):
#             if self.left:
#                 win.blit(walkleft[self.walkcount//3], (self.x,self.y))
#                 self.walkcount += 1
#             elif self.right:
#                 win.blit(walkright[self.walkcount//3], (self.x,self.y))
#                 self.walkcount += 1
#         else:
#             if self.right:
#                 win.blit(walkright[0], (self.x, self.y))
#             else: 
#                 win.blit(walkleft[0], (self.x, self.y))    




# def redrawGameWindow():
#     win.blit(bg, (0,0))
#     princess.draw(win)
#     pygame.display.update() 

# #main loop 
# princess = player(20, 435, 40,50)
# run = True

# while run:
#     clock.tick(27)
#     pygame.time.delay(27)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False


#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT] and princess.x > princess.vel:
#         princess.x -= princess.vel
#         princess.left = True
#         princess.right = False
#         princess.standing = False
#     elif keys[pygame.K_RIGHT] and princess.x < 990 - princess.width - princess.vel:
#         princess.x += princess.vel 
#         princess.right = True
#         princess.left = False
#         princess.standing = False
         
#     else: 
#         princess.standing = True
#         princess.walkcount = 0 
#     if not (princess.jumping):
#         if keys[pygame.K_SPACE]:
#             princess.jumping = True
#             princess.right = False
#             princess.left = False 
#             princess.walkcount = 0 

#     else:
#         if princess.jump_count >= -10:
#             neg = 1
#             if princess.jump_count < 0:
#                 neg = -1
#             princess.y -= (princess.jump_count **2) * 0.5 * neg
#             princess.jump_count -= 1

#         else:
#             princess.jumping = False
#             princess.jump_count = 10


#     redrawGameWindow()  
    

# pygame.quit()


import pygame    
from pygame_functions import *

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()


screenSize(1000,362)

setAutoUpdate(False)

spike = makeSprite('spike.png')
moveSprite(spike,700,295,)
showSprite  (spike)


setBackgroundImage('bar_spikes_big.png') 





testSprite  = makeSprite("girl_small2.gif",19)  # links.gif contains 32 separate frames of animation. Sizes are automatically calculated.

moveSprite(testSprite,300,375,True)

showSprite(testSprite)



# Life character sprites (3)
life_sprite = makeSprite('standing.png')
moveSprite(life_sprite,80,10)
showSprite(life_sprite) 


life_sprite = makeSprite('standing.png')
moveSprite(life_sprite,110,10)
showSprite(life_sprite) 

life_sprite = makeSprite('standing.png')
moveSprite(life_sprite,140,10)
showSprite(life_sprite) 


# Lives Label
life_color = "red"
life_line = makeLabel ('Lives:' , 28, 10, 10, life_color)
showLabel(life_line)


# Game music looped 
pygame.mixer.music.load('ninja_p.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)



ypos = 285
yspeed = 0
upthrust = 0


nextFrame = clock()
frame=0




while True:
    if clock() > nextFrame:                         # We only animate our character every 80ms.
        frame = (frame+1)%8                         # There are 8 frames of animation in each direction
        nextFrame += 80                             # so the modulus 8 allows it to loop

    if keyPressed("right"):
        changeSpriteImage(testSprite, 0*9+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left
        
    elif keyPressed("left"):
        changeSpriteImage(testSprite, 1*10+frame)    # and so on
        scrollBackground(5,0)
    
    elif keyPressed('space'):
        upthrust = -2
         
     
    
    else:
       ypos += yspeed
    moveSprite(testSprite, 500, ypos)
    yspeed += 0 + upthrust
    
    # if touching(testSprite, spike):
    #     upthrust = 2
    #     ypos += yspeed
    # moveSprite(testSprite, 500, ypos)
    # yspeed += 0 + upthrust

    

    # else:
    #     changeSpriteImage(testSprite, 1 * 8 + 1)  # the static facing front look

    updateDisplay()
    
    tick(45)

endWait()