import json
from datetime import datetime
import matplotlib.pyplot as plt

#Console Data Input
print("Enter Start and Date:\n------------------------------------------")
print("From - ")
start_month=int(input("Enter Start Month (Numeric) i.e (1,2,3,etc.) :"))
start_date=int(input("Enter Start date (Numeric) i.e (1,2,3,etc.) :"))
start_year=int(input("Enter Start year (Numeric) i.e (2019,2020,etc.) :"))
print("\n\nTo - ")
end_month=int(input("Enter end Month (Numeric) i.e (1,2,3,etc.) :"))
end_date=int(input("Enter end date (Numeric) i.e (1,2,3,etc.) :"))
end_year=int(input("Enter end year (Numeric) i.e (2019,2020,etc.) :"))

#Currency Selection
currency=input("\nEnter currency abbreviation to Visualize (eg. USD,INR) -")

#Console Data Input End


#load data
with open('./data.json') as f:
    data=json.load(f)

ex_rate_jan=dict()
#iterate throgh all dates
for i in data['rates']:
    date_obj = datetime.strptime(i, '%Y-%m-%d').date()
    
    #compare date,month and year
    if((date_obj.month>=start_month and date_obj.year>=start_year and date_obj.day>=start_date) and (date_obj.month<=end_month and date_obj.year<=end_year and date_obj.day<=end_date)):
        #create a dictionary for ploting
        ex_rate_jan[date_obj.day]=data['rates'][str(i)][currency]


#Sort the data
plot_list=sorted(ex_rate_jan.items())

#prepare for ploting
d, rate = zip(*plot_list)
plt.plot(d,rate)

#Labels
plt.xlabel('Dates')
plt.ylabel(str(currency)+' Exchange Rate (base:EUR)')

plt.show()