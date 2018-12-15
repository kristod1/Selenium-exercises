import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.tripletsandus.com/80s/80s_games/html5_galaga.htm")
clickToPlay = driver.find_element_by_css_selector("select")
actions = ActionChains(driver)
actions.click(clickToPlay).perform()
time.sleep(5)
a = driver.find_element_by_class_name("nes-screen")
actions = ActionChains(driver)
actions.click(a).perform()
time.sleep(3)
pyautogui.keyDown("enter")
pyautogui.keyUp("left")
time.sleep(5)


while True:
    pyautogui.keyDown("left")
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    time.sleep(2)
    pyautogui.keyUp("left") 
    pyautogui.keyDown("x")
    time.sleep(1)
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    time.sleep(1)        
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    time.sleep(1)
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    time.sleep(1)
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    time.sleep(1)
    pyautogui.keyUp("x")
    pyautogui.keyDown("right")
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    time.sleep(1.5)
    pyautogui.keyUp("x")
    pyautogui.keyDown("x")
    pyautogui.keyUp("right") 
        
 

