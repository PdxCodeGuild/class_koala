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
    if clock() > nextFrame:                         # animate character every 80ms.
        frame = (frame+1)%8                         # There are 8 frames of animation in each direction
        nextFrame += 80                             # modulus 8 allows it to loop

    if keyPressed("right"):
        changeSpriteImage(testSprite, 0*9+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left
        
    elif keyPressed("left"):
        changeSpriteImage(testSprite, 1*10+frame)    
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