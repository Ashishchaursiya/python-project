import pyautogui as pg
import re
import time
name=input("what's your name\t")
print('hy   '+name)
print(' 1:-YOU CAN OPEN ANYTHING LIKE VIDEOS,IMAGE,SOFTWERE.BUT THAT SOFTWERE SHOULD BE EXIST IN YOUR SYSTEM')
print(' 2:-YOU CAN SEARCH ANY THING ON GOOGLE CHROME')
print(' 3:-YOU CAN WATCH ANYTHINF ON YOUTUBE')
while(1):
    str=input("HOW CAN I HELP YOU  ")
    x=re.search('open',str)
    if(x):
        x=re.split('open',str)
        pg.hotkey('winright')
        for i in x[-1]:
            pg.typewrite(i)
        time.sleep(3)
        pg.hotkey('\n')
    y=re.search('search',str)
    if(y):
        y=re.split('search',str)
        pg.hotkey('winright')
        for i in 'google chrome':
            pg.typewrite(i)
        time.sleep(2)
        pg.hotkey('\n')
        pg.alert(text='INTERNET CONNECTION SHOULD BE ENABLE',title='WARNING',button='OK')
        time.sleep(5)
        for i in y[-1]:
            pg.typewrite(i)
        time.sleep(2)
        pg.hotkey('\n')
        x, y = pg.size()
        time.sleep(2)
        res=pg.alert(text='YOUR CHROME WINDOW SHOULD BE MAXMIZE,FIRST OF ALL MAXMIZE YOUR WINDOW THEN PRESS OK,IF IT IS MAXMIZE,THEN IGNORE IT', title='WARNING', button='OK')
        time.sleep(3)
        pg.moveTo(x/5,250)
        pg.click()
    z=re.search('watch',str)
    if(z):
        z=re.split('watch',str)
        pg.hotkey('winright')
        for i in 'google chrome':
            pg.typewrite(i)
        time.sleep(2)
        pg.hotkey('\n')
        pg.alert(text='INTERNET CONNECTION SHOULD BE ENABLE', title='WARNING', button='OK')
        time.sleep(6)
        for i in 'youtube':
            pg.typewrite(i)
        time.sleep(2)
        pg.hotkey('\n')
        x,y=pg.size()
        time.sleep(2)
        pg.moveTo(x/2,100)
        pg.click()
        time.sleep(3)
        for j in z[-1]:
            pg.typewrite(j)
        time.sleep(3)
        pg.typewrite('\n')
        time.sleep(7)
        pg.moveTo(x/2,270)
        pg.click()
    k=re.search('stop',str)
    if(k):
        exit()

