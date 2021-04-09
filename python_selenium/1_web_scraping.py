from selenium import webdriver


PATH = 'M:\\Programs\\workspace\\python\\python_selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('http://synthway.com')
print(driver.title)
# driver.close()
driver.quit()
