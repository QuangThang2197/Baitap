import pandas as pd
x=pd.read_csv('Thang.csv')
print(x.head(10))
y=pd.read_csv('https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-September-2020-quarter/Download-data/business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv')
print(y.head(10))
z=pd.read_json('https://data.cese.nsw.gov.au/data/dataset/027493b2-33ad-3f5b-8ed9-37cdca2b8650/resource/af20d17c-a7ac-4251-af75-e5ae66573e92/download/collections.json')
print(z.head(10))