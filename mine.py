import time
import pyautogui

def start_position():
    time.sleep(0.2)
    pyautogui.keyDown('down')
    time.sleep(0.9)  
    pyautogui.keyUp('down')
    
def right_position():
    time.sleep(0.05)
    pyautogui.keyDown('right')
    time.sleep(4)  
    pyautogui.keyUp('right')


def down_position():
    time.sleep(0.05)
    pyautogui.keyDown('down')
    time.sleep(1.1)  
    pyautogui.keyUp('down')

def up_position():    
    time.sleep(0.05)
    pyautogui.keyDown('up')
    time.sleep(1.1)  
    pyautogui.keyUp('up')

def left_position():    
    time.sleep(0.05)
    pyautogui.keyDown('left')
    time.sleep(1.2)  
    pyautogui.keyUp('left')

def left_last_position():
    time.sleep(3)
    pyautogui.keyDown('left')
    time.sleep(2.7)  
    pyautogui.keyUp('left')

def up_last_position():
    time.sleep(3)
    pyautogui.keyDown('up')
    time.sleep(0.9)  
    pyautogui.keyUp('up')

def mine_click_one():
    pyautogui.press('num7')
    def loop_one():
        x = 780
        y = 305


        first_x = x
        first_y = y    

        second_x = x
        second_y = y + 190

        tree_x = second_x + 230
        tree_y = second_y

        four_x = tree_x
        four_y = y

        time.sleep(0.05)
     
        #firstclick
        pyautogui.moveTo(first_x, first_y)
        time.sleep(0.1)
        pyautogui.click()

        #secondclick    
        pyautogui.moveTo(second_x, second_y)
        time.sleep(0.1)
        pyautogui.click()

        #treeclick    
        pyautogui.moveTo(tree_x, tree_y)
        time.sleep(0.1)
        pyautogui.click()
        
        #fourclick    
        pyautogui.moveTo(four_x, four_y)
        time.sleep(0.1)
        pyautogui.click()
    
    loop_one()
    time.sleep(4)
    loop_one()
    time.sleep(4)
    loop_one()
    time.sleep(4)
    loop_one()
    pyautogui.press('num7')



def mine_click_two():
    pyautogui.press('num7')
    def loop_two():
        x = 580
        y = 280


        first_x = x
        first_y = y    

        second_x = x
        second_y = y + 190

        tree_x = second_x + 230
        tree_y = second_y

        four_x = tree_x
        four_y = y

        time.sleep(0.05)
     
        #firstclick
        pyautogui.moveTo(first_x, first_y)
        time.sleep(0.1)
        pyautogui.click()

        #secondclick    
        pyautogui.moveTo(second_x, second_y)
        time.sleep(0.1)
        pyautogui.click()

        #treeclick    
        pyautogui.moveTo(tree_x, tree_y)
        time.sleep(0.1)
        pyautogui.click()
        
        #fourclick    
        pyautogui.moveTo(four_x, four_y)
        time.sleep(0.1)
        pyautogui.click()
    
    loop_two()
    time.sleep(4)
    loop_two()
    time.sleep(4)
    loop_two()
    time.sleep(4)
    loop_two()
    pyautogui.press('num7')


def mine():
    time.sleep(1)
    start_position()
    right_position()
    mine_click_one()
    down_position()
    mine_click_one()
    left_position()
    mine_click_two()
    up_position()
    mine_click_two()  
    left_last_position()
    up_last_position()


if __name__ == '__main__':
    time.sleep(3)
    while True:
        mine()