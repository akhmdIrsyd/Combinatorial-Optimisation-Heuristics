import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
#Create connection string to connect DBTest database with windows authentication
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=db_final')
cursor = con.cursor()

cursor.execute("SELECT distinct [Fakultas], YEAR(tanggal), COUNT(mahasiswa) FROM [db_final].[dbo].[MHS]  GROUP BY [Fakultas],YEAR(tanggal) ORDER BY COUNT(mahasiswa) DESC")
rows = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Fakultas', 1: 'Tahun', 2: 'Jumlah'}, inplace=True)


y = df['Jumlah']
x = df['Fakultas']

plt.barh(x, y)
plt.show()

df