from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.daraz.com.bd/")
driver.maximize_window()

hover_element = driver.find_element(By.XPATH, '//*[@id="Level_1_Category_No9"]/a/span')

#hover_element3 = driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li[1]/ul/li[1]/a/span')

# h4=driver.find_element(By.XPATH,'//*[@id="J_3442298940"]/div/ul/ul[9]/li[2]/a/span')
# h5=driver.find_element(By.XPATH,'//*[@id="J_3442298940"]/div/ul/ul[9]/li[2]/ul/li[1]/a/span')


for i in range(1,9):
    h=str(i)
    hover_element2 = driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/a/span')
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).move_to_element(hover_element2).perform()
    
    if (i==1):
        fruits_link=[]
        for p in range(1,6):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li[1]/ul/li['+k+']/a').get_attribute('href')
            fruits_link.append(link)
            data={'fruits Meats & Frozen':fruits_link}

            df=pd.DataFrame(data)
            df.to_csv('fruits Meats & Frozen.csv',index=False)
    if(i==2):    
        breakfast_link=[]
        for p in range(1,11):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/ul/li['+k+']/a').get_attribute('href')
            breakfast_link.append(link)
            data={'Breakfast':breakfast_link}

            df=pd.DataFrame(data)
            df.to_csv('Breakfast.csv',index=False)
    if(i==3):    
        cooking_ingredients_link=[]
        for p in range(1,12):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/ul/li['+k+']/a').get_attribute('href')
            cooking_ingredients_link.append(link) 
            data={'Cooking_Ingredients':cooking_ingredients_link}

            df=pd.DataFrame(data)
            df.to_csv('Cooking_Ingredients.csv',index=False)       

    if(i==4):    
        snacks_baverages_link=[]
        for p in range(1,13):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/ul/li['+k+']/a').get_attribute('href')
            snacks_baverages_link.append(link)
            data={'Snacks Baverages':snacks_baverages_link}

            df=pd.DataFrame(data)
            df.to_csv('Snacks Baverages.csv',index=False)        
    if(i==5):    
        dairy_eggs_link=[]
        for p in range(1,5):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/ul/li['+k+']/a').get_attribute('href')
            dairy_eggs_link.append(link)
            data={'Dairy Eggs':dairy_eggs_link}

            df=pd.DataFrame(data)
            df.to_csv('Dairy Eggs.csv',index=False)
    if(i==6):    
        herbs_spices_link=[]
        for p in range(1,13):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/ul/li['+k+']/a').get_attribute('href')
            herbs_spices_link.append(link)
            data={'Herbs Spices & Sauces':herbs_spices_link}

            df=pd.DataFrame(data)
            df.to_csv('Herbs Spices & Sauces.csv',index=False)
    if(i==7):    
        chocolets_candy_link=[]
        for p in range(1,13):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/ul/li['+k+']/a').get_attribute('href')
            chocolets_candy_link.append(link)
            data={'Chocolets Candy':chocolets_candy_link}

            df=pd.DataFrame(data)
            df.to_csv('Chocolets Candy.csv',index=False)
    if(i==8):    
        loundry_household_link=[]
        for p in range(1,11):
            k=str(p)
            link=driver.find_element(By.XPATH, '//*[@id="J_3442298940"]/div/ul/ul[9]/li['+h+']/ul/li['+k+']/a').get_attribute('href')
            loundry_household_link.append(link)
            data={'Loundry & household':loundry_household_link}

            df=pd.DataFrame(data)
            df.to_csv('Loundry & Household.csv',index=False)        

print(len(fruits_link))

print("fruits: ",fruits_link)





print(len(breakfast_link))
print("breakfast: ",breakfast_link)
# actions.move_to_element(hover_element2).perform()
print(len(cooking_ingredients_link))
print("cooking: ",cooking_ingredients_link)

print(len(snacks_baverages_link))
print("snacks: ",snacks_baverages_link)
print("dairy_eggs: ",dairy_eggs_link)

print(len(herbs_spices_link))
print("herbs_spices:",herbs_spices_link)

print(len(chocolets_candy_link))
print("chocolets_candy",chocolets_candy_link)

print(len(loundry_household_link))
print("loundry_household:",loundry_household_link)




# driver.get(prod_link)

time.sleep(50)



# import pandas as pd

# data={'Title':title_list,'Link':link_list,'Image':img_list}

# df=pd.DataFrame(data)
# df.to_csv('output.csv',index=False)