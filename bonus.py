import sqlite3
import base64

con = sqlite3.connect('week10.db')
c = con.cursor()
i = 0

a = ['','Brijesh','Yuanzhen Lin','Bing Yang','Vithura','Yong Shao','None','Patricia De Nardi','Chia Chin Chun','Jerome2','Radhika','Arash','Nikolai','Krishna'
,'Nazar'
,'Eduardo'
,'Fernando'
,'None'
,'None'
,'None'
,'Pushwinder Kaur'
,'None'
,'None'
,'None'
,'None'
,'Anusha'
,'Milan']

while i<26:
    with con:
        c.execute('UPDATE Lab10 SET Student = ? WHERE id = ?',(a[i],i))
        i = i + 1




