from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

user = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

service = Service(executable_path=os.getenv("DRIVER_PATH"))
driver = webdriver.Chrome(service=service)

driver.get(url="https://www.linkedin.com/")
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

time.sleep(2)

# Loga no Linkedin.
user_input = driver.find_element(By.ID, "username")
user_input.send_keys(user)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)

enter = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container  button")
enter.click()

time.sleep(2)

jobs = driver.find_element(By.ID, "ember20")
jobs.click()
time.sleep(2)
search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
search.click()
# Pesquisa por vagas.
search.send_keys("Desenvolvedor Python", Keys.ENTER)

time.sleep(2)

# for n in range({o número de vagas para seguir}):
for n in range(30):
    jobs_list = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
    save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    driver.execute_script('return arguments[0].scrollIntoView(true);', jobs_list[n])
    # Clicka na vaga.
    jobs_list[n].click()
    time.sleep(1.5)
    # Salva a vaga.
    save.click()
    article = driver.find_element(By.CSS_SELECTOR, "article")
    article.click()
    body = driver.find_element(By.TAG_NAME, 'body')
    time.sleep(1)
    body.send_keys(Keys.END)
    time.sleep(1.5)
    follow = driver.find_element(By.CSS_SELECTOR, ".jobs-company__box button")
    # Segue a empresa.
    try:
        follow.click()
    except ElementClickInterceptedException:
        body.send_keys(Keys.ARROW_UP)
        time.sleep(0.2)
        body.send_keys(Keys.ARROW_UP)
        time.sleep(0.2)
        follow.click()
    time.sleep(1)

driver.quit()
