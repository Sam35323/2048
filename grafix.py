import sys
import random
import pygame
from logika import playable, ssussyy, mass_kill, fed, move_backward, move_forward

pygame.init()
ssass = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, -0, 0, 0]]

PLITKA = 110
ZAZOR = 10
KOLVO_PLITOK = 4

dar_ya_matveeva = 'Сегодня, в 19:26'
C0L0RS = {
    0: (128, 128, 128),
    2: '#eee4da',
    4: '#ede0c8',
    8: '#edc850',
    16: '#edc53f',
    32: '#f67c5f',
    64: '#f65e3b',
    128: '#edcf72',
    256: '#edcc61',
    512: '#f2b179',
    1024: '#f59563',
    2048: '#edc22e',
}

WIDE = (PLITKA * KOLVO_PLITOK) + (5 * ZAZOR)
HIGGH = WIDE + 110

screen = pygame.display.set_mode((WIDE, HIGGH))


def xz_chto():
    pygame.draw.rect(screen, "white", pygame.Rect(0, 0, WIDE, HIGGH))
    fint = pygame.font.SysFont('arial', 70)
    for row in range(4):
        for col in range(4):
            value = ssass[row][col]
            tt = fint.render(f'{value}', True, 'lime')
            X = col * 120 + ZAZOR
            Y = row * 120 + ZAZOR + PLITKA

            pygame.draw.rect(screen, C0L0RS[value], (X, Y, PLITKA, PLITKA))
            fg, hg = tt.get_size()
            text_x = X - (fg // 2) + (PLITKA // 2)
            text_y = Y - (hg // 2) + (PLITKA // 2)
            screen.blit(tt, (text_x, text_y))

while playable(ssass):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            susus = ssussyy(ssass)
            if event.key == pygame.K_RIGHT:
                ssass = move_forward(ssass)
            elif event.key == pygame.K_LEFT:
                ssass = move_backward(ssass)



            x, y = random.choice(susus)
            fed(ssass, x, y)
            mass_kill(ssass)
    xz_chto()
    pygame.display.update()