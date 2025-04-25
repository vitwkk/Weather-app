from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

#Load html file from website
url_local_weather = "https://pocasi.seznam.cz/brno"
result = requests.get(url_local_weather)

#initializing BeautifulSoup
doc = BeautifulSoup(result.text, "html.parser")

#Getting all elements with "°C"
degrees = doc.find_all(string="°C")


#Function that requires index of element which contains "°C"
#Then we get parent of where "°C" is
#Function converts this parent to text and we get actual degrees for this index
#Function converts index of this parent to day na
# me in Czech language
#Function prints out the day and degrees for this index
def daygrees(index):
    degrees_day = degrees[index].parent
    strong_day_dg = degrees_day.find("strong")
    day = degrees_day.find("div")
    day_txt = day.text
    print(f"{day_txt.capitalize()} bude {strong_day_dg.text}")



x = [1,2,3]
y = [2,4,1]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph!')
plt.show()



#for loop that loops through valid indexes so we get degrees for the next 6 days
for i in range(15):
    if i % 2 == 1:
        if i != 1:
            daygrees(i)




"""
degrees_today = degrees[3].parent
strong_today = degrees_today.find("strong")
den0 = degrees_today.find("div")
den0_txt = den0.text
print(f"{den0_txt.capitalize()} bude {strong_today.text}")
"""
"""
degrees_p1 = degrees[5].parent
strong_p1 = degrees_p1.find("strong")
den0 = degrees_today.find("div")
den0_txt = den0.text
print(f"{den0_txt.capitalize()} je {strong_today.text}")

degrees_p2 = degrees[7].parent
strong_p2 = degrees_p2.find("strong")
den0 = degrees_today.find("div")
den0_txt = den0.text
print(f"{den0_txt.capitalize()} je {strong_today.text}")



degrees_p3 = degrees[9].parent
strong_p3 = degrees_p3.find("strong")
den0 = degrees_today.find("div")
den0_txt = den0.text
print(f"{den0_txt.capitalize()} je {strong_today.text}")



degrees_p4 = degrees[11].parent
strong_p4 = degrees_p4.find("strong")
den0 = degrees_today.find("div")
den0_txt = den0.text
print(f"{den0_txt.capitalize()} je {strong_today.text}")



degrees_p5 = degrees[13].parent
strong_p5 = degrees_p5.find("strong")
den0 = degrees_today.find("div")
den0_txt = den0.text
print(f"{den0_txt.capitalize()} je {strong_today.text}")




"""
"""
dodelat abych misto zitra a pozitri atak mel datum a chci
udelat aby ten alogritmus byl kratsi a iteroval potom
udelat grafy 
"""