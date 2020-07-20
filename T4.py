import json
from datetime import datetime
import matplotlib.pyplot as plt
import requests 

parameters = {'start_at':'2019-01-01','end_at':'2019-01-31'} 


#fetch
r = requests.get(url = 'https://api.exchangeratesapi.io/history', params = parameters) 

#load data
data = r.json()

with open('./latest-rates.json') as f:
    latest_data=json.load(f)
 
ex_rate_inr_jan=dict()
ex_rate_gbp_jan=dict()

#iterate throgh all dates
for i in data['rates']:
    date_obj = datetime.strptime(i, '%Y-%m-%d').date()
    
    #compare month and year (from 1 Jan 2019 to 31 Jan 2019)
    if(date_obj.month==1 and date_obj.year==2019):
        #create a dictionary for ploting
        ex_rate_inr_jan[date_obj.day]=data['rates'][str(i)]['INR']
        ex_rate_gbp_jan[date_obj.day]=data['rates'][str(i)]['GBP']


#Sort the data i.e. from 1st Jan to 31st Jan
plot_list_inr=sorted(ex_rate_inr_jan.items())
plot_list_gbp=sorted(ex_rate_gbp_jan.items())


#prepare for ploting
#plot both graphs INR, GBP
d, rate = zip(*plot_list_inr)
plt.plot(d,rate,'ro-')
d, rate = zip(*plot_list_gbp)
plt.plot(d,rate,'bo-')

#plot latest data for INR and GBP
plt.plot(0, latest_data['rates']['INR']*(1/latest_data['rates']['EUR']), marker='x', markersize=12, color="red")

plt.plot(0, latest_data['rates']['GBP']*(1/latest_data['rates']['EUR']), marker='x', markersize=12, color="blue")


# Reference Box
plt.legend(('INR','GBP','Latest \nINR rate','Latest \nGBP rate \n\n(base:EUR)'),loc='best')

#Labels
plt.xlabel('Dates')
plt.ylabel('INR and GBP Exchange Rate (base:EUR)')

# Note
plt.figtext(0.4, 0.5, "Hover over any point on one of the two graphs\n to view the rate according to the date.\n\n (in bottom right cornor x is date in \nJAN 2019 & y is exchange rate.)\n\n Use zoom utility to view presice values.", ha="center", fontsize=7, bbox={"facecolor":"orange", "alpha":0.5, "pad":3})

plt.show()