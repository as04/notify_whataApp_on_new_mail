import email, getpass, imaplib, os, re
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

user = raw_input("Enter your GMail username --> ")
pwd = getpass.getpass("Enter your password --> ")
m = imaplib.IMAP4_SSL("imap.gmail.com")
print 'So far so good'
try:
    m.login(user, pwd)
except:
    print sys.exc_info()[1]
    sys.exit(1)
print 'logged in'
m.select('Inbox')
(ret, msgs) = m.search(None, '(UNSEEN)')
#(ret, msgs) = m.uid('search', 'UNSEEN')
mail_ids = msgs[0].split()
first_email_id = int(mail_ids[-1])
print "first email", first_email_id
typ, data = m.fetch(first_email_id, '(RFC822)')
msg = email.message_from_string(data[0][1])
subj = msg['subject']
msg_from = msg['from']
string = "Subject: "+subj +"\n From: "+ msg_from 
print "My string ", string 
m.close()
# driver = webdriver.Chrome("/home/surya/Documents/Anu/chromedriver")
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target = '"Testing"'
# string = "testing message"

# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located(( 
#     By.XPATH, x_arg))) 
# group_title.click() 
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
# input_box = wait.until(EC.presence_of_element_located(( 
#     By.XPATH, inp_xpath))) 
# for i in range(100): 
#     input_box.send_keys(my_string + Keys.ENTER) 
#     time.sleep(1) 


x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()


message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]


message.send_keys(string)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()

driver.close()

#if ret == 'OK':
#    for num in msgs[0].split(' '):
#        print 'Processing :', msgs
#        typ, data = m.fetch(num,'(RFC822)')
#        msg = email.message_from_string(data[0][1])
#        typ, data = m.store(num,'-FLAGS','\\Seen')
#        if ret == 'OK':
#            print data,'\n',30*'-'
#            print msg

