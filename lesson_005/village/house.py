
import pygame

yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
fuchsia = (255, 0, 255)
saddlebrown = (139, 69, 19)

smile_eyes = dict(eyes='open')


def wall(screen, x1, y1):
    pygame.draw.rect(screen, saddlebrown, (x1+40, y1+20, 400, 200))
    x = x1
    y = y1

    for j in range(5): # Обозначиваем ряд
        y += 20
        x = x1
        for i in range(10): # Рисуем кирпич
            x += 40
            pygame.draw.rect(screen, (244, 164, 96), (x, y, 40, 20), 2)
        y += 20
        x = x1 + 40
        pygame.draw.rect(screen, (244, 164, 96), (x, y, 20, 20), 2)
        x = x1 + 20
        for i in range(9): # Рисуем кирпич
            x += 40
            pygame.draw.rect(screen, (244, 164, 96), (x, y, 40, 20), 2)
        pygame.draw.rect(screen, (244, 164, 96), (x+40, y, 20, 20), 2)


def window(screen, x, y):
    pygame.draw.rect(screen, yellow, (x + 220, y + 40, 180, 100))



def smile_see(screen, j, smile_eyes=smile_eyes):
    print(smile_eyes)
    if smile_eyes.get('eyes') == 'open':
        # лицо
        pygame.draw.circle(screen, fuchsia, (j[0], j[1]), 25)
        # глаза
        pygame.draw.circle(screen, blue, ((j[0]) - 7.5, (j[1] - 4)), 4)
        pygame.draw.circle(screen, blue, ((j[0]) + 7.5, (j[1] - 4)), 4)
        # улыбка
        pygame.draw.arc(screen, blue, ((j[0]) - 15, (j[1] - 10), 30, 30),
                        3.14 * 1.1, 1.9 * 3.14, 2)
        smile_eyes['eyes'] = 'close'
    elif smile_eyes.get('eyes') == 'close':
        # лицо
        pygame.draw.circle(screen, fuchsia, (j[0], j[1]), 25)
        # глаза
        pygame.draw.line(screen, blue, ((j[0]) - 12.5, (j[1] - 4)), ((j[0]) - 3.5, (j[1] - 4)), 2)
        pygame.draw.line(screen, blue, ((j[0]) + 12.5, (j[1] - 4)), ((j[0]) + 3.5, (j[1] - 4)),2)
        # улыбка
        pygame.draw.arc(screen, blue, ((j[0]) - 15, (j[1] - 10), 30, 30),
                        3.14 * 1.1, 1.9 * 3.14, 2)
        smile_eyes['eyes'] = 'open'

# def smile_sleep(screen, j):
#     # лицо
#     pygame.draw.circle(screen, fuchsia, (j[0], j[1]), 25)
#     # глаза
#     pygame.draw.line(screen, blue, ((j[0]) - 12.5, (j[1] - 4)), ((j[0]) - 3.5, (j[1] - 4)), 2)
#     pygame.draw.line(screen, blue, ((j[0]) + 12.5, (j[1] - 4)), ((j[0]) + 3.5, (j[1] - 4)),2)
#     # улыбка
#     pygame.draw.arc(screen, blue, ((j[0]) - 15, (j[1] - 10), 30, 30),
#                     3.14 * 1.1, 1.9 * 3.14, 2)
