
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
#from apscheduler.schedulers.background import BackgroundScheduler
#from github import Github
import threading
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

import time
import json
import os

def running():
    # your existing running() function
    # Use ChromeOptions directly
    
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    
    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    #chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Use context manager to handle the WebDriver instance
    with webdriver.Chrome(options=chrome_options) as driver1:
        driver1.set_window_size(800, 600)
        #driver1.minimize_window()
        driver1.get("https://profitcentr.com/")
        #driver1.maximize_window()
        print("Please wait...")
        
        # Load cookies from file
        with open('account_1.json', 'r') as f:
            cookies = json.load(f)
        #time.sleep(2)
        # Add cookies to the browser session
        for cookie in cookies:
            driver1.add_cookie(cookie)
        #time.sleep(2)
        # Refresh the page to apply cookies
        driver1.get("https://profitcentr.com/profile")
        driver1.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.5)

        WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[1]/div/div[2]/div/center/div[1]/a[6]"))).click()
        time.sleep(0.5)
        while True:
            try:
                WebDriverWait(driver1, 2).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/div[1]/label[1]"))).click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/button"))).click()
              
            
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/div[1]/label[2]"))).click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/button"))).click()
            
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/div[1]/label[3]"))).click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/button"))).click()
            
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/div[1]/label[4]"))).click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/button"))).click()

                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/div[1]/label[5]"))).click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/button"))).click()

                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/div[1]/label[6]"))).click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div/div[2]/form/button"))).click()
            except:
                break
        v=50
        d=1
        while d < v:
            driver1.execute_script("window.scrollBy(0, 50);")
            time.sleep(0.3)
            d=d+1
           

        
    

        j=75
        i=50
        driver1.execute_script("window.scrollBy(0, 100);")
        time.sleep(2)
        #driver1.execute_script("window.scrollBy(0, 70);")
        while i < j: 
            try:
                driver1.execute_script("window.scrollBy(0, 40);")
                try:
                    WebDriverWait(driver1, 1).until(              
                        EC.presence_of_element_located((By.ID, "load-pages"))).click()
                    #driver1.execute_script("window.scrollBy(0, 400);")
                    #driver1.execute_script("window.scrollBy(0, 100);")
                except:
                    pass
                   
                window_before = driver1.window_handles[0]
                
                
                
                
                time.sleep(0.5)
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div[1]/div[3]/div[{i}]/table/tbody/tr/td[2]/div[1]/span[1]"))).click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"/html/body/div[8]/table[2]/tbody/tr/td[2]/div/div/div/div[1]/div[3]/div[{i}]/table/tbody/tr/td[2]/div[1]/div/span"))).click()
                print("ok")

                window_after = driver1.window_handles[1]
                driver1.switch_to.window(window_after)
                time.sleep(2)
       
                #driver1.get(modified_url)
                try:
                    driver1.switch_to.frame(WebDriverWait(driver1, 4).until(
                        EC.presence_of_element_located((By.XPATH, '//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))))

                    WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
        
                    driver1.switch_to.default_content()
                    WebDriverWait(driver1, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/button'))).click()
                    time.sleep(2)
                except:
                    pass
                
                driver1.close()
                driver1.switch_to.window(window_before)
                i = i+1
            except:
                 break


        driver1.get("https://profitcentr.com/members")
                # Save cookies to a new file
        file_path = "./account_1.json"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully..")

        cookies = driver1.get_cookies()
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']

        new = "./account_1.json"
        with open(new, 'w') as f:
            json.dump(cookies, f)

        print("Cookies copied successfully..")
        driver1.quit()
        
        

while True:
	try:
  	 	running()
	except:
   		continue



