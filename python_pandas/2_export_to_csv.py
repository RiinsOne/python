import pandas as pd

# https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03

df = pd.DataFrame(columns=['first_name', 'last_name'])
print(df)

df = df.append({'first_name': 'Og', 'last_name': 'Riins'}, ignore_index=True)
df = df.append({'first_name': 'Bielke', 'last_name': 'Assemblage'}, ignore_index=True)
df = df.append({'first_name': 'Black', 'last_name': 'Warrior'}, ignore_index=True)
print(df)

# easiest way
# df.to_csv('easy_to_csv.csv')

# without index
# df.to_csv('easy_to_csv.csv', index=False)

# with encoding
df.to_csv('easy_to_csv.csv', index=False, encoding='utf-8')

# with a custom delimiter
df.to_csv('easy_to_csv.csv', index=False, encoding='utf-8', sep='\t')
