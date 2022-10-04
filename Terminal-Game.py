from os import get_terminal_size as gts
from time import sleep

terminal_size = gts()

if terminal_size[0] < 80 or terminal_size[1] < 24:
    print("Please resize terminal so that it is at least 80 columns wide by 24 rows tall")

while True:
    terminal_size = gts()
    if terminal_size[0] >= 80 and terminal_size[1] >= 24:
        break

for i in range(0, terminal_size[1]):
    for j in range(0, terminal_size[0] + 1):
        print(f'\33[{i};{j}H#')

for i in range(0, terminal_size[1]):
    for j in range(0, terminal_size[0] + 1):
        print(f'\33[{i};{j}H ')

for i in range(0, 50):
    print(f'\33[0;{i}H*')

for i in range(0,terminal_size[1]):
    print(f'\33[{i};0H*')
    print(f'\33[{i};49H*')


for i in range(0, 50):
    print(f'\33[{terminal_size[1] - 1};{i}H*')
