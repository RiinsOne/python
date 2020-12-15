import os
import pandas as pd


df = pd.read_csv('columns_of_hard_way_to_save_csv_file.csv')

df = df.append({'first_name': 'Og', 'last_name': 'Riins'}, ignore_index=True)
df = df.append({'first_name': 'Bielke', 'last_name': 'Assemblage'}, ignore_index=True)
print(df)

if os.path.isfile('hard_way_to_save_csv_file.csv'):
    os.remove('hard_way_to_save_csv_file.csv')

with open('hard_way_to_save_csv_file.csv', 'a', encoding='utf-8') as f:
    columns_length = len(df.columns)

    for col in range(columns_length):
        if col == columns_length - 1:
            f.write('{}\n'.format(df.columns[col]))
            break
        f.write('{},'.format(df.columns[col]))

    # for c in range(len(df.columns)):
        # if c != len(df.columns) - 1:
        #     f.write('{},'.format(df.columns[c]))
        # else:
        #     f.write('{}\n'.format(df.columns[c]))

    for i in range(0, len(df.index)):
        fn = df.loc[i, 'first_name']
        ln = df.loc[i, 'last_name']
        f.write(f'{fn},{ln}' + '\n')
