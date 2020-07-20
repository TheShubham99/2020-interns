import json
from datetime import datetime
import matplotlib.pyplot as plt

#load data
with open('./data.json') as f:
    data=json.load(f)

ex_rate_jan=dict()
#iterate throgh all dates
for i in data['rates']:
    date_obj = datetime.strptime(i, '%Y-%m-%d').date()
    
    #compare month and year (from 1 Jan 2019 to 31 Jan 2019)
    if(date_obj.month==1 and date_obj.year==2019):
        #create a dictionary for ploting
        ex_rate_jan[date_obj.day]=data['rates'][str(i)]['INR']


#Sort the data i.e. from 1st Jan to 31st Jan
plot_list=sorted(ex_rate_jan.items())

#prepare for ploting
d, rate = zip(*plot_list)
plt.plot(d,rate)

#Labels
plt.xlabel('Dates (from 1 Jan 2019 to 31 Jan 2019)')
plt.ylabel('INR Exchange Rate (base:EUR)')

plt.show()