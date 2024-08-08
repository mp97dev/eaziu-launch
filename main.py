from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import json
import random
from time import sleep

config = []
poke_substrings = ['poke', 'pokè', 'poké']

def secret_log(clear_msg, secret_msg):
    if secret_msg and config["keep_the_secret"]:
        print(secret_msg)
    elif clear_msg and not config["keep_the_secret"]:
        print(clear_msg)

def setup():
    print(f"🖥️ Setting up webdriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

def next_section():
    sleep(1)
    next_button = driver.find_elements(By.XPATH, "//*[@id=\"stkv-form-root\"]/div[4]/div/div[2]/div[1]/div/div/nav/button[1]")
    if len(next_button) == 0:
        return False
    next_button[0].click()
    return True

def pick_main_course():
    sleep(1)
    picks = driver.find_elements(By.XPATH, "//*[@id=\"block-dbed4899-9130-4194-8098-218dd064d7bf\"]//*[@data-qa=\"choice-list\"]/div")
    if len(picks) == 0:
        return False
    pick = random.choice(picks)
    pick.click()
    secret_log(f"🍝 Main course: {pick.find_element(By.CSS_SELECTOR, 'div[aria-label]').get_attribute('aria-label')}", "")
    return True

def pick_follow():
    sleep(1)
    picks = driver.find_elements(By.XPATH, "//*[@id=\"block-d94294cc-5d4b-4d87-b2e4-af6e7b8093ba\"]//*[@data-qa=\"choice-list\"]/div")
    if len(picks) == 0:
        return False
    remove_every_poke = [elem for elem in picks if not any(x in elem.get_attribute("innerHTML").lower() for x in poke_substrings)]
    pick = random.choice(remove_every_poke)
    pick.click()
    secret_log(f"🍖 Following: {pick.find_element(By.CSS_SELECTOR, 'div[aria-label]').get_attribute('aria-label')}", "")
    return True

def pick_poke():
    sleep(1)
    picks = driver.find_elements(By.XPATH, "//*[@id=\"block-d94294cc-5d4b-4d87-b2e4-af6e7b8093ba\"]//*[@data-qa=\"choice-list\"]/div")
    if len(picks) == 0:
        return False
    get_every_poke = [elem for elem in picks if any(x in elem.get_attribute("innerHTML").lower() for x in poke_substrings)]
    if(len(get_every_poke) <= 0):
        return False
    pick = random.choice(get_every_poke)
    pick.click()
    secret_log(f"🥑 Poke: {pick.find_element(By.CSS_SELECTOR, 'div[aria-label]').get_attribute('aria-label')}", "")
    return True

def pick_side():
    sleep(1)
    picks = driver.find_elements(By.XPATH, "//*[@id=\"block-120ded4b-5c30-483d-959d-44d36ed05eed\"]//*[@data-qa=\"choice-list\"]/div")
    if len(picks) == 0:
        return False
    pick = random.choice(picks)
    pick.click()
    secret_log(f"🍅 Side: {pick.find_element(By.CSS_SELECTOR, 'div[aria-label]').get_attribute('aria-label')}", "")
    return True

def pick_fry():
    sleep(1)
    picks = driver.find_elements(By.XPATH, "//*[@id=\"block-bc594af9-461e-4741-b8f5-59a7b54bd861\"]//*[@data-qa=\"choice-list\"]/div")
    if len(picks) == 0:
        return False
    pick = random.choice(picks)
    pick.click()
    secret_log(f"🍤 Fry: {pick.find_element(By.CSS_SELECTOR, 'div[aria-label]').get_attribute('aria-label')}", "")
    return True

def set_notes():
    print(f"📓 Setting notes: {config['note']}")
    sleep(1)
    note_textarea = driver.find_elements(By.XPATH, "/html/body/div[3]/main/div[1]/div/div[2]/div[3]/div[3]/div/div/div/div/div/div[2]/section/div/div/div/div/div/div/div/div/div[2]/div[1]/div/textarea")
    if len(note_textarea) == 0:
        return False
    note_textarea[0].send_keys(config["note"])
    return True

def confirm():
    sleep(1)
    confirm_button = driver.find_elements(By.XPATH, "/html/body/div[3]/main/div[1]/div/div[2]/div[3]/div[3]/div/div/div/div/div/div[2]/section/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/div/div/div[1]/div/div/button")
    if len(confirm_button) == 0:
        return False
    # confirm_button[0].click()
    sleep(1)
    print(f"✅ Confirmed")
    return True

######### start #############
if __name__ == "__main__":
    print(f"🏁 START!")

    driver = setup()
    
    # make a pick
    with open("config.json", "r") as f:
        config = json.load(f)
        samples = list(config['weight'].keys())
        weights = list(config['weight'].values())
    
    ret = True
    for i in range(0, 5):
        print(f"🪖 Attempt n.{i + 1}")
        
        # Open website
        print(f"🌐 Loading website")
        driver.get(config["url"])

        pick = random.choices(samples, weights=weights)[0]
        secret_log(f"🎲 SELECTED: {pick}", "🎲 SELECTING SOMETHING")

        # Start
        start_button = driver.find_elements(By.XPATH, "//*[@id=\"root\"]/main/div[1]/div/div[2]/div[2]/div/section/div[1]/div/div/div/div/div/div[3]/div/div/div/button")
        if len(start_button) == 0:
            continue
        start_button[0].send_keys(Keys.ENTER)

        # Name
        print(f"🏌️‍♂️ Setting name: {config['name']}")
        name_input = driver.find_elements(By.XPATH, "//*[@id=\"block-ba44ca44-825f-449c-8809-ac604b19880f\"]/div/div/div/div/div/div/div/div[2]/div[1]/input")
        if len(name_input) == 0:
            continue
        name_input[0].send_keys(config["name"])
        name_input[0].send_keys(Keys.ENTER)

        ret = True
        if pick == "primo":
            if ret: ret &= pick_main_course()   # ✅ main
            if ret: ret &= next_section()      # ❌ follow
            if ret: ret &= next_section()      # ❌ fry
            if ret: ret &= pick_side()         # ✅ side
            if ret: ret &= next_section()      # ❌ water
        elif pick == "secondo":
            if ret: ret &= next_section()  # ❌ main
            if ret: ret &= pick_follow()   # ✅ follow
            if ret: ret &= next_section()  # ❌ fry
            if ret: ret &= pick_side()     # ✅ side 
            if ret: ret &= next_section()  # ❌ water
        elif pick == "poke":
            if ret: ret &= next_section()  # ❌ main
            if ret: ret &= pick_poke()     # ✅ follow
            if ret: ret &= next_section()  # ❌ fry
            if ret: ret &= next_section()  # ❌ side 
            if ret: ret &= next_section()  # ❌ water
        elif pick == "rosticceria":
            if ret: ret &= next_section()  # ❌ main
            if ret: ret &= next_section()  # ❌ follow
            if ret: ret &= pick_fry()      # ✅ fry
            if ret: ret &= pick_side()     # ✅ side 
            if ret: ret &= next_section()  # ❌ water

        if ret: ret &= set_notes()
        if ret: ret &= confirm()

        if ret:
            break

    if ret:
        print(f"😋 Enjoy the meal")
    else:
        raise Exception(f"❌ We did everything we could, but we failed 💔")
