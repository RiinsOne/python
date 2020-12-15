import pandas as pd


read_file = pd.read_excel(r'C:\OG\workspace\venv_projects\excel\users24apr20.xlsx')
read_file.to_csv(r'C:\OG\workspace\venv_projects\excel\users24apr20.csv', index=None, header=True)
