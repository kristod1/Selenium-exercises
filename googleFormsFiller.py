import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("./chromedriver")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScSWFXV06W79rVl0cGMCuEoMo8sDd1D2RwS5yRUCS1yizv_Uw/viewform?fbclid=IwAR09n3k4upfmzX-kvYPSUAcRnBtmsjjlQUzzvuX5GTU1Hv7DESMrLUtUhYs")

inputElement = driver.find_element_by_css_selector(".freebirdFormviewerViewItemsItemItem:nth-child(1) .quantumWizTextinputPaperinputInput")
inputElement.send_keys("Labos")
inputElement.send_keys(Keys.ENTER)

inputElement = driver.find_element_by_css_selector(".freebirdFormviewerViewItemsItemItem:nth-child(2) .quantumWizTextinputPaperinputInput")
inputElement.send_keys("10.11.2018 od 18 do 22 sata")
inputElement.send_keys(Keys.ENTER)

inputElement = driver.find_element_by_css_selector(".freebirdFormviewerViewItemsItemItem:nth-child(3) .quantumWizTextinputPaperinputInput")
inputElement.send_keys("sample@sample.com")
inputElement.send_keys(Keys.ENTER)

inputElement = driver.find_element_by_css_selector(".freebirdFormviewerViewItemsItemItem:nth-child(4) .quantumWizTextinputPaperinputInput")
inputElement.send_keys("Dom tehnike")
inputElement.send_keys(Keys.ENTER)

inputElement = driver.find_element_by_css_selector(".quantumWizTextinputPapertextareaInput")
inputElement.send_keys("Labos")
inputElement.send_keys(Keys.ENTER)

submit  = driver.find_element_by_css_selector('.quantumWizButtonPaperbuttonLabel')
actions = ActionChains(driver)
actions.click(submit).perform()

