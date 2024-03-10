from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.useinsider.com")

logo_element = driver.find_element(By.CSS_SELECTOR, value='.navbar-brand')
print("HREF BUDUR :" + logo_element.get_attribute('href'))

why_insider_link = driver.find_element(By.XPATH, value='//a[contains(text(), "Why Insider")]')
print("HREF BUDUR :" + why_insider_link.get_attribute('href'))

current_url = driver.current_url

if "google.com" in current_url:
    print("Test Başarılı: Google.com sayfası ziyaret edildi.")
else:
    print(f"Beklenen url google.com ancak ziyaret edilen url {current_url}")

driver.quit()
