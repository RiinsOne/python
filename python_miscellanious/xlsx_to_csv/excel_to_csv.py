import pandas as pd


read_file = pd.read_excel(r'M:\Programs\workspace\venv_projects\xlsx_to_csv\users01jun20.xlsx')
read_file.to_csv(r'M:\Programs\workspace\venv_projects\xlsx_to_csv\users01jun20.csv', index=None, header=True)
