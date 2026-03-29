import pygame
pygame.init()
a = pygame.Vector2(3,4)
b = pygame.Vector2(6,7)
c = a.distance_to(b)
print(c)