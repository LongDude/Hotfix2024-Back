import pandas as pd

df = pd.read_excel('data/mean.xlsx')

print(df[df[4] == 0].shape[0])
df.reset_index(drop=True, inplace=True)

# df[4] = df.groupby([0,1])[4].apply(lambda x: x.interpolate())
df = df.groupby([0,1])[4].apply(
            lambda group: group.interpolate(method='spline', order=3)
        )
# for label,group in df.groupby([0,1]):
	# print(b)

print(df[df[4] == 0].shape[0])
df.to_excel('data/mean_fixed.xlsx', index=False)