import pyttsx3 as sp
import selenium
from selenium import webdriver
sp.speak("welcome to whatsapp ")
sp.speak("login to your account")
print("opening whatsapp")
sp.speak("opening whatsapp")
browser = webdriver.Chrome(r'C:\Users\Lenovo\Downloads\chromedriver_win32\chromedriver')
browser.get('https://web.whatsapp.com')

friend = input('Enter your friend name: ')
sp.speak("Enter your message")
message = input('Enter your message: ')
Number = int(input('Enter number of messages to send :'))
print("sending ....")

searchbox = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.send_keys(friend)
searchbox.send_keys(Keys.ENTER)

for i in range(Number):
  messagebox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
  messagebox.send_keys(message)
  messagebox.send_keys(Keys.ENTER)
print(" message sent")
