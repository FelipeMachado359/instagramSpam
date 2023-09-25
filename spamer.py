import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#ChromeDriver Selenium configuration 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\felip\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Profile 1") 
options.add_argument('--disable-blink-features=AutomationControlled')
chromedriver_path = r'C:\Users\felip\Documents\drivers\chromedriver.exe'
driver = webdriver.Chrome(options=options, service=Service(chromedriver_path))
window_handles = driver.window_handles

# open the wobsite
driver.get('https://www.instagram.com/')
driver.maximize_window() # Tela cheia
time.sleep(2)

# check if you is logged
def islogged(driver):
    try:
        # check if buttom "Perfil" is visible
        profile_button = driver.find_element(By.NAME, "username")
        return False
    except:
        return True
    
if not islogged(driver):
    #login with login/pass   
    wait = WebDriverWait(driver, 10) 
    email_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    # Find the login elements and enter email and password
    email = 'your email'
    password = 'you password'
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(10)

# Go to the Instagram Direct Inbox
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(3)

# Check if the notification pop-up is displayed
def havePopup(driver):
    try: 
        notification_popup = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        return False
    except:
        return True
    
if not havePopup(driver):
    notification_popup.is_displayed()
    notification_popup.click()
    time.sleep(2)

# Click the 'New Message' button
new_message_button = driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div')
new_message_button.click()
time.sleep(5)

# Wait for the recipient input field to become available
wait = WebDriverWait(driver, 10)
recipient_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')))

# Type each username and press Enter to add as a recipient
hitAccount = 'account to hit'
recipient_input.send_keys(hitAccount)
time.sleep(1)
recipient_input.send_keys(Keys.ENTER)
time.sleep(1)

select_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input')))
select_button.click()
time.sleep(5)

# Wait for the next button to become clickable
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')))

# Click the Next button to proceed to the message input
next_button.click()
time.sleep(4)

i = 0
limite = 1000 #how much messages
while i < limite:
    pyautogui.click(645, 945)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.typewrite("Message to send", interval=0.1)
    pyautogui.press('enter')
    time.sleep(10)
    i += 1
    print(i)
