import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from seleniumabsxy import coordsclicker


def select_game():
    centro_x = 615
    centro_y = 248
    pyautogui.moveTo(centro_x, centro_y)
    pyautogui.click()
    time.sleep(5)
    print('game logado com sucesso') 

def login_to_game():
    user_data_dir = r'C:\Users\Karine\AppData\Local\Google\Chrome\User Data'
    profile_dir = 'Profile 1'
    
    chrome_opt = uc.ChromeOptions()
    chrome_opt.add_argument(f'--user-data-dir={user_data_dir}')
    chrome_opt.add_argument(f'--profile-directory={profile_dir}')
    driver = uc.Chrome(options=chrome_opt)
    coordsclicker.driver = driver
    time.sleep(1)
    driver.get(r"https://play.pixels.xyz/pixels")
    time.sleep(1)
    driver.fullscreen_window()

    # Esperar explicitamente até que o elemento esteja presente
    try:
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
    
    return driver


if __name__ == "__main__":
    login_to_game() 