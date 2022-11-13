import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
# cars_df = pd.read_csv(url)

# print(cars_df[['Manufacturer', 'Price']])


# exercise XP (1)
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(url)
print(titanic)


# (2)
male_data = titanic_df[titanic_df.Sex == 'male']
