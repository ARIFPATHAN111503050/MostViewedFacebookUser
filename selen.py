from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

usr = input("Enter user name of facebook account : ")
pas = input("Enter password of the facebook account : ")

url = 'http://www.facebook.com/'
#provide correct path to the chromedriver file in you computer if run on python interpreter.
driver = webdriver.Chrome("chromedriver")
driver.get(url)
driver.find_element_by_id('email').send_keys(usr)
driver.find_element_by_id('pass').send_keys(pas)
driver.find_element_by_id('loginbutton').click()
#print(driver.page_source)

#Beautiful soup concepts ahead.


html = driver.page_source
page_soup = soup (html,"html.parser")



#getting all script tag in array called scripts
scripts = page_soup.findAll("script")

#now iterating the scripts array to find that script tag that contains our magic word InitialChatFriendsList :D
for script in scripts:
    if "InitialChatFriendsList" not in script.text:
        continue
    else :
        textReq  = script.text
        print("your are welcome")


#regex for seperating the id's
id = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d-2')
grp = id.findall(textReq)

#now i have all the ids that i needed to display the top recent most viewed person

f = open("file.txt","w")
for i in range(len(grp)) :
    print(url+grp[i].replace('-2',''))
    uClient = uReq(url+grp[i].replace('-2',''))
    html = uClient.read()
    uClient.close()
    page_soup = soup (html,"html.parser")
    a = page_soup.find("a",{"class":"_2nlw _2nlv"})
    try:
        string = ( str(i + 1 ) + "]    " + a.text+ " " + "\n" )
    except AttributeError as err:
        print("error: no text attribute")
        continue
    else:
        f.write(string)
        print(string)
    finally:
        print(a)

f.close()
#writing on the file