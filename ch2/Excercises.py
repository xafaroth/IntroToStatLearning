import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')
from matplotlib.pyplot import subplots


def run28():
    print('Excercise 2.8')
    rng = np.random.default_rng(3)
    college1 = pd.read_csv(r'..\data\College.csv')
    college2 = pd.read_csv(r'..\data\College.csv', index_col=0)
    college3 = college1.rename({'Unnamed: 0': 'College'}, axis=1)
    college3 = college3.set_index('College')
    college = college3
    print('Describing the data')
    print(college.describe())
    pd.plotting.scatter_matrix(college[['Top10perc', 'Apps', 'Enroll']], figsize=(10, 10))
    college.boxplot(column='Outstate', by='Private')
    college['Elite'] = pd.cut(college['Top10perc'], bins=[0, 50, 100], labels=['No', 'Yes'])
    college.boxplot(column='Outstate', by='Elite')
    fig, ax = plt.subplots(1, 2)
    ax[0].hist(college['Top10perc'])
    ax[1].hist(college['Top25perc'])
    print('sth')

def run29():
    auto = pd.read_csv(r'..\data\Auto.csv')
    print(auto.describe())
    print('Range of quantitative vairable {} is [{}, {}]'.
          format('displacement', auto['displacement'].min(), auto['displacement'].max()))
    print('Range of qualitative vairable {} is [{}, {}]'.
          format('origin', auto['origin'].min(), auto['origin'].max()))
    auto1 = auto.drop(auto.index[10:85])
    print(auto1.describe())
    pd.plotting.scatter_matrix(auto[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin']], figsize=(10, 10))
    print('From the scatterplot, it seems cylinders, displacement, weight, and to some extent acceleration'
          ' can be good predictors for mpg')

def run210():
    boston = pd.read_csv(r'..\data\Boston.csv')
    print('Boston data has {} rows and {} columns'.format(boston.shape[0], boston.shape[1]))
    print(boston.describe())
    pd.plotting.scatter_matrix(boston[['crim', 'zn', 'lstat', 'ptratio', 'tax']], figsize=(10, 10))
    pd.plotting.scatter_matrix(boston[['crim', 'indus', 'chas', 'nox', 'rm']], figsize=(10, 10))
    pd.plotting.scatter_matrix(boston[['crim', 'age', 'dis', 'rad', 'medv']], figsize=(10, 10))
    print('From first figure, it seems the crime rate is high at particular zn, ptratio, and tax values')
    print('From second figure, it seems the crime rate is high at particular indus, and category of chas')
    print('From third figure, it seems the crime rate has some correlation with age, and value of rad')
    print(boston.loc[boston['crim'] > 1, ['zn']])
    print('There are 174 rows with crime rate > 1, and all have zn=0')
    crimZone = boston.loc[boston['zn'] == 0]
    crimZone.boxplot(column=['zn'], by='chas')
    print('The boxplot shows that zn=0 is more common for chas=0')

if __name__ == '__main__':
    print('Excercises 2.8 till 2.10')
    # run28()
    # run29()
    run210()
