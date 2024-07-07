import time
import pyautogui
import keyboard
from selenium import webdriver
from login import login_to_game, select_game, check_energy
from routine import go_to_sauna, go_to_speck
from full_mine import full_mine
from game_interface import GameInterface

running = True

def toggle_running():
    global running
    running = not running
    if running:
        print("Retomando a execução...")
    else:
        print("Execução pausada. Pressione 'Ctrl + R' para retomar.")

def run_game(driver):
    energy = check_energy(driver)
    print(energy)
    if energy >= 950:
        print(f'{energy} de energia.')
        go_to_speck(driver)
        full_mine()
    elif energy <= 100:
        print(f'Energia baixa, {energy}. Indo para sauna')
        go_to_sauna(driver)
        time.sleep(120)
        print(energy)
        if energy <= 100:
            print('Energia não disponível, indo para piscina...')
            pyautogui.keyDown('down')
            time.sleep(3.2)
            pyautogui.keyUp('down')
            print('Pausa de 30 min na piscina para recarregar')
            time.sleep(1800)
            go_to_speck(driver)
        else:
            print('Energia recarregada com sucesso!')
    else:
        print('Minerando...')
        full_mine()

def main():
    # Registra a combinação de teclas 'Ctrl + P' para pausar/resumir o programa
    keyboard.add_hotkey('ctrl+p', toggle_running)
    # Registra a combinação de teclas 'Ctrl + Q' para parar o programa
    keyboard.add_hotkey('ctrl+q', lambda: exit())

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
                if running:
                    run_game(driver)
                else:
                    time.sleep(1)  # Aguarda um segundo antes de verificar novamente

        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            # Garante que o driver é encerrado corretamente
            driver.quit()

if __name__ == "__main__":
    main()
