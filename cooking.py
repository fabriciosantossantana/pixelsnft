import time
import pyautogui
from itertools import islice
from login import check_energy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc
from seleniumabsxy import coordsclicker
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains



# Função para mover para a posição inicial
def first_position_cooking():

    time.sleep(3)
    pyautogui.keyDown('right')
    time.sleep(7)  
    pyautogui.keyUp('right')

    time.sleep(0.2)    
    pyautogui.keyDown('up')
    time.sleep(2.5)  
    pyautogui.keyUp('up')

    time.sleep(0.2)
    pyautogui.keyDown('left')
    time.sleep(0.65)  
    pyautogui.keyUp('left')


    #waiting load map
    time.sleep(5)

    pyautogui.keyDown('up')
    time.sleep(2)  
    pyautogui.keyUp('up')

    pyautogui.keyDown('left')
    time.sleep(3.65)  
    pyautogui.keyUp('left')


def cooking(driver):
    driver = driver
    #todas coordenadas
    coordenadas = {
        'cooking1': (585, 490),
        'cooking2': (585, 360),
        'cooking3': (595, 233),
        'cooking4': (707, 233),
        'cooking5': (830, 233),
        'cooking6': (707, 488),
        'cooking7': (830, 488),
    }
    
    # Exemplo de coordenada para clicar e verificar se a janela aparece
    for name, coord in coordenadas.items():
        try:
            pyautogui.click(coord)
            time.sleep(0.1)
            pyautogui.click(coord)

            # Verificar se a janela apareceu
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_leftPage__S3WpY")))

            # Janela apareceu
            print(f"Livro foi aberto")

            name_item = 'Grumpkin Loaf'
            # Clicar para selecionar grumpkin na lista
            grumpkin_loaf = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Grumpkin Loaf']"))
            )
            grumpkin_loaf.click()

            #Clicar para selecionar o botao de criar            
            create_buttom = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_craftingButton__Qd6Ke")))
            print('clicou para prepara Grumkin Loaf')
            create_buttom.click()

            time.sleep(3)
            #Clicar para fechar a tela
            close_buttom = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_craftingCloseButton__ZbHQF")))
            print('clicou para fechar a janela')
            
            close_buttom.click()
            

        except TimeoutException:
            # Se a janela não aparecer, usar um item para ativar a janela
            print(f"Madeira acabou {coord}, usando item para ativar o fogao...")

            # Aqui usar a madeira
            pyautogui.keyDown('num1')
            time.sleep(0.1)
            pyautogui.moveTo(coord)
            time.sleep(0.1)
            pyautogui.click()     
            pyautogui.keyDown('num1')
    time.sleep(20)

if __name__ == '__main__':    
    cooking()

   
