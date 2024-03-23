import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

white = (255, 255, 255)
red = (255, 0, 0)

x = 25
y = 25

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 20
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20


    x = max(25, min(x, 775)) # x не будет меньше 25 (левая граница экрана) и не будет больше 800 - 25 (правая граница экрана)
    y = max(25, min(y, 575)) # ограничивает значение y таким образом, чтобы оно не выходило за верхнюю (25) и нижнюю (600 - 25) границы экрана

    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), 25)
    #pygame.draw.rect(screen, red, (0,0,50,50))
    pygame.display.flip()
    pygame.time.delay(60)
