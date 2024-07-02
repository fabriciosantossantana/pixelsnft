from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

    def click_option1(self):
        """
        Simula o clique no botão de opção 1 dentro do menu de terra.
        """
        try:
            option1_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "id_do_botao_opcao1"))
            )
            option1_button.click()
            print("Botão de opção 1 clicado com sucesso.")
        except Exception as e:
            print(f"Falha ao clicar no botão de opção 1: {e}")

    def click_option2(self):
        """
        Simula o clique no botão de opção 2 dentro do menu de terra.
        """
        try:
            option2_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "id_do_botao_opcao2"))
            )
            option2_button.click()
            print("Botão de opção 2 clicado com sucesso.")
        except Exception as e:
            print(f"Falha ao clicar no botão de opção 2: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    from login import login_to_game

    driver = login_to_game()
    interface = GameInterface(driver)

    # Clica no botão do menu de terra para abrir o menu principal
    interface.click_land_menu_button()

    # Simula cliques em outras opções dentro do menu de terra
    interface.click_option1()
    time.sleep(2)  # Aguarda 2 segundos entre cliques para simular outras interações
    interface.click_option2()
