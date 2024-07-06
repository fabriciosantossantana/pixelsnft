from full_mine import full_mine
from login import login_to_game, select_game, check_energy
import pyautogui

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
                energy = float(check_energy(driver))
                # if energy <= 900:
                #     go_to_sauna(driver)
                #     if energy >= 998:
                #         go_to_speck()
                # else:
                if energy <= 450:

                    #use wine
                    time.sleep(3)
                    pyautogui.press('num2')
                    pyautogui.moveTo(695, 368)
                    time.sleep(0.25)
                    pyautogui.click(695, 368, 2)
                    time.sleep(0.25)
                    pyautogui.press('num2')
                
                     #move to center
                    time.sleep(0.2)
                    pyautogui.keyDown('left')
                    time.sleep(3.4)  
                    pyautogui.keyUp('left')
                else: 
                    full_mine()
            # Mantém o programa em execução
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            # Garante que o driver é encerrado corretamente
            driver.quit()
