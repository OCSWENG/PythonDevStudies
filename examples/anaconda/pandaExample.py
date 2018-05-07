import pandas

# what can be done in excel spreadsheet studies can be done with 
# panda

# convert a list,numpy array, or dictionary to a Series()
# stored procedures can be put into an array

# DataFrames are an array of Series



#jupyter IDE
#matrix rows : columns
#df1 = pandas.DataFrame([[],[]])

#df1 = pandas.DataFrame([[],[]],columns=['C1','C2','C3'])

#df1 = pandas.DataFrame([[],[]],index=["r1","r2"])

#df2 = pandas.DataFrame([{"":""},{"":""}])

# add a column
# df['newColun'] = df['C0'] + df['C2']
# remove a column or a row
# df.drop('newColumn', axis=1)

# row selection by label
#df.loc['1']
# row selection by index
# df.iloc[2]

# bolean results
# df > 4

# get results and NaN
# df[df > 4]
# 
#df[(df['W']>0) & (df['Y'] > 1)]

# setting new index
# df.set_index('C5')

# mulit Indexing is possible


#outIdx = ['R1','R1','R1','R2','R2','R2']
#inidx = [1,2,3,1,2,3]
#index = list(zip(outIdx,inIdx))
#index = pd.MultiIndex.from_tuples(index)
# df.xs('R1')

# getting rid of Nan
# dropna
# fillna(-1)

# groupBy will form new data frames with all rows with the same column value

# powerful api
#df.describe().transpose()



#normally derived from data files

# Data Analysis
#dir(df1)

# panda series 
#df1.mean()

#df1.mean().mean()

#df1.C1

#df1.shape

#CSV (separated with commas)
#df4=pandas.read_csv("file.csv", header=None)

# JSON
#df4=pandas.read_json("file.json", header=None)
#df4.set_index("ID")
# label based indexing
#df5 = df4.set_index("C1")
#df5.loc["ValueRange1":"Value2Range2"]
#df5.loc[:"Column"]

# position based indexing
#df4.iloc[ range1:range2,1:4]
#df4.iloc[ 3,1:4]

#combine indexing [row, column]
#df4.ix[3,"name"]


# Merging, Joining , Concatenation

# df1, df2, df3 are dataFrames (4x4)
# panda.concat([df1,df2,df3], axis=0) axis=1 is along the columns
# panda.merge(leftDF,rightDF, how='inner', on='key') like SQL inner join, outer, right

# leftDF.join(rightDF)

# hdf, pickle, csv, excel(with spreadsheets), html, 

# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///memory')
# df.to_sql('myTable', engine)
# sqldf = pd.read_sql('my_table', con=engine)





# XLSX
#df4=pandas.read_excel('file.xlsx',sheetname=0)

# TXT with commas
#df4=pandas.read_csv('file.txt')

# TXT with semi-colons
#df4=pandas.read_csv('file2.txt',sep=";")


# GEOCODING
# ADDRESS to coordinates
# install geopy

#from geopy.geocoders import Nominatim
#nom = Nominatim(scheme='http')
#n = nom.geocode("3995 23rd st, San Francisco, CA 94114")
#n.latitude
#n.longitude

#df = pandas.read_csv('supermarkets.csv')
#df["Address"]=df["Address"] +","+df["City"]+","+df["State"]+","+df["Country"]

#df["Coordinates"]=df["Address"].apply(nom.geocode)
# add a latitude column
#df['lat']= df['coord'].apply(lambda x: x.latitude)


import os

def getFileSize(fileName)
	statInfo = os.stat(fileName)
	return statInfo.st_size

def sampleData (fileHandle, skipRate=2)
	for idx, Value in enumerate(fileHandle): 
		if idx % skipRate==0:
			print('Reading Line: ' + str(idx) + ' Content: ' + Value)


from random import random

def randomSampleData (fileHandle, skipRate=0.25)
	for idx, Value in enumerate(fileHandle):
		rdm = random() 
		if  rdm % skipRate==0:
			print('Reading Line: ' + str(idx) + ' Content: ' + Value)
	


# 10 MB
fileSizeMAX= 1024*1024*10

if(getFileSize('data.txt') <fileSizeMax ):
	with open("data.txt", 'rb') as open_file:
		print 'Dat file  content:\n' + open_file.read()

else:
	with open("Colors.txt", 'rb') as open_file: 
		for observation in open_file:
			print 'Reading Data: ' + observation


import pandas as panda
Atable = panda.io.parsers.read_table("Dat.txt") 
print color_table

aTable = panda.io.parsers.read_csv("Dat.csv")



# image Data

from skimage.io import imrear
from skimage.transform import resize 
from matplotlib import pyplot as plotter 
import matplotlib.cm as cm

picFile = ("http://website" + "directory/picture.png")
image = imread(picFile, as_grey=True)
plotter.imshow(image, cmap=cm.gray) 
plotter.show()

image3 = resize(image, (30, 30), mode='nearest') 
plotter.imshow(image3, cmap=cm.gray)

# After you have all the images the right size, 
# the next step is to flatten the image
image_row = image3.flatten()


# XML data

from lxml import objectify 
import pandas as panda

xml = objectify.parse(open('XMLData.xml')) 
root = xml.getroot()
df = panda.DataFrame(columns=('Number', 'String', 'Boolean'))
# common code to extract from xml
for i in range(0,4):
	obj = root.getchildren()[i].getchildren()
	row = dict(zip(['Number', 'String', 'Boolean'], [obj[0].text, obj[1].text,
	obj[2].text])) 
	row_s = pd.Series(row)
	row_s.name = i
	df = df.append(row_s)


print df


# Figure out what's in the data

# finding duplicates
# <See XML data to get df>

search = pd.DataFrame.duplicated(df)
print search[search == True]

 
 #The first task is to create a search object containing a list
 # of duplicated rows by calling pd.DataFrame.duplicated(). 
 #The duplicated rows contain a True next to their row number.

xml = objectify.parse(open('Dat2.xml'))
root = xml.getroot()
df = panda.DataFrame(columns=('Number', 'String', 'Boolean'))


df.drop_duplicates()


# data map and data plan 
# identify rendundant variables
# possible errors
# missing values
# variable transformations


a_group_desc = df.groupby('A').describe()
print a_group_desc

# data is crammed together, but you can break it apart
unstacked = a_group_desc.unstack()

# drill it down
unstacked.loc[:,(slice(None),['count','mean']),]

# creating a categorical variable and then using it to check 
# if some data falls within the specified limits

data = pd.Series(
panda.Categorical(['Yellow', 'Green', 'Red', 'Blue','Purple'], 
	categories=pd_series, ordered=False))

findEntries = pd.isnull(data)
findEntries[findEntries == True]


# combining categories to improve statistical values

data.cat.categories = ["Blue_Red", "Red", "Green"] 
print data.ix[data.isin(['Red'])]
data.ix[data.isin(['Red'])] = 'Blue_Red'

# numpy array slicing
x[:,1]

# numpy array dicing aka row and column slicing
print x[1,1]
print x[:,1,1]
print x[1,:,1]

df = df.sort_index(by=['A', 'B'], ascending=[True, True])
df = df.reset_index(drop=True)
index = df.index.tolist() 
np.random.shuffle(index)


# data aggregation
df['newColumn1'] = df.groupby('Column1')['Column2'].transform(np.sum) 
df['newColumn2'] = df.groupby('Column1')['Column2'].transform(np.mean) 
df['newColumn3'] = df.groupby('Column1')['Column2'].transform(np.var)

# CHAPTER 7 SHAPING DATA





