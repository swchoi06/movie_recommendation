import pandas as pd
import numpy as np
import math
import sys

# Read prediction
# prediction = pd.read_csv('./dataset/small/quiz_small_answer.csv')
prediction = pd.read_csv(sys.argv[1])

# Read target
# target = pd.read_csv('./dataset/small/quiz_small_answer.csv')
target = pd.read_csv(sys.argv[2])

rmse = ((prediction.Rating - target.Rating) ** 2).mean() ** .5
mae = (abs(prediction.Rating - target.Rating)).mean()

print("Evaluating RMSE, MAE of algorithm")
print("---------")
print("RMSE: " + str(rmse))
print("MAE: " + str(mae))
print("---------")
