import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots
if __name__ == '__main__':
    print('This is intro to stat learning.')
    #region: random practice
    rng = np.random.default_rng(3)
    y = rng.standard_normal(10)
    A = np.random.randint(1, 100, 16).reshape(4, 4)
    print(A)
    idx = np.ix_([1, 3], [0, 2])
    print(A[idx])  # similar to A[[1, 3]][:, [0, 2]], or A[1:4:2, 0:3:2]
    # Easy Booleans
    kr = np.zeros(A.shape[0], bool)
    kr[[1, 3]] = True
    print(A[kr])   # returns 2nd and 4th row
    # pandas
    df = pd.read_csv(r'..\data\Auto.csv')
    df_re = df.set_index('name')
    print(df_re.iloc[0: [1, 4]])   # takes indices
    print(df_re.loc['ford galaxie 500', ['mpg', 'origin']])    # takes keys
    print(df_re.loc[lambda df_:(df_['year']>80) & (df['mpg']>30), ['weight', 'origin']])   # filtering
    #endregion