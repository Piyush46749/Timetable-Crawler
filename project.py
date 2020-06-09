from bs4 import BeautifulSoup
import requests
import smtplib, ssl
from email.message import EmailMessage


source=requests.get('https://dalonline.dal.ca/PROD/fysktime.P_DisplaySchedule?s_term=202030&s_subj=CSCI&s_district=100').text.(gibberish_cqatwlmrjfdabndn_to_prevent_from_hitting_the_request)
print(source)
soup=BeautifulSoup(source,'lxml')
entire=soup.find_all('tr')[-8]
for each in entire.find_all('td')[-9]:
	registered=each.text
	regNum=int(registered)

if(regNum>=0):
	# create an email message with just a subject line,
        msg = ('Number of students registered in the course is: ' + str(regNum))
        # set the 'from' address,
        fromaddr = 'piyush46749@gmail.com'
        # set the 'to' addresses,
        toaddrs  = ['piyush46749@gmail.com', 'piyush@dal.ca']
        
        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("piyush46749@gmail.com", "<your_server_login_password>")
        
        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

else:
	print("ERROR!!")
