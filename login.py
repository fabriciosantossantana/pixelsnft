import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from seleniumabsxy import coordsclicker
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def use_wine():
    # Use wine
    time.sleep(3)
    pyautogui.press('num2')
    pyautogui.moveTo(695, 368)
    time.sleep(0.25)
    pyautogui.click(695, 368)
    time.sleep(0.25)
    pyautogui.click(695, 368)
    time.sleep(0.25)
    pyautogui.press('num2')



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
        
        print('Mapa carregado com sucesso')
    except Exception as e:
        print(f"Erro ao selecionar o jogo: {e}")

def login_to_game():
    profile_select = input("Que profile quer usar? ")
    profile_dir = f'Profile {profile_select}'
    user_data_dir = r'C:\Users\Karine\AppData\Local\Google\Chrome\User Data'
    
    chrome_opt = uc.ChromeOptions()
    chrome_opt.add_argument(f'--user-data-dir={user_data_dir}')
    chrome_opt.add_argument(f'--profile-directory={profile_dir}')
    chrome_opt.add_argument('--disable-cache')
        
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
    time.sleep(3)
    
    try:
        driver.get(r"https://play.pixels.xyz/pixels")
        time.sleep(3)
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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_energy(driver):
    try:
        # Localizar o elemento span pelo seletor CSS
        span_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.commons_coinBalance__d9sah.Hud_energytext__3PQZQ'))
        )
        # Obter o texto dentro do span
        span_text = span_element.text

        # Verificar se o valor contém vírgula
        if ',' in span_text:
            # Substituir a vírgula por um ponto e converter para float
            span_value = float(span_text.replace(',', '.'))
        else:
            # Remover ponto e converter para int
            span_value = int(span_text.replace('.', ''))

        # Converter float para int se necessário
        if isinstance(span_value, float):
            span_value = int(span_value)

      
        return span_value
    except Exception as e:
        print(f"Erro ao capturar o valor do span: {e}")
        return None


def change_map(driver, url):
    try:
        driver.get(url)
        time.sleep(5)  # Ajuste conforme necessário
        
        # Recarregar a página simulando Ctrl + R
        driver.execute_script("location.reload()")
        
        pyautogui.hotkey('ctrl', 'f5')
        time.sleep(6)  # Ajuste conforme necessário

        # Verificar se o botão de login está presente e visível
        try:
            login_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.Intro_startbutton__QtxEz'))
            )
            WebDriverWait(driver, 10).until(
                EC.visibility_of(login_button)
            )
            login_button.click()
            print("Botão de login clicado novamente com sucesso!")
        except Exception as e:
            print("Botão de login não encontrado ou não visível.")
    except Exception as e:
        print(f"Erro ao mudar de mapa: {e}")

    time.sleep(20)

if __name__ == "__main__":
    driver = login_to_game()
    if driver:
        try:
            select_game(driver)
            time.sleep(10)  # Ajustar conforme necessário
            
            # Capturar logs do navegador
            get_browser_logs(driver)
            
            # Mudar de mapa
            map_url = "https://play.pixels.xyz/pixels/DrunkenGooseInterior"
            change_map(driver, map_url)
            
            time.sleep(999)  # Mantém o programa em execução
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            driver.quit()
