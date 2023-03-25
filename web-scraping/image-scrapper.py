from selenium import webdriver


# opening browser
driver_path = r'C:\Users\skumar\Desktop\python-projects\util-libs\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()

# do google search
search_link = f'https://images.google.com/'
driver.get(search_link)
query = 'Sree Leela'
driver.find_element_by_name('q').send_keys(query)

driver.find_element_by_class_name('Tg7LZd').click()

image_urls = set()
# get image addresses
actual_images = driver.find_elements_by_css_selector('islrc')
for actual_image in actual_images:
    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
        image_urls.add(actual_image)

print(image_urls)