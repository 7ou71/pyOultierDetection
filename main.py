# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from scipy.spatial import distance_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.neighbors import LocalOutlierFactor


# import values phi+ and phi-
phi_data = pd.read_csv('/Users/sian/Downloads/classement exp84.csv', sep=';')
#data_roba= [[0,0,4,1],[0,0,1,4],[0,1,1,3],[0,2,1,2],[0,5,0,0],[0,1,2,2]]
# reate preference table and initialise it
zero_data = np.zeros(shape=(len(phi_data),4))
pref_table = pd.DataFrame(zero_data,columns=['I', 'P+', 'P-','R'])
print(pref_table)
# fill the preference table
for x in range(len(phi_data)):
    for y in range(x,len(phi_data)):
        if y==x :
            continue
        if (phi_data.at[x,'phi1']>phi_data.at[y,'phi1']) and (phi_data.at[x,'phi2']<phi_data.at[y,'phi2']) or (phi_data.at[x,'phi1']>phi_data.at[y,'phi1'] and phi_data.at[x,'phi2']==phi_data.at[y,'phi2'])or (phi_data.at[x,'phi1']==phi_data.at[y,'phi1'] and phi_data.at[x,'phi2']<phi_data.at[y,'phi2']):
            pref_table.at[x, 'P+'] = pref_table.at[x, 'P+']+1
            pref_table.at[y, 'P-'] = pref_table.at[y, 'P-']+1
        else:
            if (phi_data.at[x,'phi1']==phi_data.at[y,'phi1']) and (phi_data.at[x,'phi2']==phi_data.at[y,'phi2']):
                pref_table.at[x, 'I'] = pref_table.at[x, 'I'] + 1
                pref_table.at[y, 'I'] = pref_table.at[y, 'I'] + 1
            else:
                pref_table.at[x, 'R'] = pref_table.at[x, 'R'] + 1
                pref_table.at[y, 'R'] = pref_table.at[y, 'R'] + 1
print(pref_table)

# use the local outlier factor algo with pref_table
lof = LocalOutlierFactor(n_neighbors=40, contamination=.22)
out_indice = lof.fit_predict(pref_table)
print(out_indice)
# create outlier table for draw the plane
oult_table = pd.DataFrame(columns=['phi1','phi2'])
for x in range(len(out_indice)):
    if out_indice[x]==-1:
        oult_table.loc[oult_table.shape[0]]=phi_data.loc[x]
print(oult_table)
#draw plan
plt.scatter(phi_data.loc[:,'phi1'], phi_data.loc[:,'phi2'])
plt.scatter(oult_table.loc[:,'phi1'], oult_table.loc[:,'phi2'],color='r')

plt.show()

