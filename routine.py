import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from seleniumabsxy import coordsclicker  # Certifique-se de que este módulo está corretamente importado
from login import login_to_game, change_map, select_game # Importe sua função login_to_game do módulo login
from cooking import first_position_cooking
from selenium.webdriver.common.keys import Keys



def goldbox(driver):
    try:
        # Verificar se a janela apareceu
        goldbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Hud_mailbox__qj4Ou"))
        )
        time.sleep(1)
        goldbox.click()
        print("Colhendo o dinheiro")
        
        time.sleep(1)

        collectgold = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MailBox_collectAllButton__yi4P_"))
        )
        time.sleep(1)
        collectgold.click()
       
        time.sleep(1)

        collectgold = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "commons_closeBtn__UobaL"))
        )
        time.sleep(1)
        collectgold.click()

       
  
    except Exception as e:
        print(f"Erro durante o click da goldbox: {e}")
    pass



def search_and_buy(driver, item_name, iterations, quantity):
    try:
        time.sleep(5)
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.Marketplace_filter__3ynr2'))
        )

        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.DELETE)
        
        time.sleep(1)

        search_input.send_keys(item_name)
        
        view_listing = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.commons_pushbutton__7Tpa3.Marketplace_viewListings__q_KfD'))
        )
        view_listing.click()

        auto_buy = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "commons_pushbutton__7Tpa3.MarketplaceItemListings_buyListing__jYwuF"))
        )
        auto_buy.click()

        for _ in range(iterations):
            div_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "MarketplaceItemListings_listing__TyllF"))
            )

            # Encontrar os inputs dentro do div_element
            amount_inputs = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MarketplaceItemListings_amount__IyJRp input[type='number']"))
            )

            # Garantir que temos pelo menos dois inputs
            if len(amount_inputs) >= 2:
                for input_field in amount_inputs:
                    # Limpar o campo de maneira mais segura
                    input_field.send_keys(Keys.CONTROL + "a")
                    input_field.send_keys(Keys.DELETE)
                
                # Esperar um tempo curto para garantir que os campos foram limpos
                time.sleep(0.5)
                
                # Preencher o primeiro input com a quantidade desejada
                amount_inputs[0].send_keys(quantity)
                
                # Esperar um tempo curto para garantir que o valor foi inserido
                time.sleep(0.5)
                
                # Preencher o segundo input com "9999"
                amount_inputs[1].send_keys("9999")
                
                # Esperar um tempo curto para garantir que o valor foi inserido
                time.sleep(0.5)

            buttons = div_element.find_elements(By.CSS_SELECTOR, ".MarketplaceItemListings_buttons__LNftA button")
            if buttons:
                buttons[0].click()

            close_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.commons_uikit__Nmsxg.commons_pushbutton__7Tpa3.Marketplace_button__x_SGP'))
            )
            close_button.click()

            time.sleep(18)

        pyautogui.moveTo(903, 165)
        pyautogui.click()
        time.sleep(1)

    except Exception as e:
        print(f"Error during search_and_buy for {item_name}: {e}")

def buy(driver):
    try:
        pyautogui.keyDown('right')
        time.sleep(3)
        pyautogui.keyUp('right')

        coords = (830, 255)
        pyautogui.moveTo(coords)
        pyautogui.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'Marketplace_content__MWwNh'))
        )

        items_to_buy = [
            ('Craftbark Log', 10, '99'),
            ('Grumpkin Wine', 1, '20'),

        ]

        for item_name, iterations, quantity in items_to_buy:
            search_and_buy(driver, item_name, iterations, quantity)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Marketplace_container__nQQtb"))
        )
        close_button_market = driver.find_element(By.CSS_SELECTOR, ".Marketplace_container__nQQtb button.commons_closeBtn__UobaL")
        close_button_market.click()

    except Exception as e:
        print(f"Error during the execution of BUY: {e}")


    

