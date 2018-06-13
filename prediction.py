import pandas as pd
import numpy as np
import math

def prediction(movie_id, user_id, date):
    return 3.0

# Read dataset
# prediction = pd.read_csv('./dataset/small/quiz_small_answer.csv')
df = pd.read_csv('./dataset/small/quiz_small.csv')

# Predict Rating
df['Rating'] = df.apply(lambda x:prediction(x['Movie_Id'], x['Cust_Id'], x['Date']), axis=1)

# Save to csv
df.to_csv('./result.csv', index=False)
