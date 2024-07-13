import time
import pyautogui
from itertools import islice
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
    time.sleep(10)

    pyautogui.keyDown('up')
    time.sleep(2)  
    pyautogui.keyUp('up')

    pyautogui.keyDown('left')
    time.sleep(3.65)  
    pyautogui.keyUp('left')


def cooking(driver):
    driver = driver
    crafting = None
    #todas coordenadas

    coordenadas = {
        'cooking1': (580, 490),
        'cooking2': (580, 370),
        'cooking3': (580, 235),
        'cooking4': (700, 235),
        'cooking5': (830, 235),
        'cooking6': (700, 495),
        'cooking7': (830, 488),
   
    }
    
    coordenadas2 = {
        'cooking8': (565, 250),
        'cooking9': (690, 250),
        'cooking10': (820, 250),
        'cooking11': (820, 500),
        'cooking12': (690, 500),
        'cooking13': (570, 500),
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
            item = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, f"//span[text()='{name_item}']"))
            )
            item.click()
            

            crafting_check(driver)
            crafting = crafting_check(driver)
            print(f'Valor do crafting check {crafting}')

            #Clicar para selecionar o botao de criar            
            create_buttom = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_craftingButton__Qd6Ke")))
            print(f'clicou para preparar {name_item}')
            create_buttom.click()
            time.sleep(0.2)
            create_buttom.click()

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

    pyautogui.keyDown('right')
    time.sleep(2)  
    pyautogui.keyUp('right')
    time.sleep(0.5)
    
    for name, coord in coordenadas2.items():
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

            
            crafting_check(driver)
            crafting = crafting_check(driver)
            print(f'Valor do crafting check {crafting}')

            #Clicar para selecionar o botao de criar            
            create_buttom = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_craftingButton__Qd6Ke")))
            print('clicou para prepara Grumkin Loaf')
            create_buttom.click()
            time.sleep(0.2)
            create_buttom.click()

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

    pyautogui.keyDown('left')
    time.sleep(2)  
    pyautogui.keyUp('left')


    #esperar ate que termine de cozinhar
    
    time.sleep(6.5)
    return crafting





            # Fazer a verificação do valor
            # if valor_necessario <= "2":
            #     go_to_market(driver)
            #     sell(driver)
            #     buy(driver)
            #     go_to_speck(driver)
            #     first_position_cooking()
            # else:
            #     print("Recursos suficientes para cozinhar")


def crafting_check(driver):
    try:
        # Aguardar até que pelo menos uma div com a classe específica esteja presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'Crafting_craftingFontQuantities__FDoj9'))
        )

         # Encontrar todas as divs com a classe específica
        div_elements = driver.find_elements(By.CLASS_NAME, 'Crafting_craftingFontQuantities__FDoj9')

        valor_necessario = None
        for div_element in div_elements:
            # Extrair o texto da div
            texto_completo = div_element.text
            print(f"Texto completo encontrado: {texto_completo}")

            # Obter apenas o valor antes da barra
            valor_necessario_str = texto_completo.split('/')[0]
            valor_necessario = int(valor_necessario_str)
            print(f"Valor necessário: {valor_necessario}")
        return valor_necessario
                            
    except Exception as e:
        print(f"Erro durante a verificação dos valores: {e}")
        return None        

if __name__ == '__main__':    
    cooking()

   
