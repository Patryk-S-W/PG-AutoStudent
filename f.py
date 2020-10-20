import contextlib
from selenium import webdriver
from getpass import getpass
import sys
import json
import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
       


if len(sys.argv) > 1:
    page = sys.argv[1]                
else:
    print("python f.py link")
    page = input("Link: ")

def load_config():
    global config
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)

def wait_until_found(sel, timeout):
    try:
        element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, sel))
        WebDriverWait(browser, timeout).until(element_present)

        return browser.find_element_by_css_selector(sel)
    except exceptions.TimeoutException:
        print(f"Timeout waiting for element: {sel}")
        return None


def main():
    global browser, config

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--lang=pl");
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if 'headless' in config and config['headless']:
        chrome_options.add_argument('--headless')
        print("Enabled headless mode")

    if 'mute_audio' in config and config['mute_audio']:
        chrome_options.add_argument("--mute-audio")

    chrome_type = ChromeType.GOOGLE
    if 'chrome_type' in config:
        if config['chrome_type'] == "chromium":
            chrome_type = ChromeType.CHROMIUM
        elif config['chrome_type'] == "msedge":
            chrome_type = ChromeType.MSEDGE     

    browser = webdriver.Chrome(ChromeDriverManager(chrome_type=chrome_type).install(), options=chrome_options)

    window_size = browser.get_window_size()
    if window_size['width'] < 950:
        browser.set_window_size(1020, window_size['height'])

    browser.get("https://logowanie.pg.edu.pl/login")

    if config['usernamePG'] != "" and config['passwordPG'] != "":
        login_email = wait_until_found("input[name='username']", 30)
        if login_email is not None:
            login_email.send_keys(config['usernamePG'])
            time.sleep(1)

        login_pwd = wait_until_found("input[name='password']", 5)
        if login_pwd is not None:
            login_pwd.send_keys(config['passwordPG'])
            time.sleep(1)

        time.sleep(1)
        submitAttedence = wait_until_found("input[id='submit_button']", 5)
        if submitAttedence is not None:
            submitAttedence.click()
        
        browser.get("https://enauczanie.pg.edu.pl/moodle/")
        browser.find_element_by_link_text("Zaloguj się").click()
        browser.find_element_by_xpath("//div/a/button[@value='Zaloguj się']").click()
        
        
        browser.get(page)
        time.sleep(1)
        submitAttedence = wait_until_found(".attendance.modtype_attendance a']", 5)
        if submitAttedence is not None:
            submitAttedence.click()
        
        browser.find_element_by_link_text("Zarejestruj obecność").click()
        browser.find_elements_by_css_selector("input[type='radio'][name='status']")[0].click()
        
        time.sleep(1)
        submitAttedence = wait_until_found("input[id='id_submitbutton']", 5)
        if submitAttedence is not None:
            submitAttedence.click()
        try:
            element_present = EC.presence_of_element_located((By.ID, 'user-notifications'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out")
        
        
        
    
    
if __name__ == "__main__":
    load_config()

    if 'run_at_time' in config and config['run_at_time'] != "":
        now = datetime.now()
        run_at = datetime.strptime(config['run_at_time'], "%H:%M").replace(year=now.year, month=now.month, day=now.day)

        if run_at.time() < now.time():
            run_at = datetime.strptime(config['run_at_time'], "%H:%M").replace(year=now.year, month=now.month, day=now.day + 1)

        delay = (run_at - now).total_seconds()

        print(f"Waiting until {run_at} ({int(delay)}s)")
        time.sleep(delay)

    try:
        main()        
        time.sleep(100)
    except NoSuchElementException:
        browser.quit()
        quit()
    except TimeoutException:
        browser.quit()
        quit()