from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = 'M:\\Programs\\workspace\\python\\python_selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

url = 'https://techwithtim.net'
driver.get(url)
print(driver.title)

search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

# print(driver.page_source)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        header = article.find_element_by_class_name('entry-header')
        print(header.text)
    # print(main.text)
finally:
    driver.quit()


# main = driver.find_element_by_id('main')
# print(main.text)

# driver.quit()
