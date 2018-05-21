import math
from IPython import display
from matplotlib import cm, gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv(
    "https://storage.googleapis.com/mledu-datasets/california_housing_train.csv",
    sep=",")

california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0

# a demo of printing out the data
print(california_housing_dataframe)

# after we get our hands on the data we can exam it
# this is the pandas function we learned previously
print(california_housing_dataframe.describe())

## The building of the first model
## The feature column
# define the input feature: total room
my_feature = california_housing_dataframe[['total_rooms']]
# configure a numeric feature column for total_rooms
feature_columns = [tf.feature_column.numeric_column("total_rooms")]

## now we define the target
# define the label 
target = california_housing_dataframe["median_house_value"]

# Use gradient descent as the optimizer for training
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer,5.0)

# Configure the linear regression model with our feature columns and optimizer
# set a learning rate of 0.0000001 for the gradient desent
linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_columns,optimizer=my_optimizer)