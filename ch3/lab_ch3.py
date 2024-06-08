import numpy as np
import pandas as pd
from matplotlib.pyplot import subplot
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF
from statsmodels.stats.anova import anova_lm
from ISLP import load_data
from ISLP.models import (ModelSpec as MS, summarize, poly)



if __name__ == "__main__":
    dir()
    print('This is Excercise 3')