def sell(driver):
    try:
        # Posicionar para vender

        pyautogui.keyDown('left')
        time.sleep(2.1)  
        pyautogui.keyUp('left')


        pyautogui.keyDown('right')
        time.sleep(1.2)
        pyautogui.keyUp('right')

        # Abrir a loja
        coords = (685, 250)
        pyautogui.moveTo(coords)
        pyautogui.click()

        marketopen = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'Infiniportal_tabsContainer__9D6ke'))
        )

        # Se a loja estiver aberta clicar no botão de "Create"
        if marketopen:
            create_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Create']"))
            )
            create_button.click()

            try:
                # Espera até que a div com o span "Blue Grumpkin Loaf" esteja visível
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//span[text()="Craftbark Plank"]/ancestor::div[@class="MarketplaceListings_listing__WlDih"]//button[text()="Add"]'))
                )
    
                # Clica no botão "Add"
                element.click()
                print("Botão 'Add' clicado com sucesso!")
                time.sleep(5)
                try:

                    # Espera até que a div específica seja visível
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "MarketplaceAddListing_listinginfo__PjDEl")))

                    # Localiza todos os spans dentro da div específica
                    spans = driver.find_elements(By.CSS_SELECTOR, ".MarketplaceAddListing_listinginfo__PjDEl span")

                    # O valor desejado está no segundo span
                    if len(spans) > 1:
                        valor_str = spans[1].text.strip()  # Obtém o texto do segundo span e remove espaços em branco extras
                        print("Valor encontrado:", valor_str)        


                        valor = int(valor_str)
                        valor = valor - 1

                        # Encontra o input para o preço por item
                        input_price = driver.find_element(By.CSS_SELECTOR, ".MarketplaceAddListing_prop__Aqxnc input[type='number']")

                        # Preenche o valor obtido no input
                        input_price.clear()  # Limpa qualquer valor existente
                        input_price.send_keys(valor)  # Insere o valor encontrado no input
                        
                        # Encontra o link "max"
                        link_max = driver.find_element(By.CLASS_NAME, "MarketplaceAddListing_hotlink__Cp9YM")
                        # Clica no link "max"
                        link_max.click()

                        # Encontra o botão "Create"
                        button_create = driver.find_element(By.CSS_SELECTOR, ".MarketplaceAddListing_buttons__wSc7Q button")
                        # Clica no botão "Create"
                        button_create.click()

                        # Espera até que o botão de fechar seja visível
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "commons_closeBtn__UobaL")))
                        # Encontra o botão de fechar
                        button_close = driver.find_element(By.CLASS_NAME, "commons_closeBtn__UobaL")
                        # Clica no botão de fechar
                        button_close.click()

                        time.sleep(300)

                except Exception as e:
                    print(f"Erro ao abrir o item: {e}")  
            except Exception as e:
                print(f"Erro ao clicar no botão 'Add': {e}")
    
    except Exception as e:
        print(f"Erro durante a execução: {e}")
    pass

def go_to_sauna(driver):

    pyautogui.hotkey('ctrl', 'f5')
    time.sleep(4)
    map_url = "https://play.pixels.xyz/pixels/DrunkenGooseInterior"
    change_map(driver, map_url)
    if not driver.fullscreen_window():
        driver.fullscreen_window()
    print('going to sauna')
    time.sleep(5)
    # ROTA DA SAUNA
    pyautogui.keyDown('right')
    time.sleep(1.3)  
    pyautogui.keyUp('right')
    
    pyautogui.keyDown('down')
    time.sleep(4)  
    pyautogui.keyUp('down')
    
    pyautogui.keyDown('left')
    time.sleep(1.3)  
    pyautogui.keyUp('left')

    pyautogui.keyDown('down')
    time.sleep(4)  
    pyautogui.keyUp('down')

    # espera carregar proximo mapa

    time.sleep(12)

    pyautogui.keyDown('left')
    time.sleep(2.5)  
    pyautogui.keyUp('left')

    pyautogui.keyDown('up')
    time.sleep(8)  
    pyautogui.keyUp('up')

    pyautogui.keyDown('right')
    time.sleep(1.5)  
    pyautogui.keyUp('right')

    pyautogui.keyDown('up')
    time.sleep(3)  
    pyautogui.keyUp('up')
    
    time.sleep(12)

    pyautogui.keyDown('up')
    time.sleep(8)  
    pyautogui.keyUp('up')

    pyautogui.moveTo(700, 270)
    time.sleep(1)
    pyautogui.click()

    pass


