import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://PostgresSQL14:Sanjeeb@9006/localhost:5432/Database-automation")

with pd.ExcelFile('Dataset.xlsx') as xls:
    df = pd.read_excel(xls)
    df.to_sql(name='automation', con=engine, if_exists='append', index=False)
