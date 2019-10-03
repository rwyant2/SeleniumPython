from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class FirstSelenium:

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--test-type')
    driver = webdriver.Chrome(executable_path="/home/richard-u18/PycharmProjects/SeleniumPython/webdrivers/chromedriver",chrome_options=options)
    driver.get('https://python.org')

# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()