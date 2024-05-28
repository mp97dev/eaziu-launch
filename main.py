from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import json
import random
from time import sleep

poke_substrings = ['poke', 'pokè', 'poké']

def setup():
    print("Setting up webdriver...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
    driver.implicitly_wait(5)
    return driver

def log(pick):
    try:
        print(pick.find_elements(By.XPATH, 'div/div/div[2]')[0].text)
    except:
        print('upsy')

def next_section():
    sleep(1)
    next_button = driver.find_elements(By.XPATH, "//*[@id=\"stkv-form-root\"]/div[4]/div/div[2]/div[1]/div/div/nav/button[1]")
    if len(next_button) <= 0: raise Exception("No next button found")
    next_button[0].click()

def pick_main_course():
    print("🍝 Picking main course: ", end="")
    sleep(1)
    main_picks = driver.find_elements(By.XPATH, "//*[@id=\"block-dbed4899-9130-4194-8098-218dd064d7bf\"]/div/div/div/div/div/div/fieldset/div[2]/div/div[1]/div/div/div")
    if len(main_picks) <= 0: raise Exception("No main course found")
    pick=random.choice(main_picks)
    pick.click()
    log(pick)    

def pick_follow():
    print("🍖 Picking following: ", end="")
    sleep(1)
    foll_picks = driver.find_elements(By.XPATH, "//*[@id=\"block-d94294cc-5d4b-4d87-b2e4-af6e7b8093ba\"]/div/div/div/div/div/div/fieldset/div[2]/div/div[2]/div/div/div")
    if len(foll_picks) <= 0: raise Exception("No follow dish found")
    filtered_foll_picks = [elem for elem in foll_picks if "pokè" not in elem.get_attribute("innerHTML").lower()]
    pick=random.choice(filtered_foll_picks)
    pick.click()
    log(pick)

def pick_poke():
    print("🥑 Picking poke: ", end="")
    sleep(1)
    poke_picks = driver.find_elements(By.XPATH, "//*[@id=\"block-d94294cc-5d4b-4d87-b2e4-af6e7b8093ba\"]/div/div/div/div/div/div/fieldset/div[2]/div/div[2]/div/div/div")
    if len(poke_picks) <= 0: raise Exception("No follow dish found")

    filtered_poke_picks = [elem for elem in poke_picks if any(x in elem.get_attribute("innerHTML").lower() for x in poke_substrings)]
    if(len(filtered_poke_picks) <= 0): raise Exception("No poke found")

    pick=random.choice(filtered_poke_picks)
    pick.click()
    log(pick)

def pick_side():
    print("🍅 Picking side: ", end="")
    sleep(1)
    side_picks = driver.find_elements(By.XPATH, "//*[@id=\"block-120ded4b-5c30-483d-959d-44d36ed05eed\"]/div/div/div/div/div/div/fieldset/div[2]/div/div[2]/div/div/div")
    if len(side_picks) <= 0: raise Exception("side not founds")
    pick=random.choice(side_picks)
    pick.click()
    log(pick)

def pick_fry():
    print("🍤 Picking fry: ", end="")
    sleep(1)
    side_picks = driver.find_elements(By.XPATH, "//*[@id=\"block-bc594af9-461e-4741-b8f5-59a7b54bd861\"]/div/div/div/div/div/div/fieldset/div[2]/div/div[2]/div/div/div")
    if len(side_picks) <= 0: raise Exception("fry not founds")
    pick=random.choice(side_picks)
    pick.click()
    log(pick)

def set_notes():
    print("📓 Setting notes: " + config["note"])
    sleep(1)
    note_textare = driver.find_elements(By.XPATH, "/html/body/div[3]/main/div[1]/div/div[2]/div[3]/div[3]/div/div/div/div/div/div[2]/section/div/div/div/div/div/div/div/div/div[2]/div[1]/div/textarea")
    if len(note_textare) <= 0: raise Exception("missing note field")
    note_textare[0].send_keys(config["note"])

def confirm():
    sleep(1)
    confirm_button = driver.find_elements(By.XPATH, "/html/body/div[3]/main/div[1]/div/div[2]/div[3]/div[3]/div/div/div/div/div/div[2]/section/div/div/div/div/div/div/div/div/div[2]/div[3]/div/div/div/div/div[1]/div/div/button")
    if len(confirm_button) <= 0: raise Exception("Missing confirm button")
    confirm_button[0].click()
    sleep(1)
    print("✅ Confirmed")

######### start #############
if __name__ == "__main__":
    print("🏁 START!")

    driver = setup()
    # make a pick
    with open("config.json", "r") as f:
        config = json.load(f)
        samples=list(config['weight'].keys())
        weights=list(config['weight'].values())
        pick = random.choices(samples, weights=weights)[0]
        print("🎲 SELECTED: " + pick)

    print("🌐 Loading website")
    # Open website
    driver.get(config["url"])

    # Start
    start_button = driver.find_elements(By.XPATH, "//*[@id=\"root\"]/main/div[1]/div/div[2]/div[2]/div/section/div[1]/div/div/div/div/div/div[3]/div/div/div/button")
    if len(start_button) <= 0: raise Exception("missing Start button")
    start_button[0].send_keys(Keys.ENTER)

    print("🏌️‍♂️ Setting name: " + config["name"])
    # Name
    name_input = driver.find_elements(By.XPATH, "//*[@id=\"block-ba44ca44-825f-449c-8809-ac604b19880f\"]/div/div/div/div/div/div/div/div[2]/div[1]/input")
    if len(name_input) <= 0: raise Exception("missing name input")
    name_input[0].send_keys(config["name"])
    name_input[0].send_keys(Keys.ENTER)

    if pick == "primo":
        pick_main_course()   # ✅ main
        next_section()      # ❌ follow
        next_section()      # ❌ fry
        pick_side()         # ✅ side
        next_section()      # ❌ water

    if pick == "secondo":
        next_section()  # ❌ main
        pick_follow()   # ✅ follow
        next_section()  # ❌ fry
        pick_side()     # ✅ side 
        next_section()  # ❌ water

    if pick == "poke":
        next_section()  # ❌ main
        pick_poke()     # ✅ follow
        next_section()  # ❌ fry
        next_section()  # ❌ side 
        next_section()  # ❌ water

    if pick == "rosticceria":
        next_section()  # ❌ main
        next_section()  # ❌ follow
        pick_fry()      # ✅ fry
        pick_side()     # ✅ side 
        next_section()  # ❌ water

    set_notes()
    confirm()

    print("Closing")
