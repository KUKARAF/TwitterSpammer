from selenium import webdriver
from getpass import getpass
from bs4 import BeautifulSoup
import time
driver = webdriver.Firefox()
def login_twitter(username, password,driver):

    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)

    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()


if __name__ == "__main__":
    #username = input("user name : ")
    #password = getpass("password  : ")
    username = ""
    password = ""
    login_twitter(username, password, driver )

    driver.get('https://twitter.com/8btbrs/followers')


def getUsrFlwr():
    followers_link=driver.page_source  #follwer page 18at a time
    soup=BeautifulSoup(followers_link,'html.parser')

    #output=open('twitter_follower_sadoperator.csv','a')
    #output.write('Name,Twitter_Handle,Location,Bio,Join_Date,Link'+'\n')
    div = soup.find('div',{'class':'GridTimeline-items has-items'})
    bref = div.findAll('a',{'class':'ProfileCard-bg js-nav'})
    name_list=[]
    lastHeight = driver.execute_script("return document.body.scrollHeight")

    followers_link=driver.page_source  #follwer page 18at a time
    soup=BeautifulSoup(followers_link,'html.parser')

    followers_per_page = 18
    followers_count = 15777


    for _ in xrange(0, followers_count/followers_per_page + 1):
            driver.execute_script("window.scrollTo(0, 7755000);")
            time.sleep(2)
            newHeight = driver.execute_script("return document.body.scrollHeight")
            if newHeight == lastHeight:
                    followers_link=driver.page_source  #follwer page 18at a time
                    soup=BeautifulSoup(followers_link,'html.parser')
                    div = soup.find('div',{'class':'GridTimeline-items has-items'})
                    bref = div.findAll('a',{'class':'ProfileCard-bg js-nav'})
                    for name in bref:
                            name_list.append(name['href'])
                    break
            lastHeight = newHeight
            followers_link=''

            print len(name_list)
            thefile = open('test.txt', 'w')

            for item in name_list:
              thefile.write("%s\n" % item)
            thefile.close()

    t = (line.rstrip('\n') for line in open('test.txt', 'r'))
    s=[]
    for i in t:
       if i not in s:
          s.append(i)
    #getUsrFlwr()

    """
    for usrrr in s:
    driver.get("https://twitter.com" + usrrr +  "/followers")
    getUsrFlwr()
    """
