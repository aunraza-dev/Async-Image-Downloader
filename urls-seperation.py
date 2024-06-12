import pandas as pd

df = pd.read_csv('tools.csv')

urls = df['Img']

with open('urls-seperated.txt', 'w') as f:
    for url in urls:
        f.write(url + '\n')