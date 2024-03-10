from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")

textarea = driver.find_element(By.CLASS_NAME, value="gLFyf" )
textarea.send_keys("Insider")
textarea.send_keys(Keys.RETURN)

current_url = driver.current_url

if "google.com" in current_url:
    print("Test Başarılı: Google.com sayfası ziyaret edildi.")
else:
    print(f"Beklenen url google.com ancak ziyaret edilen url {current_url}")

driver.quit()
