import pygame
from sys import exit


# inits bruv
pygame.init()
screen = pygame.display.set_mode((400, 700))
screen_bg_colour = (42,43,46)
screen.fill(screen_bg_colour)

# set the new icon
icon_surface = pygame.Surface((32, 32))
icon_surface.fill((139,0,139))
pygame.display.set_icon(icon_surface)

pygame.display.set_caption("Tetrizz")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # screen.fill((94,129,162))
    # screen.blit(screen, (0, 0))
    pygame.display.update()