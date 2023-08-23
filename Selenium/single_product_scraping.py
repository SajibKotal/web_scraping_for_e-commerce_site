from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.daraz.com.bd/men-muslimin-shirts/")

title_list=[]
link_list=[]
img_list=[]

for p in range(1,41):
    k=str(p)
    prod_title= driver.find_element(By.XPATH,value='//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+k+']/div/div/div[2]/div[2]/a').text

    prod_link= driver.find_element(By.XPATH,value='//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+k+']/div/div/div[2]/div[2]/a').get_attribute('href')

    prod_img=driver.find_element(By.XPATH,value='//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+k+']/div/div/div[1]/div/a/img').get_attribute('src')

    title_list.append(prod_title)
    link_list.append(prod_link)
    img_list.append(prod_img)

# response=requests.get(prod_img)

# with open("2.jpg","wb") as file:
#     file.write(response.content)

print(title_list,"/n",link_list,"/n",img_list)

# driver.get(prod_link)
driver.maximize_window()
time.sleep(10)

# # Find an element on the page using its XPath or CSS selector
# element = driver.find_element_by_xpath("//div[@class='example']")

# # Extract the text or attribute value from the element
# text = element.text
# attribute_value = element.get_attribute("attribute_name")

import pandas as pd

data={'Title':title_list,'Link':link_list,'Image':img_list}

df=pd.DataFrame(data)
df.to_csv('output.csv',index=False)