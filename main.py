from farm import farm
from login import login_to_game
from login import select_game
import time
from game_interface import GameInterface

if __name__ == "__main__":
    # Inicia o processo de login
    driver = login_to_game()
    if driver:
        try:
            # Cria uma instância da interface do jogo
            interface = GameInterface(driver)
            time.sleep(10)

            # Seleciona o jogo
            select_game(driver)

            # Clica no botão do menu de terra para abrir o menu principal
            farm()
            # Mantém o programa em execução
            time.sleep(999)
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            # Garante que o driver é encerrado corretamente
            driver.quit()
