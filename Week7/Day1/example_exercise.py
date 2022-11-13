import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# # df.shape
# # print(df)
# df.info()
# df.describe()

# exercise1

# def numpy_array(start,length,stop):
#     # stop = (stop-1*z)
#     end = (stop*length)-stop*start
#     return np.arange(start,end,stop)
# array = numpy_array(0,100,4)
# print(array)
# print(array.shape)


# exercise2
a = np.array([1,2,3,np.nan,5,6,7,np.nan])
print(a)




# exercise3
random_numpy = np.random.randint(100,size=100)
random_numpy = random_numpy.reshape(5,6)
print(np,max(random_numpy,axis-1))


# exercise4
series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
print(series.value_counts())


# exercise5


# exercise6

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df.rename(columns = {'Type':'Typeofcar'}, inplace = True)
print("the remaining was successful")
print(df.info())
print(df.isnull().sum().idxmax())
