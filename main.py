from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import chromedriver_autoinstaller


#chromedriver_autoinstaller.install()

# path to selenium server standalone jar, downloaded here:
# http://docs.seleniumhq.org/download/
# or a direct url:
# http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar
os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
import time
browser = webdriver.Firefox(executable_path="C:\dev\geckodriver.exe")
#browser = webdriver.Firefox()

# makes the browser wait if it can't find an element
browser.implicitly_wait(10)

browser.get("https://mesh.uia.no/")

hir = browser.find_element(By.PARTIAL_LINK_TEXT, "Hierarki-søk")
hir.click()
foundAll = False
browser.implicitly_wait(3)
print("done waiting")
items = []
time.sleep(2)
failStrenght=0
while not foundAll:
    #Wt-ctrl rh expand
    try:
        time.sleep(0.1)
        plusButton = browser.find_element(By.XPATH, "//div[contains(@class, 'Wt-ctrl rh expand')]")
        plusButton.click()
    except Exception:
        failStrenght += 1
        print(failStrenght)
        print(Exception)
        if failStrenght > 2000:
            foundAll = True

items = browser.find_elements(By.XPATH, "//div[contains(@class, 'Wt-tv-c2 Wt-tv-c rh ')]")
with open("items.txt", "w+") as file:
    for x in items:
        file.write(x.text+"\n")


browser.quit()
print("Done")



