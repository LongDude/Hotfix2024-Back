
import pandas as pd

df = pd.read_excel('train_old.xlsx')

new_order = [
    'airline', 'num_code', 'stop_type', 'time_taken', #brute force
    # 'dep_time', 'arr_time', # time
    'from', 'to', 'day', 'economy', # front data
    'price' # target
]
df = df[new_order]

df.to_excel('train.xlsx', index=False)



df = pd.read_excel('test_old.xlsx')

new_order = [
    # 'airline', 'numcode', 'stop_type', 'time_taken', #brute force
    # 'dep_time', 'arr_time', # time
    'from', 'to', 'day', 'economy', # front data
    'price' # target
]
df = df[new_order]

df.to_excel('test.xlsx', index=False)
