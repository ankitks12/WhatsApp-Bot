from selenium import webdriver
import time

driver = webdriver.Chrome(r'/home/ankit/Documents/Trash-files/chromedriver_linux64/chromedriver')

url = driver.command_executor._url
session_id = driver.session_id 

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.close()   # this prevents the dummy browser
driver.session_id = session_id

driver.get("https://web.whatsapp.com/")

dontKeepSignedIn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/label/input")
dontKeepSignedIn.click()

#input("Please sign in and press any key: ")
time.sleep(15)

menu = driver.find_element_by_css_selector('span[data-testid="menu"]')
menu.click()

settings = driver.find_element_by_css_selector('div[title="Settings"]')
settings.click()

theme = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[3]/div[2]/div/span")
theme.click()

dark = driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[2]/label")
dark.click()

ok = driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div[2]")
ok.click()

back = driver.find_element_by_css_selector('span[data-testid="back"]')
back.click()

time.sleep(20)

driver.quit()

