'''
    Criar um bot que vai conseguir jogar o jogo guitar flash
'''

import pyautogui
import keyboard
from time import sleep


while keyboard.is_pressed('1') == False:
    # Informa se na coordenada corresponde a essa cor, parâmetros (coordenada, cor)
    if pyautogui.pixelMatchesColor(512,559, (0,152,0)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(601,562, (255,0,0)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(691,564, (244,244,2)):
        pyautogui.press('j')
        sleep(0.05)      