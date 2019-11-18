import sqlite3
import webbrowser
import base64


number = input("please enter the number between 1 to 24")
numbers = int(number)
if number =="q":
    quit(0)
while numbers >24:
    input("please enter the number between 1 to 24")


con = sqlite3.connect('week10.db')
c = con.cursor()
query = "SELECT ID AND LINK FROM lab10"

result = c.execute(query)
for r in result.fetchall():
    print(base64.b64decode(r[1]))
    if r[0]==5:
        dburl = base64.urlsafe_b64decode(r[1]).decode('utf-8')
        webbrowser.open(dburl,2)

c.close

