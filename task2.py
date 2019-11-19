import sqlite3
import webbrowser
import base64
con = sqlite3.connect('week10.db')
c = con.cursor()
query = "select id,link from lab10"

result = c.execute(query)
number = int(input("please enter"))
while True:
    if number>=1 and number<=24:
        for r in result.fetchall():
            if r[0] == number:
                dburl = base64.urlsafe_b64decode(r[1]).decode('utf-8')
                webbrowser.open(dburl, 2)
                print(base64.b64decode(r[1]))
                cityname = input("please input city name")
                countryname = input("please input country name")
                with con:
                    c.execute('UPDATE Lab10 SET City = ? WHERE id = ?', (cityname,number))
                with con:
                    c.execute('UPDATE Lab10 SET Country = ? WHERE id = ?', (countryname, number))
    else:
        number = int(input("please enter"))

con.close


