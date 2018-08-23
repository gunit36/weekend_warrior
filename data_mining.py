import pandas as pd
import os
import matplotlib.pyplot as plt
top_dir = os.getcwd()
stats_dir = r"Q://FantasyFB_2018//stats//"

stats16 = pd.read_csv(os.path.join(stats_dir,'passing2016.csv'))
#stats16 = stats16[stats16['TD']>5]
stats16['TDQGP'] = stats16['TD']/stats16['G']
stats16.hist(column='TDQGP')
stats16['Name'] = stats16['Name'].str.replace('*','')
stats16['Name'] = stats16['Name'].str.replace('+','')
stats16['Name'] = stats16['Name'].str.split('\\').str.get(0)
stats16['Year'] = 2016


#plt.show()

stats17 = pd.read_csv(os.path.join(stats_dir,'passing2017.csv'))
stats17 = stats17[stats17['TD']>5]
stats17['Name'] = stats17['Name'].str.replace('*','')
stats17['Name'] = stats17['Name'].str.replace('+','')
stats17['Name'] = stats17['Name'].str.split('\\').str.get(0)
stats17['Year'] = 2017
#stats17.hist(column='TD')
plt.show()

stats = pd.merge(stats16,stats17, on=['Name','Year'])

print('hello')
