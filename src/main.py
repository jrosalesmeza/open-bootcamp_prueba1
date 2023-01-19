import pandas as pd

file_path = 'app/files/example.xls'

df = pd.read_excel(file_path)

print('Emails únicos: ', df['email'].drop_duplicates().to_list())
