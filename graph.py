import numpy as np
import pandas as pd
import networkx as nx

df=pd.read_csv("~/Documents/datathon/Datathon_2018_Dataset_Hashbyte_New.csv")

conditions = [
    (df['Label'] == 'Low') & (df['Real_Event_Flag'] == 0),
    (df['Label'] == 'Low') & (df['Real_Event_Flag'] == 1),
    (df['Label'] == 'Medium'),
    (df['Label'] == 'High')
]

values= [0.5, 1, 2, 3]

df['Score']=np.select(conditions,values)

df_agg=df[['Subscriber_A','Subscriber_B','Score']].copy()
df_agg=df_agg.groupby(['Subscriber_A','Subscriber_B']).sum().reset_index()

subscribers=np.unique(df_agg[['Subscriber_A', 'Subscriber_B']].values)

G=nx.from_pandas_dataframe(df_agg,'Subscriber_A', 'Subscriber_B','Score')

number_of_neighbours=[]

for i in range(len(subscribers)):
    number_of_neighbours.append(len(G[subscribers[i]]))

number_of_neighbours=np.asarray(number_of_neighbours)

#im=subscribers[np.where(number_of_neighbours>270)]

#H=G.subgraph(im)
