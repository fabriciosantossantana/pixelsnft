from farm import farm
from mine import mine
from routine import go_to_sauna, go_to_speck
from login import login_to_game, select_game, check_energy

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
            while True:
                energy = check_energy(driver)
                # if energy <= 900:
                #     go_to_sauna(driver)
                #     if energy >= 998:
                #         go_to_speck()
                # else:
                if energy <= 100:
                    time.sleep(3600)
                else: 
                    mine()
                    farm()
            # Mantém o programa em execução
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            # Garante que o driver é encerrado corretamente
            driver.quit()
