import pandas as pd
import numpy as np

require_cols = [6]
people_cols = [4]


#compare 2 files to find the person that is not in the crimes file

# setting the 3rd row as header.
df = pd.read_excel("Crimes.xlsx", sheet_name = 0, skiprows=11, usecols = require_cols)

#df[df[Name].str.contains("bello")]
df['Name'] = df['Name'].str.strip() #remove leading and trailing spaces
df['Name'].replace('', np.nan, inplace=True)
df.dropna(subset=['Name'], inplace=True) #remove empty rows
df.sort_values(by=['Name'])
#print(df.to_string())
df.to_csv('Crimes3.csv',  index=False,header=True,encoding='utf-8')
li = df['Name'].values.tolist()


df2 = pd.read_excel("People.xlsx", sheet_name = 0, skiprows=0, usecols = people_cols)
df2.columns.values[0] = 'People Name'  # creating a column name
df2['People Name'] = df2['People Name'].str.strip()   #remove leading and trailing spaces
df2['People Name'].replace('', np.nan, inplace=True)
df2.dropna(subset=['People Name'], inplace=True)  #drop empty rows
df2.sort_values(by=['People Name'])


li2 = df2['People Name'].values.tolist()


def get_difference(list_a, list_b):
    return set(list_a)-set(list_b)

#Get the person that is missing from the crime excel
non_match = list(get_difference(li2, li))
print("No match elements: ", non_match)


df2.to_csv('People3.csv',  index=False,header=True,encoding='utf-8')





