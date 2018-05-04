
#given a dataset interpret the data using lambdas

data = [44,92,2,6,22,29,33,13,-1,8,-21,17]

#find all even/odd numbers
evens = filter(lambda a: a%2 ==0, data)
odds  = filter(lambda a: a%2 ==1, data)


#add value to the data set
mappedData = map(lambda a: a /3, data)

# sum up the data
reduction = reduce(lambda a,b: a-b, data)

print("data: ", data)
print("evens: " , evens)
print("odds: ", odds)
print("Mapped by dividing by 3: " , mappedData)
print("Reduction (a - b) : ", reduction)

words = ["data", "evens", "odds", "Mapped", "by", "dividing","Reduction"]
lengths = map(lambda word: len(word), words)
print ("words: ", words)
print ("word lengths: ", lengths)


