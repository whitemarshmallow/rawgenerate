import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

warnings.filterwarnings("ignore")
# %matplotlib inline

train_data_file = "CSI_data.csv"
# test_data_file = "./zhengqi_test.txt"

train_data = pd.read_csv(train_data_file, encoding='utf-8')

print(train_data.info())

print(train_data.describe())