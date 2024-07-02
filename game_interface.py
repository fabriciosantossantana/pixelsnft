from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class GameInterface:
    
    def __init__(self, driver):
        self.driver = driver

    def click_land_menu_button(self):
        """
        Clica no botão do menu para abrir o menu principal.
        """
        try:
            # Aguarda até que o botão esteja presente e seja clicável
            land_menu_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Hud_outside__zzIGQ"))
            )
            land_menu_button.click()
            print("Botão do menu de terra clicado com sucesso.")
        except Exception as e:
            print(f"Falha ao clicar no botão do menu de terra: {e}")