from farm import farm
from login import login_to_game
from login import select_game
import time
  
if __name__ == "__main__":
    driver = login_to_game()
    time.sleep(10)
    select_game()
    farm()