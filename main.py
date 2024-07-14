import time
import pyautogui
import keyboard
from selenium import webdriver
from login import login_to_game, select_game, check_energy, use_wine
from routine import go_to_sauna, go_to_speck, go_to_market, sell, buy, goldbox
from full_mine import full_mine
from game_interface import GameInterface
from cooking import cooking, first_position_cooking

running = True

def toggle_running():
    global running
    running = not running
    if running:
        print("Retomando a execução...")
    else:
        print("Execução pausada. Pressione 'Ctrl + P' para retomar.")


def handle_high_energy(driver, energy):
    print(f'{energy} de energia. Energia está cheia')
    go_to_speck(driver)
    first_position_cooking()
    crafting = cooking(driver)
    cooking(driver)
    # full_mine()

    if crafting is not None and crafting <= 3:
        go_to_market(driver)
        sell(driver)
        goldbox(driver)
        buy(driver)
        go_to_speck(driver)
        first_position_cooking()
        cooking(driver)

def handle_low_energy(driver, energy):
    print(f'Energia baixa, {energy}. Indo para Sauna')
    #print(f'Energia baixa, {energy}. Indo para sauna')
    go_to_sauna(driver)
    time.sleep(30)

    energy = check_energy(driver)  # Atualize o valor da energia após a sauna
    if energy is None:
        print("Erro ao obter a energia após a sauna. Verifique a função check_energy.")
        return
    
    #print(f'Energia após a sauna: {energy}')
    
    if energy <= 100:
        print('Energia não disponível, usando vinho e voltando para land...')
        # time.sleep(7000)
        go_to_speck(driver)
        first_position_cooking()
        use_wine()
        cooking(driver)

        # print('Minerando...')
        # full_mine()
        
        print("Cozinhando...")
        #print(f'Energia {energy} recarregada com sucesso!')
    else:
        print(f'Energia {energy} recarregada com sucesso!')

def handle_normal_energy(driver):
    #print('Minerando...')
    #full_mine()

    print('Cozinhando...')
    crafting = cooking(driver)
    if crafting is not None and crafting <= 3:
        go_to_market(driver)
        sell(driver)
        goldbox(driver)
        buy(driver)
        go_to_speck(driver)
        first_position_cooking()
        cooking(driver)

def run_game(driver):
    time.sleep(5)
    energy = check_energy(driver)
    if energy is None:
        print("Erro ao obter a energia. Verifique a função check_energy.")
        return
    
    print(f'Energia atual: {energy}')
    
    if energy >= 999:
        handle_high_energy(driver, energy)
    elif energy <= 50:
        handle_low_energy(driver, energy)
    else:
        handle_normal_energy(driver)

def main():
    keyboard.add_hotkey('ctrl+p', toggle_running)
    keyboard.add_hotkey('ctrl+q', lambda: exit())

    driver = login_to_game()
    if driver:
        try:
            interface = GameInterface(driver)
            time.sleep(10)

            select_game(driver)

            while True:
                if running:
                    run_game(driver)
                else:
                    time.sleep(1)

        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            driver.quit()

if __name__ == "__main__":
    main()
