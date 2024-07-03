import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from seleniumabsxy import coordsclicker
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def select_game(driver):
    try:
        # Locate the canvas element by its tag name, id, or class name
        canvas = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "canvas"))
        )
        
        # Click on the canvas element
        canvas.click()
        
        # Wait for a few seconds to ensure the game is loaded
        time.sleep(5)
        
        print('Game logado com sucesso')
    except Exception as e:
        print(f"Erro ao selecionar o jogo: {e}")

def login_to_game():
    profile_select = input("Que profile quer usar? ")
    profile_dir = f'Profile {profile_select}'
    user_data_dir = r'C:\Users\Karine\AppData\Local\Google\Chrome\User Data'
    
    chrome_opt = uc.ChromeOptions()
    chrome_opt.add_argument(f'--user-data-dir={user_data_dir}')
    chrome_opt.add_argument(f'--profile-directory={profile_dir}')
    
    print(f'Muito bem, {profile_dir} do Chrome sendo executado...')

    # Adicionando capacidade para capturar logs do navegador
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}
    
    try:
        driver = uc.Chrome(options=chrome_opt, desired_capabilities=capabilities)
    except Exception as e:
        print(f"Erro ao inicializar o driver: {e}")
        return None
    
    coordsclicker.driver = driver
    time.sleep(1)
    
    try:
        driver.get(r"https://play.pixels.xyz/pixels")
        time.sleep(1)
        driver.fullscreen_window()

        # Esperar explicitamente até que o elemento esteja presente
        continer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.Intro_startbutton__QtxEz'))
        )

        # Garantir que o elemento está visível
        WebDriverWait(driver, 10).until(
            EC.visibility_of(continer)
        )
        
        # Clicar no contêiner
        continer.click()
        print("Login realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao logar: {e}")
        driver.quit()
        return None
    
    return driver

def get_browser_logs(driver):
    logs = driver.get_log('browser')
    for log in logs:
        print(log)

if __name__ == "__main__":
    driver = login_to_game()
    if driver:
        try:
            select_game()
            time.sleep(10)  # Ajustar conforme necessário
            
            # Capturar logs do navegador
            get_browser_logs(driver)
            
            time.sleep(999)  # Mantém o programa em execução
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            driver.quit()
