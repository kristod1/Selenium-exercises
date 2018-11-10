import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
keyword=input("Enter keyword: ")
numberOfPages=int(input("How many pages in do you want to go? "))
driver = webdriver.Chrome("./chromedriver")


def listPage():
	titles_elementA = driver.find_elements_by_class_name("entity-title")
	titles_elementB = driver.find_elements_by_class_name("entity-prices")
	prices = [y.text for y in titles_elementB]
	items = [x.text for x in titles_elementA]
	for x, j in zip(items, prices):
		print(x + " / " + j)

driver.get("https://www.njuskalo.hr")
inputElement = driver.find_element_by_id("keywords")
inputElement.send_keys(keyword)
inputElement.send_keys(Keys.ENTER)

for i in range(0, numberOfPages):
	print("Page", i+1, "items:")
	nextPage = driver.find_element_by_css_selector('.entity-list-pagination--top .Pagination-item--next > .Pagination-link')
	listPage()
	actions = ActionChains(driver)
	actions.click(nextPage).perform()
	
time.sleep(10)
assert "No results found." not in driver.page_source
driver.close()