def go_to_market(driver):
    driver = driver

    pyautogui.hotkey('ctrl', 'f5')
    time.sleep(4)
    map_url = "https://play.pixels.xyz/pixels/DrunkenGooseInterior"
    change_map(driver, map_url)
    if not driver.fullscreen_window():
        driver.fullscreen_window()
    print('Indo para o Market')
    time.sleep(5)
    # ROTA DA SAUNA
    pyautogui.keyDown('right')
    time.sleep(1.3)  
    pyautogui.keyUp('right')
    
    pyautogui.keyDown('down')
    time.sleep(4)  
    pyautogui.keyUp('down')
    
    pyautogui.keyDown('left')
    time.sleep(1.3)  
    pyautogui.keyUp('left')

    pyautogui.keyDown('down')
    time.sleep(4)  
    pyautogui.keyUp('down')

    time.sleep(15)

    #ROTA PARA BUCKGALORE

    pyautogui.keyDown('right')
    time.sleep(6)  
    pyautogui.keyUp('right')
    
    pyautogui.keyDown('up')
    time.sleep(7.8)  
    pyautogui.keyUp('up')

    
    pyautogui.keyDown('right')
    time.sleep(5)  
    pyautogui.keyUp('right')
    
    pyautogui.keyDown('up')
    time.sleep(3)  
    pyautogui.keyUp('up')


    #ROTA DENTRO DA LOJA

    time.sleep(15)

    pyautogui.keyDown('right')
    time.sleep(0.45)  
    pyautogui.keyUp('right')

    pyautogui.keyDown('up')
    time.sleep(6.5)  
    pyautogui.keyUp('up')


def go_to_speck(driver):

    # Encontrar o elemento da div principal
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Hud_topLeftBackground__OhgQS'))
    )


    # Aguarde até que o modal desapareça
    WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "commons_modalBackdrop__EOPaN"))
    )

    # Encontrar e clicar no primeiro botão dentro da div principal
    buttons = div_element.find_elements(By.CSS_SELECTOR, 'button.Hud_outside__zzIGQ')
    if buttons:
        first_button = buttons[0]
        first_button.click()

    # Aguardar um pouco após o clique
    time.sleep(3)

    # Encontrar o elemento da div principal
    div_element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'LandAndTravel_mapSquare__LuVEh'))
    )

    # Encontrar e clicar no segundo botão (assumindo que é o botão correto)
    second_button = driver.find_element(By.CSS_SELECTOR, 'div.LandAndTravel_mapsSquare__vG99V button')

    # Clique no botão
    second_button.click()
    print('Going to speck')

    time.sleep(15)

    pyautogui.keyDown('left')
    time.sleep(0.2)  
    pyautogui.keyUp('left')

    pyautogui.keyDown('up')
    time.sleep(3.2)  
    pyautogui.keyUp('up')



if __name__ == '__main__':
    go_to_sauna()
    driver = login_to_game()
    # if driver:
    #     try:
    #         go_to_sauna(driver)
    #         time.sleep(10)  # Ajustar conforme necessário

    #         # Exemplo de captura de logs do navegador
    #         # get_browser_logs(driver)

    #         time.sleep(999)  # Mantém o programa em execução
    #     except Exception as e:
    #         print(f"Erro durante a execução: {e}")
    #     finally:
    #         driver.quit()
