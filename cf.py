import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

l=input("Enter lower rating: ")
r=input("Enter upper rating: ")
PATH = 'C:\WebDriver\chromedriver.exe'
driver = webdriver.Chrome(PATH)
action = ActionChains(driver)
driver.get('https://codeforces.com/problemset')
print("Entered")
driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[5]/form/div[1]/label/span/input[1]').send_keys(l)
driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[5]/form/div[1]/label/span/input[2]').send_keys(r)
driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[5]/form/div[4]/input').click()
print('values entered')
time.sleep(5)
elements=driver.find_elements_by_tag_name('a')
prb=[]
for val in elements:
  d=val.get_attribute('title')
  f=val.get_attribute('href')
  if (f.find('problemset/problem')==-1):
    f=-1
  else:
    prb.append(val.get_attribute('innerHTML'))
f=''
g=random.randrange(0,len(prb),2)
d=prb[g]
for i in d:
  b=str(i)
  if b==' ' or b=='\n':
    b=1
  else:
    f=f+b
driver.find_element_by_link_text(f).click()
print("Done")