import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumabsxy import coordsclicker  # Certifique-se de que este módulo está corretamente importado
from login import login_to_game, change_map  # Importe sua função login_to_game do módulo login


def go_to_sauna(driver):
    driver = driver

    pyautogui.hotkey('ctrl', 'f5')
    time.sleep(4)
    map_url = "https://play.pixels.xyz/pixels/DrunkenGooseInterior"
    change_map(driver, map_url)
    if not driver.fullscreen_window():
        driver.fullscreen_window()
    print('going to sauna')
    time.sleep(5)
    # ROTA DA SAUNA
    pyautogui.keyDown('right')
    time.sleep(1.3)  
    pyautogui.keyUp('right')
    
    pyautogui.keyDown('down')
    time.sleep(4)  
    pyautogui.keyUp('down')
    
    pyautogui.keyDown('left')
    time.sleep(1.3)  
    pyautogui.keyUp('left')

    pyautogui.keyDown('down')
    time.sleep(4)  
    pyautogui.keyUp('down')

    # espera carregar proximo mapa

    time.sleep(12)

    pyautogui.keyDown('left')
    time.sleep(2.5)  
    pyautogui.keyUp('left')

    pyautogui.keyDown('up')
    time.sleep(8)  
    pyautogui.keyUp('up')

    pyautogui.keyDown('right')
    time.sleep(1.5)  
    pyautogui.keyUp('right')

    pyautogui.keyDown('up')
    time.sleep(3)  
    pyautogui.keyUp('up')
    
    time.sleep(12)

    pyautogui.keyDown('up')
    time.sleep(8)  
    pyautogui.keyUp('up')

    pyautogui.moveTo(700, 270)
    time.sleep(1)
    pyautogui.click()



def go_to_speck(driver):
    driver = driver
    # CLICAR PARA IR PARA SPECK

    if driver:
        try:
            # Encontrar o elemento da div principal
            div_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'Hud_topLeftBackground__OhgQS'))
            )

            # Encontrar e clicar no primeiro botão dentro da div principal
            buttons = div_element.find_elements(By.CSS_SELECTOR, 'button.Hud_outside__zzIGQ')
            if buttons:
                first_button = buttons[0]
                first_button.click()

            # Aguardar um pouco após o clique
            time.sleep(3)
            # Encontrar o elemento da div principal
            div_element2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'LandAndTravel_mapSquare__LuVEh'))
            )

            # Encontrar e clicar no segundo botão (assumindo que é o botão correto)
            second_button = driver.find_element(By.CSS_SELECTOR, 'div.LandAndTravel_mapsSquare__vG99V button')

            # Clique no botão
            second_button.click()
            print('Going to speck')
        except Exception as e:
            print(f"Erro durante a execução de go_to_speck(): {e}")    
    print('Going to speck')

    time.sleep(10)
    pyautogui.keyDown('left')
    time.sleep(0.2)  
    pyautogui.keyUp('left')
    time.sleep(0.1)   

    pyautogui.keyDown('up')
    time.sleep(3)  
    pyautogui.keyUp('up')
    time.sleep(0.1)


if __name__ == '__main__':
    go_to_sauna()
    driver = login_to_game()
    # if driver:
    #     try:
    #         go_to_sauna(driver)
    #         time.sleep(10)  # Ajustar conforme necessário

    #         # Exemplo de captura de logs do navegador
    #         # get_browser_logs(driver)

    #         time.sleep(999)  # Mantém o programa em execução
    #     except Exception as e:
    #         print(f"Erro durante a execução: {e}")
    #     finally:
    #         driver.quit()
