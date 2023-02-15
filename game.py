import pygame
from sys import exit


# inits bruv:
pygame.init()
screen = pygame.display.set_mode((350, 700))
screen_bg_colour = (42,43,46)
screen.fill(screen_bg_colour)

# Draw board outline:
for x in range(35, 400, 35):
    pygame.draw.line(screen, "black", (x, 0), (x, 700), width = 1)

for y in range(35, 800, 35):
    pygame.draw.line(screen, "black", (0, y), (400, y), width = 1)

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