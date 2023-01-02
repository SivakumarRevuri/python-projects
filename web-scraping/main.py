from urllib.request import urlopen
from selenium import webdriver
import time


def browser_access_check():
    html = urlopen(url='https://en.wikipedia.org/wiki/India')
    file_path = r'C:\Users\skumar\Desktop\python-projects\web-scraping\index.html'
    with open(file_path, 'w') as f:
        f.write(str(html.read()))
        print('Done!!!')


driver_path = r'C:\Users\skumar\Desktop\python-projects\web-scraping\chromedriver.exe'
google_homepage = r'https://google.com/'

driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get(url=google_homepage)
# to print information of web-page
print(driver.title)
print(driver.current_url)

driver.find_element_by_name('q').send_keys('Narendra Modi')
time.sleep(5)
driver.find_element_by_name('btnK').click()

# print('goes backward')
# driver.back()
# print(driver.title)
# print(driver.current_url)
#
# print('*'*15)
# print('goes forward')
# driver.forward()
# print(driver.title)
# print(driver.current_url)
# driver.close()
