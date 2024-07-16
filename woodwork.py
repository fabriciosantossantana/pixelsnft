import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from login import login_to_game
from routine import go_to_speck


# def login_to_game():
#     debugger_address = "127.0.0.1:9222"
    
#     chrome_opt = webdriver.ChromeOptions()
#     chrome_opt.debugger_address = debugger_address

#     # Adicionando capacidade para capturar logs do navegador
#     chrome_opt.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

#     print(f'Conectando ao Chrome com debugger address {debugger_address}...')
    
#     try:
#         driver = webdriver.Chrome(options=chrome_opt)
#     except Exception as e:
#         print(f"Erro ao inicializar o driver: {e}")
#         return None
    
#     # Navegar para a URL do jogo
#     url_do_jogo = "http://play.pixels.xyz"
#     driver.get(url_do_jogo)
#     print(f'Navegando para {url_do_jogo}...')
    
#     return driver


def first_position_wood():

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

    pyautogui.keyDown('left')
    time.sleep(0.24)  
    pyautogui.keyUp('left')

    pyautogui.keyDown('up')
    time.sleep(4.25)  
    pyautogui.keyUp('up')

    pyautogui.keyDown('left')
    time.sleep(5.5)  
    pyautogui.keyUp('left')


def woodwork(driver):
    coordenadas = {
        'cooking1': (610, 170),
        'cooking2': (610, 310),
        'cooking3': (610, 500),
        'cooking4': (810, 170),
        'cooking5': (810, 310),
        'cooking6': (810, 500),  
    }

    def steps_woodwork(name_item):
        crafting = None  # Declaração de 'crafting' dentro da função steps_woodwork
        for name, coord in coordenadas.items():
            try:
                pyautogui.click(coord)
                time.sleep(0.1)
                pyautogui.click(coord)

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_recipeSection__2_HQt")))

                print(f"Livro foi aberto para {name}")

                item = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//span[text()='{name_item}']"))
                )

                item.click()

                crafting = crafting_check(driver)
                print(f'Valor do crafting check {crafting}')

                create_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_craftingButton__Qd6Ke")))
                print(f'clicou para preparar {name_item}')
                create_button.click()
                time.sleep(0.2)
                create_button.click()

                close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Crafting_craftingCloseButton__ZbHQF")))
                print('clicou para fechar a janela')
                close_button.click()

            except TimeoutException as e:
                print(f"Erro ao preparar item na coordenada {name}: {e}")
            except Exception as e:
                print(f"Erro inesperado ao preparar item na coordenada {name}: {e}")
        print(f'Valor final do crafting: {crafting}')        
        return crafting
    
    pyautogui.keyDown('right')
    time.sleep(0.85)
    pyautogui.keyUp('right')

    # Executando a função steps_woodwork e capturando o valor retornado
    crafting = steps_woodwork('Glue')
    print(f'Primeira execução de steps_woodwork: {crafting}')
    
    pyautogui.keyDown('right')
    time.sleep(1.8)
    pyautogui.keyUp('right')

    crafting = steps_woodwork('Glue')
    print(f'Segunda execução de steps_woodwork: {crafting}')

    pyautogui.keyDown('right')
    time.sleep(3.4)
    pyautogui.keyUp('right')

    crafting = steps_woodwork('Glue')
    print(f'Terceira execução de steps_woodwork: {crafting}')
    
    pyautogui.keyDown('right')
    time.sleep(1.8)
    pyautogui.keyUp('right')

    crafting = steps_woodwork('Glue')
    print(f'Quarta execução de steps_woodwork: {crafting}')

    pyautogui.keyDown('left')
    time.sleep(9.5)
    pyautogui.keyUp('left')

    # Esperar até que termine de cozinhar
    time.sleep(100)

    print(f'Quarta execução de steps_woodwork: {crafting}')

    return crafting

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
    driver = login_to_game()
    while driver:
        woodwork(driver)

