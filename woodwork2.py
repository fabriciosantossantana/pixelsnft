import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from login import login_to_game
from routine import go_to_speck
from login import use_wine


def login_to_game():
    debugger_address = "127.0.0.1:9222"
    
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.debugger_address = debugger_address

    # Adicionando capacidade para capturar logs do navegador
    chrome_opt.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    print(f'Conectando ao Chrome com debugger address {debugger_address}...')
    
    try:
        driver = webdriver.Chrome(options=chrome_opt)
    except Exception as e:
        print(f"Erro ao inicializar o driver: {e}")
        return None
    
    # Navegar para a URL do jogo
    #url_do_jogo = "https://play.pixels.xyz"
    #driver.get(url_do_jogo)
    #print(f'Navegando para {url_do_jogo}...')
    
    return driver



def start_position_woodwork2():
    pyautogui.keyDown('left')
    time.sleep(5)
    pyautogui.keyUp('left')

    pyautogui.keyDown('right')
    time.sleep(1.2)
    pyautogui.keyUp('right')

def woodwork2(driver):
    coordenadas = {
        'woodwork1': (500, 300),
        'woodwork2': (500, 435),
        'woodwork3': (700, 435),
        'woodwork4': (700, 300),
        'woodwork5': (700, 160),
        'woodwork6': (500, 160),  
    }

    coordenadas2 = {
        'woodwork1': (500, 280),
        'woodwork2': (500, 425),
        'woodwork3': (700, 425),
        'woodwork4': (700, 280),  
    }

    
    coordenadas3 = {
        'woodwork1': (800, 450),
        'woodwork2': (800, 320),
        'woodwork3': (800, 180),  
    }

    coordenadas4 = {
        'woodwork1': (800, 425),
        'woodwork3': (800, 280),  
    }

    coordenadas5 = {
        'woodwork1': (600, 445),
        'woodwork2': (600, 300),
        'woodwork3': (600, 150),

        'woodwork4': (800, 445),
        'woodwork5': (800, 300),
        'woodwork6': (800, 150),
    }

    coordenadas6 = {
        'woodwork1': (600, 275),
        'woodwork2': (600, 420),
        'woodwork3': (800, 275),
        'woodwork4': (800, 420),  
    }

    coordenadas7 = {
        'woodwork1': (800, 445),
        'woodwork2': (800, 300),
        'woodwork3': (800, 155),
        'woodwork4': (1000, 445),
        'woodwork5': (1000, 300),  
        'woodwork6': (1000, 155),
    }


    def reposition_row():
        pyautogui.keyDown('down')
        time.sleep(2)
        pyautogui.keyUp('down')

        pyautogui.keyDown('right')
        time.sleep(0.95)
        pyautogui.keyUp('right')

    def reposition_side():

        pyautogui.keyDown('right')
        time.sleep(1.5)
        pyautogui.keyUp('right')

    def reposiotion_start_loop():        
        pyautogui.keyDown('left')
        time.sleep(3.2)
        pyautogui.keyUp('left')

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
    
    
    def steps_woodwork2(name_item):
        crafting = None  # Declaração de 'crafting' dentro da função steps_woodwork
        for name, coord in coordenadas2.items():
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
    
    def steps_woodwork3(name_item):
        crafting = None  # Declaração de 'crafting' dentro da função steps_woodwork
        for name, coord in coordenadas3.items():
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


    def steps_woodwork4(name_item):
        crafting = None  # Declaração de 'crafting' dentro da função steps_woodwork
        for name, coord in coordenadas4.items():
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
    
    def steps_woodwork5(name_item):
        crafting = None  # Declaração de 'crafting' dentro da função steps_woodwork
        for name, coord in coordenadas5.items():
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
    
    def steps_woodwork6(name_item):
        crafting = None  # Declaração de 'crafting' dentro da função steps_woodwork
        for name, coord in coordenadas6.items():
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
    
    def steps_woodwork7(name_item):
        crafting = None  # Declaração de 'crafting' dentro da função steps_woodwork
        for name, coord in coordenadas7.items():
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
    

    # Executando a função steps_woodwork e capturando o valor retornado
    start_position_woodwork2()

    name_of_item = 'Craftbark Plank'

    time.sleep(0.3)
    crafting = steps_woodwork(name_of_item)
    print(f'Primeira execução de steps_woodwork: {crafting}')
    
    
    pyautogui.keyDown('up')
    time.sleep(2)
    pyautogui.keyUp('up')


    time.sleep(0.3)
    crafting = steps_woodwork2(name_of_item)

    reposition_row()

    time.sleep(0.3)
    crafting = steps_woodwork3(name_of_item)

    pyautogui.keyDown('up')
    time.sleep(2)
    pyautogui.keyUp('up')

    time.sleep(0.3)
    crafting = steps_woodwork4(name_of_item)

    reposition_row()

    reposition_side()

    time.sleep(0.3)
    crafting = steps_woodwork5(name_of_item)

    pyautogui.keyDown('up')
    time.sleep(2)
    pyautogui.keyUp('up')

    time.sleep(0.3)
    crafting = steps_woodwork6(name_of_item)

    reposition_row()

    pyautogui.keyDown('right')
    time.sleep(0.95)
    pyautogui.keyUp('right')

    time.sleep(0.3)
    crafting = steps_woodwork7(name_of_item)

    reposiotion_start_loop()
    
    time.sleep(70)
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
        energy = woodwork2(driver)
        if energy <= 300:
            use_wine()