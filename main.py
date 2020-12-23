# selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# python modules
from dotenv import load_dotenv, find_dotenv
from time import sleep
from sys import argv
import os

load_dotenv(find_dotenv())
os.system(f'caffeinate -t {int(argv[1]) * 3600}')

options = Options()
options.add_argument('--use-fake-ui-for-media-stream')
driver = webdriver.Chrome(options=options)
driver.get('https://discord.com/login')

form = driver.find_element(By.CSS_SELECTOR, '.mainLoginContainer-1ddwnR')
user = form.find_element(By.NAME, 'email')
password = form.find_element(By.NAME, 'password')

sleep(.5)

user.send_keys(os.getenv('EMAIL'))
password.send_keys(os.getenv('PASSWORD'))
form.submit()

servers = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.wrapper-21YSNc'))
)

servers.find_element(
    By.CSS_SELECTOR, '.closedFolderIconWrapper-15K9MK').click()

sleep(1)

servers.find_element(By.CSS_SELECTOR, '[aria-label="  Ｖ１"]').click()

chats = driver.find_element(By.CSS_SELECTOR, '.sidebar-2K8pFh')

for _ in range(int(argv[1])):
    sleep(.2)
    chats.find_element(
        By.CSS_SELECTOR, '[data-list-item-id="channels___732583805541679191"]').click()
    sleep(2700)
    chats.find_element(
        By.CSS_SELECTOR, '[aria-label="Disconnect"]').click()
