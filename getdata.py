from utils import *

url_legco_hk_vote_matrix = 'https://course.ie.cuhk.edu.hk/~engg4030/tutorial/tutorial7/votes-matrix.csv'
import pandas as pd
df = pd.io.parsers.read_csv(url_legco_hk_vote_matrix, index_col='member')
print 'number of users:', len(df.index)
print 'number of items:', len(df.columns)
df[:5]

# Convert votes to numeric values
def vote_to_numeric(v):
    if v == 'Yes':
        return 1
    elif v == 'No':
        return -1
    return 0
df = df.applymap(vote_to_numeric)
df[:5]

all_data_points = []
for item in df.columns:
    for user in df[item].keys():
        rating = df[item][user]
        all_data_points.append((user, item, rating))
print 'len of all_data_points:', len(all_data_points)
nonzero_data_points = filter(lambda x: x[2] != 0, all_data_points)
print 'len of nonzero_data_points:', len(nonzero_data_points)
print all_data_points[:5]

train_data_points, test_data_points = split_data_points(nonzero_data_points, int(0.9 * len(nonzero_data_points)))
print 'len of train_data_points:', len(train_data_points)
print 'len of test_data_points:', len(test_data_points)

import shelve
s = shelve.open('data.shelve')
s['train_data_points'] = train_data_points
s['test_data_points'] = test_data_points
s.close()
