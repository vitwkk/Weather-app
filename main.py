from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

#Load html file from website
url_local_weather = "https://pocasi.seznam.cz/brno"
result = requests.get(url_local_weather)

#initializing BeautifulSoup
doc = BeautifulSoup(result.text, "html.parser")

#Getting all elements with "°C", these elements also contain day name
degrees = doc.find_all(string="°C")


#Function that requires index of element which contains "°C"
#Then we get parent of where "°C" is
#Function converts this parent to text and we get actual degrees for this index
#Function converts index of this parent to day name in Czech language
#Function prints out the day and degrees for this index
#Function returns 2 values, one for degrees and second one for day name so i can make graph later
def daygrees(index):
    degrees_day = degrees[index].parent
    strong_day_dg = degrees_day.find("strong")
    day = degrees_day.find("div")
    day_txt = day.text
    print(f"{day_txt.capitalize()} bude {strong_day_dg.text}")
    return strong_day_dg, day

x = []
y = []
#for loop that loops through valid indexes so we get degrees for the next 6 days
#loop also gets degrees and day name from daygrees() function and stores them in a tuple
for i in range(15):
    if i % 2 == 1:
        if i != 1:
            day_dg, day_name = daygrees(i)
            y.append(day_dg.text)
            x.append(day_name.text)

#renders out the graph of degrees celsius for each day
plt.plot(x, y)
plt.xlabel('dny')
plt.ylabel('stupně')
plt.title('Počasí - dny a teploty')
plt.show()
