
import pandas as pd

bankDF = pd.read_csv('./banklist.csv')

# show the head of the dataFrame
bankDF.head()

columnNames = bankDF.columns

# find the number of states represented in this dataset

stateRepresentation = bankDF['ST'].nunique()

listOfStateRepresentation = bankDF['ST'].unique()

topFiveStates = bankDF.groupby('ST').count().sort_values('Bank Name', ascending=False).iloc[:5]['Bank Name']

topFiveAcquiring = bankDF['Acquiring Institution'].value_counts().iloc[:5]


banksAcqByBankOfTexas = bankDF[bankDF['Acquring Institution']=='State Bank of Texas']

# get all the banks of CA
#	Groupby City
#		count
#			present in decending Bank Name

bankDF[bankDF['ST']=='CA'].groupby('City').count().sort_values('Bank Name', ascending=False).head(1)


# what is the total number of banks that don't have a title Bank in their name
sum(bankDF['Bank Name'].apply(lambda x: 'Bank' not in x))


sum(bankDF['Bank Name'].apply(lambda x: x[0].upper() =='S'))


sum(bankDF['CERT'] > 20000)

sum(bankDF['Bank Name'].apply(lambda name: len(name.split())==2))

# pick the last two digits off of the date
sum(bankDF['Closing Date'].apply(lambda date: date[-2:]) == '08')





