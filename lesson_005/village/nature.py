
import pygame

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (128, 0, 128)

def rainbow_line(screen):
    rainbow = (red, orange, yellow, green, cyan, blue, purple)
    x1 = 50
    y1 = 50
    x2 = 350
    y2 = 450
    screen.fill((255, 255, 255))

    for i in rainbow:
        x1 += 5
        x2 += 5
        pygame.draw.line(screen, i, [x1, y1], [x2, y2], 4)

def rainbow_oval(screen):
    rainbow = (red, orange, yellow, green, cyan, blue, purple)
    screen.fill((255, 255, 255))

    xr = 600
    yr = 1250

    for i in rainbow:
        yr -= 5
        pygame.draw.circle(screen, i, [xr, yr], 900, 4)

