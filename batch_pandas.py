# Data types:
# Series: 1-D labelled Array
# Dataframe: 2-D Array with columns of diff datatypes

import numpy as np, pandas as pd
"""
# s = pd.Series(data, index = index)
my_index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(np.random.randn(5), index=my_index)
print(s)
print(s.index)

d = {'a': 0., 'b': 'kd.', 'c': 2.}
s = pd.Series(d)
print(s)
s = pd.Series(d, index=my_index)
print(s)

s = pd.Series(5., index=my_index, name='Seriesname', dtype=int)
print(s)

print(s[0])
print(s['a'])
print('a' in s)

print(s + s)
print(s ** 2)
print(np.sqrt(s))

print(s[2:] + s[:-1])

# >>>>>>Dataframes>>>>
# DataFrame accepts many different kinds of input:
#
# > Dict of 1D ndarrays, lists, dicts, or Series
# > 2-D numpy.ndarray
# > Structured or record ndarray
# > A Series
# > Another DataFrame

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

df = pd.DataFrame(d, index=['d', 'b', 'a'])
print(df)
df = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
print(df)
print(df.columns)
print(df.index)

d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
df = pd.DataFrame(d)
print(df)

data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
df = pd.DataFrame(data)
print(df)

df['flag'] = df['A'] > 2
print(df)

data2 = [{'a': 'kd', 'b': 4}, {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data2, index=my_index[:-2])
print(df)
df['a_trunc'] = df['a'][:2]
print(df)

df.insert(1, 'col_name', df['a'])
print(df)

# print(df.T)
# print(df.T.dot(df))




# >>>>>>> INDEXING/SELECTION >>>>>>>

# The basics of indexing are as follows:
#
# > Operation	                        Syntax	            Result
# > Select column	                    df[col]	            Series
# > Select row by label	                df.loc[label]	    Series
# > Select row by integer location	    df.iloc[loc]	    Series
# > Slice rows	                        df[5:10]	        DataFrame
# > Select rows by boolean vector	    df[bool_vec]	    DataFrame
data2 = [{'a': 1, 'b': 4}, {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data2, index=my_index[:-2])

print(df['a'])
print(df.loc['c'])
print(df['a'].loc['c'])
print(df['a'].iloc[1])
print(df[df['a'] < 3])

# >>>>>>Reading flat files>>>>>>>
baseball = pd.read_csv('baseball.csv')
# print(baseball)
# print(baseball.info())
# print(baseball.head())
# similarly you can use pd.read_excel(), pd.read_json() and so on...

# >>>>>> for SAS datasets
#
# import sas7bdat as sas
# import pandas as pd
# data = sas.SAS7BDAT("sasdataset_name.sas7bdat")
#
# df = data.toDataFrame()
# further reading for comparison with SAS
# https: // pandas.pydata.org / pandas - docs / stable / comparison_with_sas.html


# handling missing data

dff = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))
dff.iloc[3:5, 0] = np.nan
dff.iloc[4:6, 1] = np.nan
dff.iloc[5:8, 2] = np.nan
print(dff)
dff2 = dff.copy()
print(dff.isnull())
print(dff.notnull())
#
# dff = dff.fillna('missing')
# print(dff)
dff = dff.fillna(dff.mean())
# print(dff)
# del dff2['A']
print(dff2.dropna(axis=0))  # 0 for rows
# print(dff2.dropna(axis=1)) # 1 is for columns

# df.replace('.', np.nan)

"""
# >>>>>>>>>END NOW>>>>>>>>>>>>>>>>

# >>>>>>GROUP BY>>>>>>>>

# https://chrisalbon.com/python/pandas_apply_operations_to_groups.html
# official doc : https://pandas.pydata.org/pandas-docs/stable/groupby.html
# gb.agg        gb.boxplot    gb.cummin     gb.describe   gb.filter     gb.get_group  gb.height     gb.last       gb.median     gb.ngroups    gb.plot       gb.rank       gb.std        gb.transform
# gb.aggregate  gb.count      gb.cumprod    gb.dtype      gb.first      gb.groups     gb.hist       gb.max        gb.min        gb.nth        gb.prod       gb.resample   gb.sum        gb.var
# gb.apply      gb.cummax     gb.cumsum     gb.fillna     gb.gender     gb.head       gb.indices    gb.mean       gb.name       gb.ohlc       gb.quantile   gb.size       gb.tail       gb.weight



df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

# print(df)

grouped = df.groupby('A')
print(grouped)

for name, group in grouped:
    print(name)
    print(group) #prints df group
    print(grouped.get_group(name))

print(type(grouped.get_group('bar')))
print(grouped.get_group('bar').max())
print(grouped.get_group('bar').max()['A'])

grouped = df.groupby(['A','B'])
print(grouped) # this will print only the object

for name, group in grouped:
    print(name) # now its a tuple having 4 combnations
    print(group)
    print(grouped.get_group(name))

print(type(grouped.get_group(('bar','one'))))
print(grouped.get_group(('bar','one')).max())
print(grouped.get_group(('bar','one')).max()['A'])


# >>>>>>>>>
print(grouped.indices)
print(grouped.indices.keys())
print(grouped.indices.values())

# splitting by rows
grouped = df.groupby(['A'])
grouped2 = df.groupby(['A', 'B'])
# print(grouped.describe())
# print(grouped2.describe())
# print(grouped.count())
# print(grouped['C'].count())
# print(grouped2.count())


# splitting by columns
def get_letter_type(letter):
    # this letter variable holds the name of the columns i.e., A,B,C,D
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'

grouped_by_col = df.groupby(get_letter_type, axis=1)
# print(grouped_by_col.count())


#Aggregate
print(df)
print(grouped.aggregate(np.sum))
#multiple aggregate operations
print(grouped.aggregate([np.sum,np.mean]))
print(grouped.aggregate([np.sum,np.mean])['C'])
print(grouped.aggregate([np.sum,np.mean])['C']['sum'])
print(grouped.aggregate([np.sum,np.mean])['C']['sum'].loc['bar'])

#reset index to default integers
print(grouped.aggregate([np.sum,np.mean]))
print(grouped.aggregate([np.sum,np.mean]).reset_index())

#filter
dff = pd.DataFrame({'A': np.arange(8), 'B': list('aabbbbcc')})

print(dff)
dff = dff.groupby('B').filter(lambda x: len(x)> 3)
print(dff)

# a   [0,
#     1]
# b   [2,
#     3,
#     4,
#     5]
# c   [6,
#     7]

# https://pandas.pydata.org/pandas-docs/stable/groupby.html
# https://pandas.pydata.org/pandas-docs/stable/cookbook.html
