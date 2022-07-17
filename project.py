import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import pandas as pd

data=pd.read_csv('StudentsPerformance.py')
mean = sum(data)/len(data)
print(mean)
std_dev = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
print(std_dev,median,mode)
std_dev_start_1,std_dev_end_1=mean-std_dev,mean+std_dev
std_dev_start_2,std_dev_end_2=mean-(2*std_dev),mean+(2*std_dev)
std_dev_start_3,std_dev_end_3=mean-(3*std_dev),mean+(3*std_dev)

fig=ff.create_distplot([data],['Result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
fig.show()

list_of_data_within_1_std_dev=[r for r in data if r> std_dev_start_1 and r < std_dev_end_1]
print(format(len(list_of_data_within_1_std_dev)*100.0/len(data)))