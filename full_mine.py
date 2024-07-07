import time
import pyautogui
from itertools import islice
from login import check_energy

# Função para mover para a posição inicial
def first_position():
    time.sleep(0.2)
    pyautogui.keyDown('left')
    time.sleep(7)  
    pyautogui.keyUp('left')

# Dicionário de coordenadas fixas
coordenadas = {
    'mine1': (280, 300),
    'mine2': (280, 450),
    'mine3': (500, 300),
    'mine4': (500, 450),
    'mine5': (280, 315),
    'mine6': (280, 445),
    'mine7': (500, 320),
    'mine8': (500, 450),
    'mine9': (293, 286),
    'mine10': (296, 469),
    'mine11': (487, 477),
    'mine12': (483, 286),
    'mine13': (307, 294),
    'mine14': (307, 482),
    'mine15': (492, 469),
    'mine16': (492, 292),
}

# Função para clicar nas coordenadas
def click_cords(sub_coordenadas):
    for name, (x, y) in sub_coordenadas:
        pyautogui.moveTo(x, y)
        time.sleep(0.1)  # Pequena pausa antes de clicar
        pyautogui.click()
        print(f"Clicou em {name} nas coordenadas ({x}, {y})")

# Função para obter fatias do dicionário
def get_chunks(coordenadas, chunk_size):
    it = iter(coordenadas.items())
    for first in it:
        yield [first] + list(islice(it, chunk_size - 1))

# Função principal para executar a sequência de cliques e movimentos
def play_row(delta_x=0):
    time.sleep(0.2)
    pyautogui.keyDown('right')
    time.sleep(0.98)  
    pyautogui.keyUp('right')

    pyautogui.press('num1')
    # Executa o movimento inicial para cima
    time.sleep(0.2)
    pyautogui.keyDown('up')
    time.sleep(2)  
    pyautogui.keyUp('up')

    # Modifica as coordenadas x conforme necessário
    coordenadas_modificadas = {
        name: (x + delta_x, y) for name, (x, y) in coordenadas.items()
    }

    chunk_size = 4
    times = 0.92
    for sub_coordenadas in get_chunks(coordenadas_modificadas, chunk_size):
     
        # Clica nas coordenadas do grupo atual
        click_cords(sub_coordenadas)

        # Executa as ações adicionais após cada grupo de cliques
        time.sleep(0.1)
        pyautogui.keyDown('down')
        time.sleep(times)  
        pyautogui.keyUp('down')
        time.sleep(0.1)

        times += 0.025

    time.sleep(0.1)
    pyautogui.keyDown('up')
    time.sleep(2)  
    pyautogui.keyUp('up')
    time.sleep(0.1)

    pyautogui.press('num1')

    

def full_mine():
    first_position()
    play_row()
    play_row(delta_x=200)  
    play_row(delta_x=360)  
    play_row(delta_x=350) 
    play_row(delta_x=350) 
    play_row(delta_x=340)
    play_row(delta_x=550)
    time.sleep(0.2)
    pyautogui.keyDown('left')
    time.sleep(3.5)  
    pyautogui.keyUp('left')

if __name__ == '__main__':
    while  True:
        time.sleep(2)
        full_mine()

   
