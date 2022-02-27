import time
import loguru
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random

def report(targets:list, accounts:list, parametr:str = 'l', random_from=8, random_to=10, separator_acc=':', separator_target=':'):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument(
        "accept_contents=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.9"
    )
    #options.add_argument('--headless')
    loguru.logger.debug('ay')
    #dr = webdriver.Remote('http://chrome:4444/wd/hub', options=options)
    dr = webdriver.Chrome(r'C:\Users\user\Desktop\chromedriver', options=options)
    time.sleep(2)
    for acc in accounts:
        dr.get('https://www.instagram.com/accounts/login')
        time.sleep(random.randint(random_from, random_to))
        el = dr.find_element(value='html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input', by=By.XPATH)
        el.send_keys(acc.split(separator_acc)[0])
        time.sleep(random.randint(random_from, random_to))
        el = dr.find_element(value='html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input', by=By.XPATH)
        el.send_keys(acc.split(separator_acc)[1])
        try:
            el = dr.find_element(value='html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div', by=By.XPATH)
            el.click()
        except:
            continue
        for target in targets:
            target = target.replace("https://www.instagram.com/", "")
            target = target.replace("/", "")
            try:
                parametr = parametr.split(separator_target)[1]
            except:
                parametr = parametr
            try:
                dr.get(f'https://www.instagram.com/{target}')
                time.sleep(random.randint(random_from, random_to))
                el = dr.find_element(value='html/body/div[1]/section/main/div/div/div/div/button', by=By.XPATH)
                el.click()
                time.sleep(random.randint(random_from, random_to))
                el = dr.find_element(value='html/body/div[1]/section/main/div/header/section/div[1]/div/button', by=By.XPATH)
                el.click()
                time.sleep(random.randint(random_from, random_to))
                el = dr.find_element(value='html/body/div[6]/div/div/div/div/button[3]', by=By.XPATH)
                el.click()
                time.sleep(random.randint(random_from, random_to))
                el = dr.find_element(value='html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]', by=By.XPATH)
                el.click()
                time.sleep(random.randint(random_from, random_to))
                el = dr.find_element(value='html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]', by=By.XPATH)
                el.click()
                time.sleep(random.randint(random_from, random_to))
                el = dr.find_element(value='html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]', by=By.XPATH)
                el.click()
                time.sleep(random.randint(random_from, random_to))
                if parametr == 'v':
                    el = dr.find_element(value='html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[6]/div/div[1]', by=By.XPATH)
                if parametr == 'n':
                    el = dr.find_element(value='html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[7]/div/div[1]', by=By.XPATH)
                if parametr == 'l':
                    el = dr.find_element(value='html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[11]/div', by=By.XPATH)
                el.click()
            except:
                continue
targets = open('targets.txt','r')
targets = targets.read().split(',')
accounts = open('accounts.txt','r')
accounts = accounts.read().split(',')
print(targets)
report(targets,accounts)