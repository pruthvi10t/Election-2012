import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import requests
from datetime import datetime

sns.set_style('whitegrid')

url = 'http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv'

source = requests.get(url).text
poll_data = StringIO(source)

poll_df = pd.read_csv(poll_data)

avg = pd.DataFrame(poll_df.mean())
avg.drop('Number of Observations',axis=0,inplace=True)

std = pd.DataFrame(poll_df.std())
std.drop('Number of Observations',axis=0,inplace=True)

plot1 = avg.plot(yerr = std,kind='bar',legend=False)

poll_avg = pd.concat([avg,std],axis=1)
poll_avg.columns = ['Average','STD']

print(poll_avg)

plot2 = poll_df.plot(x='End Date',y=['Obama','Romney','Undecided'],linestyle='',marker='o')
plt.show(plot2)

poll_df['Difference'] = (poll_df.Obama-poll_df.Romney)/100

poll_df = poll_df.groupby(['Start Date'],as_index=False).mean()
plot3 = poll_df.plot(x='Start Date',y='Difference',linestyle='-',marker='o')

plt.show(plot3)

#Analysing Setiments towards the candidates before and after the debate
#Plotting lines on 3 Debate days


plt.axvline(x=392+2,linewidth=4,color='grey')
plt.axvline(x =392+10,linewidth=4,color='grey')
plt.avxline(x=392+21,linewidth=4,color='grey')









