# import pandas and matploltlib
import pandas as pd 
import matplotlib.pyplot as plt

# extracting the population 
population = pd.read_csv("../data/historical-world-population.csv")

# extarcting the internet users 

internet_users = pd.read_csv("../data/world-internet-users.csv")

# finding the 100 millions of users were crosed over 

over_100million = internet_users.query("internet_users > 100e6")
print("year of 100 millions of internet were croessed:",over_100million["year"].head(1))

# creatig a new csv file of name Fahh

Fahh = internet_users.merge(population,on = "year",how = "left")
# creating a new column for the percentage of internet is used by population 
Fahh['Percent'] =  Fahh.eval('internet_users/population*100').round(2)

#print(Fahh)
Fahh  = Fahh.dropna()
print(Fahh)


plt.plot(Fahh['year'], Fahh['Percent'])
plt.axhline(50,color = "green",linestyle = "--")
plt.xlabel("percent")
plt.ylabel("year")

plt.savefig("../outputs/internet_usesage.png")
plt.show()