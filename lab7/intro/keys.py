import pygame

# all keyboard key constants available in pygame
print(list(filter(lambda x: "K_" in x, dir(pygame)))) 

print(pygame.K_SPACE)

pygame.init()

print(pygame.key.get_pressed())

print(pygame.key.get_pressed()[pygame.K_SPACE])