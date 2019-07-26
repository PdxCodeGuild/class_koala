import pygame

pygame.init()


win = pygame.display.set_mode((1000, 500))

pygame.display.set_caption('My Awsome Game')

x = 50
y = 445
width = 40
height = 50
vel = 10
left = False
right = False
walkcount = 0 


jumping = False
jump_count = 10
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 1000 - width - vel:
        x += vel 
    if not (jumping):

        if keys[pygame.K_SPACE]:
            jumping = True

    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count **2) * 0.5 * neg
            jump_count -= 1

        else:
            jumping = False
            jump_count = 10


    
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()





pygame.quit()



