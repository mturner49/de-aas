from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By


def fb_login(
    email: str,
    password: str) -> None:
    """Allow users to login via Facebook"""
    usr = email
    pwd = password
    
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    print ("Opened facebook")
    sleep(1)
    
    username_box = driver.find_element(By.ID, 'email')
    username_box.send_keys(usr)
    print("Email Id entered")
    sleep(1)
    
    password_box = driver.find_element(By.ID, 'pass')
    password_box.send_keys(pwd)
    print("Password entered")
    
    login_box = driver.find_element(By.NAME, 'login')
    login_box.click()
    
    print ("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")