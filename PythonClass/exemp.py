from datetime import datetime
from selenium import webdriver

current_time = datetime.now()


driver = webdriver.Chrome()
driver.get("https://www.google.com")

currentURL = driver.current_url
print(currentURL)

if 'apple' in currentURL:
    print("Doğru Sayfadayız !")
else:

    driver.save_screenshot("./screenshot/hata_{}.png".format(current_time.strftime("%H:%M:%S")))

driver.quit()