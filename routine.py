import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumabsxy import coordsclicker  # Certifique-se de que este módulo está corretamente importado
from login import login_to_game  # Importe sua função login_to_game do módulo login


def go_to_sauna(driver):

    #CLICAR PARA IR PARA SAUNA

    
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
                EC.presence_of_element_located((By.CLASS_NAME, 'LandAndTravel_customHeader__goUPo'))
            )

            # Encontrar e clicar no segundo botão (assumindo que é o botão correto)
            second_button = driver.find_element(By.CSS_SELECTOR, 'div.LandAndTravel_customHeader__goUPo button')

            # Clique no botão
            second_button.click()
            print('Going to sauna')
        except Exception as e:
            print(f"Erro durante a execução de go_to_sauna(): {e}")

    time.sleep(10)
    # ROTA DA SAUNA
    def up():
        time.sleep(3)
        pyautogui.keyDown('up')
        time.sleep(1.3)  
        pyautogui.keyUp('up')
    def left():
        time.sleep(3)
        pyautogui.keyDown('left')
        time.sleep(8)  
        pyautogui.keyUp('left')
    
    def last_up():
        time.sleep(3)
        pyautogui.keyDown('up')
        time.sleep(3)  
        pyautogui.keyUp('up')

    up()
    left()
    last_up()
    

def go_to_speck():

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
            print('Going to sauna')
        except Exception as e:
            print(f"Erro durante a execução de go_to_sauna(): {e}")    
    print('Going to speck')

    #ROTA DA SPECK

if __name__ == '__main__':
    driver = login_to_game()
    if driver:
        try:
            go_to_sauna(driver)
            time.sleep(10)  # Ajustar conforme necessário

            # Exemplo de captura de logs do navegador
            # get_browser_logs(driver)

            time.sleep(999)  # Mantém o programa em execução
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            driver.quit()
