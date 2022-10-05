from os import get_terminal_size as gts
from time import sleep

import pygame

pygame.init()
win = pygame.display.set_mode((10,10), 0, 32)

def clearScr(terminal_size):
    for i in range(0, terminal_size[1]):
        for j in range(0, terminal_size[0] + 1):
            print(f'\33[{i};{j}H ')

def drawBoard(terminal_size):
    for i in range(0, 50):
        print(f'\33[2;{i}H*')

    for i in range(2,terminal_size[1]):
        print(f'\33[{i};0H*')
        print(f'\33[{i};49H*')


    for i in range(0, 50):
        print(f'\33[{playfieldy};{i}H*')

terminal_size = gts()

if terminal_size[0] < 80 or terminal_size[1] < 24:
    print("Please resize terminal so that it is at least 80 columns wide by 24 rows tall")

while True:
    terminal_size = gts()
    if terminal_size[0] >= 80 and terminal_size[1] >= 24:
        break

playfieldx = 50
playfieldy = terminal_size[1] - 1

for i in range(0, terminal_size[1]):
    for j in range(0, terminal_size[0] + 1):
        print(f'\33[{i};{j}H#')

clearScr(terminal_size)

drawBoard(terminal_size)

posx = int(playfieldx / 2)
posy = int(playfieldy / 2)
while True:
    for event in pygame.event.get():
        if event.key == pygame.KEYDOWN:
            print('\33[1;1HYou pressed up', end = '', flush=True)
        try:
            print(f'\33[1;51H{posx}:{posy}')
            print(f'\33[{posy};{posx}H0')
            print('\33[1;1H', end = '', flush=True)
            sleep(0.1)
            clearScr(terminal_size)
            drawBoard(terminal_size)

            posx += 1
            if posx >= playfieldx - 1:
                posx = 2
        except KeyboardInterrupt:
            clearScr(terminal_size)
            print('\33[1;1HYou chose to exit, goodbye')
            break
