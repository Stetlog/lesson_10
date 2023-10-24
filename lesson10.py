import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data['robot'] = data['whoAmI'].apply(lambda x: '1' if x == 'robot' else '0')
data['human'] = data['whoAmI'].apply(lambda x: '1' if x == 'human' else '0')
del data['whoAmI']
print(data)



# # data.loc[data['whoAmI'] == 'robot', 'one_hot_1'] = str('0')
# # data.loc[data['whoAmI'] == 'human', 'one_hot_1'] = str('1')
# pivoted = pd.pivot(data, index = range(10), columns=['whoAmI'], values=['one_hot'])
# print(pivoted.head)