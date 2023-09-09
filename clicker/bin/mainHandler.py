from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import chromedriver_autoinstaller
import random
import time

from ..core.libs.tool import Kit

requests.packages.urllib3.disable_warnings()
chromedriver_autoinstaller.install()
kit = Kit.build()
cursor = kit.getCursor()

LIST_WITH_STATIC = [
	['https://github.com/', 1300],
]

@cursor.command("click")
def click():
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(options=options)
	counter = 0
	for clicker in LIST_WITH_STATIC:		
		while clicker[1] > 0:
			print(counter)
			driver.get(clicker[0])
			clicker[1] -= 1
			counter += 1
			time.sleep(random.randint(2, 5))
			
	
	

