# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:52:49 2020

@author: Azeemushan
"""

import pyttsx3
import os
import datetime
import smtplib
import wikipedia
import webbrowser
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen
import time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) 0-->male 1-->female
engine.setProperty('voice', voices[1].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def newsRead():
    site = 'https://news.google.com/news/rss'
    op = urlopen(site)
    read = op.read()
    op.close()
    soup_page  = soup(read,'xml')
    news_list = soup_page.findAll('item')
    for  news in news_list[:8]:
        print(news.title.text)
        speak(news.title.text)
        #print(news.link.text)
        print(news.pubDate.text)
        print("--"*50)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! Azeemushan Ali")
        speak("Good Morning! Azeemushan Ali")

    elif hour>=12 and hour<18:
        print("Good Afternoon! Azeemushan Ali")   
        speak("Good Afternoon! Azeemushan Ali")   

    else:
        print("Good Evening! Azeemushan Ali")  
        speak("Good Evening! Azeemushan Ali")  

    print("I am Alena Sir. Please tell me how may I help you")
    speak("I am Alena Sir. Please tell me how may I help you")
    
#speak('Hello World')
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
def icoulddo():
    icoulddo = "I could do following - \n*Open Chrome,Notepad,VS Code IDE\n*Send Email\n*Play Songs for you\n*Search anything in wikipedia or Youtube or Stack Overflow\n*Tell you today's News\n*Tell about my creator\n*Tell you about date & time\n*Ask What do you do? or ask for help anytime"
    print(icoulddo)
    speak(icoulddo.replace('*',' '))
        
    
if __name__ == "__main__":
    wishMe()
    icoulddo()
    state = 'in'
    while state == 'in':
        print("So what do you want me to do?")
        speak("So what do you want me to do?")
        command = input().lower()
#        command = command.lower()
        if 'wikipedia' in command:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            command = command.replace('search ','')
            command = command.replace('in wikipedia','')
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif ('what you do' or 'what do you do') in command:
            icoulddo()
        elif 'news' in command:
            newsRead()
        elif 'youtube' in command and 'search' in command:
            command = command.replace('search ','')
            command = command.replace('in youtube','')
            url = "https://www.youtube.com/results?search_query="
            speak('Launching your results in Chrome')
            webbrowser.open(url+command)
            time.sleep(5)
        elif 'search' in command and 'stackoverflow' in command:
            command = command.replace('search ','')
            command = command.replace('in stackoverflow','')
            url = "https://stackoverflow.com/search?q="
            speak('Launching your results in Chrome')
            webbrowser.open(url+command)
            time.sleep(5)
        elif ( 'launch' in command or 'execute' in command or 'run' in command or 'open' in command ) and 'chrome' in command:
            path = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"'
            os.system(path)
        elif ( 'launch' in command or 'execute' in command or 'run' in command or 'open' in command ) and 'notepad' in command:
            os.system('notepad')
        elif ( 'launch' in command or 'execute' in command or 'run' in command or 'open' in command ) and ('ide' in command or 'vs code'in command or 'code' in command or 'vscode'in command ):
            os.system('code')
        elif 'creator' in command:
            creator = "My Creator is Azeemushan Ali. Connect with him on Linkedin "
            print(creator)
            speak(creator)
#            speak('Launching your results in Chrome')
            webbrowser.open('https://www.linkedin.com/in/azeemushan-ali/')
            time.sleep(5)
        elif ('send email' in command):
            try:
                speak("What should I say?")
                content = input("What should I say?\n")
                speak("Please Enter the recipient email!")
                to = input("Please Enter the recipient email!\n")    
                #sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir !! . I am not able to send this email right now.Please try again later") 
        elif 'quit' in command or 'exit' in command or 'shutup' in command or 'shutdown' in command or 'shut down' in command or 'shut up' in command:
            speak("I hope you liked me Sir!!")
            speak('I am closing my services and shutting down')
            speak('Have a nice day')
            state = 'exit'
        elif 'help' in command:
            help_str= 'You want help for which command?'
            speak(help_str)
            help_cmd = input(help_str+'\n').lower()
            if 'wikipedia' in help_cmd:
                wiki_str = "Wikipedia command works like this - \n\
                Input 'Search Python in wikipedia' and you will hear your results  "
                print(wiki_str)
                speak(wiki_str)
            elif 'youtube' in help_cmd:
                yt_str = "Youtube command works like this - \n\
                Input 'Search Python Tutorials in youtube' and you will see your results soon "
                print(yt_str)
                speak(yt_str)
            elif 'stackoverflow' in help_cmd:
                yt_str = "Stakoverflow command works like this - \n\
                Input 'Search how to solve index out of bound in stackoverflow' and you will see your results opening soon "
                print(yt_str)
                speak(yt_str)
            elif 'news' in help_cmd:
                news_str = "Input 'Tell me todays news' or 'Read today's news' and you will hear the news soon  "
                print(news_str)
                speak(news_str)
            elif 'email' in help_cmd:
                email_str = "Send Email command works like this - \n \
                Input 'Send Email' or 'I want to send email' and you will hear \n \
                me to ask for the email content. Enter the email content \n\
                and then I will ask you to whom you want to send email? \n\
                Enter the email id of recipient and email will be sent !!"
                print(email_str)
                speak(email_str) 
            elif 'chrome' in help_cmd:
                chr_str = "Chrome command works like this - \n\
                Input 'Open chrome' or 'Please launch chrome for me' and you will see chrome opening soon "
                print(chr_str)
                speak(chr_str)
            elif 'notepad' in help_cmd:
                chr_str = "Notepad command works like this - \n\
                Input 'Open notepad' or 'Please launch notepad for me' and you will see notepad opening soon "
                print(chr_str)
                speak(chr_str)
            elif 'ide' in help_cmd or 'vscode' in help_cmd or 'vs code' in help_cmd:
                chr_str = "IDE command works like this - \n\
                Input 'Open VS Code' or 'Please launch my IDE for me' and you will see VS Code opening soon "
                print(chr_str)
                speak(chr_str)
            elif 'shutup' in help_cmd or 'shutdown' in help_cmd:
                chr_str = "Shutup command works like this - \n\
                Input 'Shutup' or 'Please Shut down' or 'will you please shut up!' or 'Get lost' and you will see me shutting down soon "
                print(chr_str)
                speak(chr_str)
            elif 'time' in help_cmd:
                chr_str = "Time command works like this - \n\
                Input 'What is the time' or \n \
                'Please tell me the time' or \n \
                'will you please tell what time it is?'\n \
                and you will hear me saying the excact time soon "
                print(chr_str)
                speak(chr_str)
            else:
                print("Please try with valid reason")
                speak("Please try with valid reason")
        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'play music' in command:
            music_dir = 'Songs\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            el_str = "I have no idea what you are saying. Kindly try taking help by inputting help"
            print(el_str)
            speak(el_str)
    
    
    
    
