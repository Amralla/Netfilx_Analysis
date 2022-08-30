from msilib import add_data
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
# read csv file
data_set=pd.read_csv('csv/netflix_titles.csv')

# print the first 5 lines
print(data_set.head())

# the last 5 lines data 
print(data_set.tail())

# the shape of data 
print(data_set.shape)

# size of data 
print(data_set.size)

# name of column 
print(data_set.columns)

# type of column
print(data_set.dtypes)

# information of data    Non-Null Count && dtypes && memory usage 
print(data_set.info())

# description of data 
print(data_set.describe().round())

# Task1  delte dupplicated data
print(data_set[data_set.duplicated()])
data_set.drop_duplicates(inplace=True)

# Task 2  delete null data or cleaning data    
# print(data_set.dropna(axis=0,how='any'))
# print(data_set.isnull().sum())
print("---------------null_data---------------------------")
print(data_set.isna().sum())
#and can show it by heatmap for seaborn
sns.heatmap(data_set.isnull())
plt.show()
# data_set.fillna(0,axis=0,inplace=True)
print(data_set.isna().sum())


# Task 3  show the row of column title  has Dick Johnson Is Dead 
print(data_set[data_set['title']=='Dick Johnson Is Dead'])
#or
data_set[data_set['title'].isin(['Dick Johnson Is Dead'])]
#or
data_set[data_set['title'].str.contains('Dick Johnson Is Dead')]

# Task 4          in which year and month height number of the tv show & movies were released ? show with Bar Graph
print(data_set.dtypes)
data_set['date_new']=pd.to_datetime(data_set['date_added'])
print(data_set['date_new'].dt.year.value_counts())

data_set['date_new'].dt.year.value_counts().plot(kind='bar')
plt.show()
data_set['date_new'].dt.month_name().value_counts().plot(kind='bar')
plt.show()


#how many move and show tv in dataset
print(data_set.groupby('type')['type'].count())
print(data_set['type'].value_counts())
sns.countplot(data_set['type'])
plt.show()
data_set['type'].value_counts().plot(kind='bar')
plt.show()


# Task 5     show all movies in 2020
print(data_set[(data_set['date_new'].dt.year==2020)&(data_set['type']=='Movie')]['type'].value_counts())

# Task 6  show only the title of all tv show were released in india only
task6=data_set[(data_set['type']=='TV Show')&(data_set['country']=='India')]
print(task6[['title','country']])

# Task 7   show top 10 directors ,whow gave the heights number of tv show and movies to |Netfilx
print(data_set['director'].value_counts().head(10))


# Task 8      show all records ,' where type is moives and listed_in is Comedies or country is India '
listed_in=data_set['listed_in'].isin(['Comedies'])
tupe=data_set['type']=='Movie'
count=data_set['country']=='United Kingdom'
print(data_set[(listed_in) & (tupe | count)])
print("\n\n")

# Task9 how many movies and shows ,Tom Cruise was cast
#abservation  IF COLUMN not HAVE NULL DATA will be used str.contains() or isin IF HAVE USE STR.CONTAINS()
data_frame=data_set.dropna()
tom=data_frame['cast'].str.contains('Tom Cruise')
print(data_frame[(tom)]['type'])

#  Task 10  what are the differient Rating defined by netfilx
print('\n',data_set['rating'].unique())
print('number of nunique data for rating \n',data_set['rating'].nunique())

# Task 11        how many movie got the "TV-14" rating in Canda

rat=data_set['rating'].isin(["TV-14"])
coun=data_set['country'].isin(["Canada"])
move=data_set['type'].isin(['Movie'])
print(' \nhow many movie got the "TV-14" rating in Canda \n',data_set[(rat) & (coun) & (move) ].shape[0])

# Task 15 How many Tv show got the 'R' rating  after year 2018
show=data_set['type'].isin(['TV Show'])
rating=data_set['rating'].isin(['R'])
date=data_set['date_new'].dt.year>=2018
print('\n',data_set[(show) & (rating) & (date)])

# Task 16 what the maximum duration of moives and shows on netfilx
print("\n\n",data_set['duration'].dtypes)
data_set[['Minutes','Uint']]=data_set['duration'].str.split(' ',expand=True)
data_set['Minutes']=pd.to_numeric(data_set['Minutes'])

print(" \n the max number  ",data_set['Minutes'].max())
print(" \n the min number  ",data_set['Minutes'].min())
print(" \n the mean number  ",data_set['Minutes'].mean())
print(" \n the median number  ",data_set['Minutes'].median())

# Task 17  sort database by year
print(data_set.sort_values(by='release_year'))

# Task 18   find all the instances 
# type is moives and listed_in  Dramas
# or type is tv show and listed_in Kids' Tv
tupe=data_set['type'].isin(['Movie'])
dram=data_set['listed_in'].isin(['Dramas'])
show=data_set['type'].isin(['TV Show'])
kids=data_set['listed_in']=="Kids' Tv"
print(data_set[(tupe & dram) | (show & kids)])

