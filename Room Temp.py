from os import stat
import plotly.figure_factory as pff
import statistics
import pandas as pd
import csv
import random
import plotly.graph_objects as pgo

df=pd.read_csv('room_temp.csv')
data=df['average'].tolist()

pop_mean=statistics.mean(data)
pop_stdev=statistics.stdev(data)
print("Mean = ",pop_mean,"  ","Standard Deviation = ",pop_stdev)

# graph=pff.create_distplot([data],['Temp'],show_hist=False)
# graph.show()

# dataset=[]

# for i in range(0,100):
#     index=random.randint(0,len(data)-1)
#     value=data[index]
#     dataset.append(value)

# sample_mean=statistics.mean(dataset)
# sample_stdev=statistics.stdev(dataset)
# print("Mean = ",sample_mean,"  ","Standard Deviation = ",sample_stdev)

def random_set_mean(counter):
    dataset=[]

    for i in range(0,100):
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return(mean)

def show_graph(mean_list):
    data=mean_list
    mean=statistics.mean(data)

    graph=pff.create_distplot([data],['Temp'],show_hist=False)
    graph.add_trace(pgo.Scatter(x=[mean,mean],y=[0,12],mode='lines',name="Mean"))
    graph.show()

def setup():
    mean_list=[]

    for i in range (0,1000):
        set_of_means=random_set_mean(100)
        mean_list.append(set_of_means)
    
    show_graph(mean_list)
    print(statistics.mean(mean_list))
    print(statistics.stdev(mean_list))

setup()