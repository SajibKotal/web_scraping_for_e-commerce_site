from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.daraz.com.bd/products/arctic-hunter-outdoor-climbing-backpack-for-men-i216213294-s1164521235.html?spm=a2a0e.searchlist.list.1.6b596b21dIyGlJ&search=1")

comment_list=[]
h=driver.execute_script('return document.body.scrollHeight')

for p in range(0,h+1000,30):
    driver.execute_script(f'window.scrollTo(0,{p});')
    time.sleep(0.4)
    

all_comments=driver.find_elements(By.CLASS_NAME,'content')  

for i in all_comments:
    comment_list.append(i.text)
  


print(comment_list)
# response=requests.get(prod_img)

# with open("2.jpg","wb") as file:
#     file.write(response.content)

# print(title_list,"/n",link_list,"/n",img_list)

# driver.get(prod_link)

time.sleep(10)



import pandas as pd

data={'Comment':comment_list}

df=pd.DataFrame(data)
df.to_csv('comment.csv',index=False)