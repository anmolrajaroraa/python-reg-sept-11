import pygame
pygame.init()

screenWidth = 1000
screenHeight = 600

# Color - red,green,blue (primary colors) 0-255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
black = 0,0,0
white = 255,255,255
newColor = 131,34,134
x = 0
y = 0
rectWidth = 50
rectHeight = 50
radius = 25
moveX = 1
moveY = 1

screen = pygame.display.set_mode((screenWidth,screenHeight))

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = -1
            elif event.key == pygame.K_UP:
                moveY = -1
            elif event.key == pygame.K_DOWN:
                moveY = 1
            elif event.key == pygame.K_RIGHT:
                moveX = 1

    screen.fill(white)

    # place to draw, color, (x,y,rectWidth,rectHeight)
    # pygame.draw.rect(screen, newColor, (x,y,rectWidth,rectHeight))
    pygame.draw.circle(screen, newColor, (x,y),radius)
    x = x + moveX
    y = y + moveY

    # rectangle conditions
    # if y > screenHeight - rectHeight:
    #     moveY = -1
    # elif x > screenWidth - rectWidth:
    #     moveX = -1
    # elif y < 0:
    #     moveY = 1
    # elif x < 0:
    #     moveX = 1

    if y > screenHeight - radius:
        moveY = -1
    elif x > screenWidth - radius:
        moveX = -1
    elif y < radius:
        moveY = 1
    elif x < radius:
        moveX = 1

    pygame.display.update()    