import unittest
import selenium
import sys
from datetime import datetime
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


import time
f = open('C:\\Users\\lthalapa\\Desktop\\lakshmi\\studies\\ouput_%s.log'%datetime.now().strftime("%Y%m%d-%H%M%S"),'w')
print("Greetings! We are now in service now Automation for acknowledging the high sev tickets", file=f)
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities(), executable_path="C:\\Users\\lthalapa\\Desktop\\lakshmi\\studies\\chromedriver_win32\\chromedriver.exe")
driver.get("https://amexitsm.service-now.com")
time.sleep(20)
driver.maximize_window()
time.sleep(20)
try:
    driver.find_element_by_name("username").is_displayed()
    time.sleep(20)
    driver.find_element_by_name("username").send_keys("lthalapa")
    driver.find_element_by_css_selector("input[name=password]").send_keys("Laks@0905")
    driver.find_element_by_css_selector("input[type=submit]").click()
    print("Authentication sucessfull", file=f)
except:
    print("we are directly logging into the servicenow", file=f)
finally:
    wait=WebDriverWait(driver,30)
    wait.until(EC.element_to_be_clickable((By.ID,"filter")))
    navigator=driver.find_element(By.ID,"filter")
    time.sleep(30)
    navigator.send_keys("Unassigned")
    time.sleep(20)
    driver.find_element(By.XPATH,"//*[@id='0615c2985094600076e849ab90690669']/div/div").click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='0615c2985094600076e849ab90690669']")))
    driver.find_element_by_xpath("//*[@id='0615c2985094600076e849ab90690669']").click()
    time.sleep(10)
    driver.switch_to_frame("gsft_main")
    count = driver.find_elements_by_css_selector("a.linked.formlink")
    print("Number of Incidents : ", len(count),file=f)
    if len(count) > 0:
        print("List of incidents Unassigned:", file=f)
        for incident in count:
            print(incident.text, file=f)
        time.sleep(20)
        i=0
        while(len(count)>i):
            driver.find_elements_by_css_selector("a.linked.formlink")[i].click()
            time.sleep(20)
            incident = driver.find_element_by_css_selector("input[id='sys_readonly.incident.number']")
            select = Select(driver.find_element_by_css_selector("select[id='sys_readonly.incident.severity']"))
            desc = driver.find_element_by_css_selector("input[id='incident.short_description']")
            description = desc.get_attribute('value')
            incident_number = incident.get_attribute('value')
            selected_option = select.first_selected_option.text
            print("-----------------------------------------------------------------------------------------------------------------", file=f)
            print("-----------------------------------------------------------------------------------------------------------------", file=f)
            
            if selected_option in ['Sev1', 'Sev2']:
                #print("This is a High Sev ticket", file=f)
                driver.find_element_by_css_selector("span>button#inc_acknowledge").click()
                print(incident_number,"   :   ",selected_option,"   :   ",description," :  ","This is a High Sev ticket","---->Acknowledged suceessfully", file=f)
                time.sleep(20)
                driver.find_element_by_css_selector("button[role=link]").click()
                time.sleep(10)
                count = driver.find_elements_by_css_selector("a.linked.formlink")
                print("-----------------------------------------------------------------------------------------------------------------", file=f)
            else:
                #print(incident_number,"is not high sev ticket", file=f)
                print(incident_number,"   :   ",selected_option,"   :   ",description," :  ","This is not a High Sev ticket","----> Please Acknowledge manually", file=f)
                driver.find_element_by_css_selector("button[role=link]").click()
                time.sleep(20)
                count = driver.find_elements_by_css_selector("a.linked.formlink")
                time.sleep(10)
                i+=1
                print("-----------------------------------------------------------------------------------------------------------------", file=f)
        print("-----------------------------------------------------------------------------------------------------------------", file=f)
        count = driver.find_elements_by_css_selector("a.linked.formlink")
        if len(count) > 0:
            print("Remaining Tickets  :  ",len(count)," ----> Are low Sev tickets ", file=f)
        else:
            print("As of now there are no incidents", file=f)
            print("Thanks for your time", file=f)
    else:
        print("As of now there are no incidents", file=f)
        print("Thanks for your time", file=f)
time.sleep(10)
f.close()
driver.quit()

