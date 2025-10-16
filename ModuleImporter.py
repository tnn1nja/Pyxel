import Pyxel

from time import sleep
from os import system
for i in range(1,20):
    system("cls")
    Pyxel.display_ngon(i, 100)
    sleep(1)