import time
import pyautogui

def reposition():
    time.sleep(1)
    pyautogui.keyDown('up')
    time.sleep(3)  
    pyautogui.keyUp('up')

def seed(num, clicks, repeats):
    pyautogui.press(num)
    time.sleep(1)
    for _ in range(repeats):
        #movimenta o mouse para posicao inicial e clica
        pyautogui.moveTo(615, 248)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.5)
        #movimenta o mouse para direita e clica
        pyautogui.moveTo(675, 248)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.5)
        #desse um skm 
        pyautogui.keyDown('down')
        time.sleep(0.24)  
        pyautogui.keyUp('down')
        time.sleep(1)
        clicks += 2

        if clicks >= 100 and num == 'num1':
            num = 'num2'
        elif clicks >= 200 and num == 'num2':
            num = 'num3'
        elif clicks >= 300 and num == 'num3':
            num = 'num4' 
        elif clicks >= 400 and num == 'num4':
            num = 'num5'
        elif clicks >= 500 and num == 'num5':
            num = 'num6'
        elif clicks >= 600 and num == 'num6':
            num = 'num7'
    time.sleep(1)
    return num, clicks

def water():
    
    pyautogui.press('num9')
    for _ in range(10):
        #movimenta o mouse para posicao inicial e clica
        pyautogui.moveTo(615, 248)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.5)
        #movimenta o mouse para direita e clica
        pyautogui.moveTo(675, 248)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.5)
        #desse um skm 
        pyautogui.keyDown('down')
        time.sleep(0.24)  
        pyautogui.keyUp('down')
        time.sleep(1)
    pyautogui.press('num9')    
    time.sleep(1)

def right_move():
    pyautogui.keyDown('right')
    time.sleep(0.2)  
    pyautogui.keyUp('right')
    time.sleep(0.2)

def left_move():    
    pyautogui.keyDown('left')
    time.sleep(0.2)  
    pyautogui.keyUp('left')
    time.sleep(0.2)

def harvest():
    pyautogui.press('num8')
    time.sleep(1)
    for _ in range(10):
        #movimenta o mouse para posicao inicial e clica
        pyautogui.moveTo(615, 248)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.5)
        #movimenta o mouse para direita e clica
        pyautogui.moveTo(675, 248)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.5)
        #desse um skm 
        pyautogui.keyDown('down')
        time.sleep(0.24)  
        pyautogui.keyUp('down')
        time.sleep(1)
    pyautogui.press('num8')
    time.sleep(1)
    

def farm():
    clickseed = 0
    num = 'num1'
    while True:
        num, clickseed = seed(num, clickseed, 10)
        reposition()
        water()
        reposition()
        time.sleep(85)
        harvest()
        reposition()
