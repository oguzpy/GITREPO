import time
from selenium.common import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



def is_element_present(locator):
    try:
        object = driver.find_element(*locator)
        return True

    except NoSuchElementException:
        return False

def scroll_click_element(locator,wait=1,ElementWait = None):
    is_element_present(locator)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto' , block: 'center', inline: 'center'});", element)
    time.sleep(wait)
    element.click()
    return element

def switch_to_new_tab():
    # Ana sekmenin tanımlayıcısını alın
    main_window_handle = driver.current_window_handle

    # Tüm açık pencerelerin tanımlayıcılarını alın
    all_window_handles = driver.window_handles

    # Ana sekme dışındaki diğer sekmeleri kontrol edin
    for window_handle in all_window_handles:
        if window_handle != main_window_handle:
            # Yeni sekmenin tanımlayıcısını alın
            new_window_handle = window_handle

    # Yeni sekmenin tanımlayıcısına geçin
    driver.switch_to.window(new_window_handle)

driver = webdriver.Chrome()
driver.get('https://useinsider.com/')


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://useinsider.com/')
Company = driver.find_element(By.XPATH, '/html/body/nav/div[2]/div/ul[1]/li[6]/a')
print(Company.text)
Company.click()
Carrers = driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]/div/div[2]/a[2]')
Carrers.click()


LocationsSectionLoc = By.ID, 'career-our-location'
TeamsSectionLoc = By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div/section/div/div/a'
LifeAtInsiderSectionLoc = By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[1]/div/h2'
QualityAssuranceLoc = By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div/section/div/div/div[2]/div[12]/div[2]/a'
SeeAllJobsLoc = By.XPATH, '/html/body/div[1]/section[1]/div/div/div/div[1]/div/section/div/div/div[1]/div/div/a'
JobsListLoc = By.CLASS_NAME, 'position-list-item'
JobsListElementLoc = By.XPATH, '/html/body/section[3]/div/div/div[2]/div[1]/div/p'
SelectLocationLoc = By.ID, 'select2-filter-by-location-container'
SelectDepartmentLoc = By.ID, 'select2-filter-by-department-container'
TR_IST_SelectLoc = By.XPATH, "/html/body/span/span/span[2]/ul/li[2]"
QA_SelectLoc = By.XPATH, "/html/body/span/span/span[2]/ul/li[17]"
ViewRolBtnLoc = By.XPATH, "/html/body/section[3]/div/div/div[2]/div[1]/div/a"




#Assert


scroll_click_element(TeamsSectionLoc)
scroll_click_element(QualityAssuranceLoc)
scroll_click_element(SeeAllJobsLoc)
LocationSelect = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, 'deneme')))
scroll_click_element(SelectLocationLoc)
scroll_click_element(TR_IST_SelectLoc)
scroll_click_element(SelectDepartmentLoc)
scroll_click_element(QA_SelectLoc)
scroll_click_element(JobsListLoc)
ViewRolBtn = driver.find_element(ViewRolBtnLoc[0],ViewRolBtnLoc[1])
from selenium.webdriver.common.action_chains import ActionChains

print(driver.current_url)
switch_to_new_tab()
print(driver.current_url)
time.sleep(3)
if is_element_present((By.XPATH, '/html/body/div[3]/div/div[2]/div[6]/a')):
    print("Test Başarılı !")
else:
    print("Test Başarısız !")


driver.find_elements()
