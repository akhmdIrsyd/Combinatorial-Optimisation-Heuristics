import pandas as pd
import pyodbc as db
#Create connection string to connect DBTest database with windows authentication
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=db_final')
cursor = con.cursor()

cursor.execute("SELECT TOP (10)fakultas, dosen, count(dosen) FROM [db_final].[dbo].[hasil1] group by fakultas, dosen order by count(dosen) desc")
rows = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Fakultas', 1: 'nama', 2: 'matakuliah',3: 'dosen', 4: 'Tahun', 5: 'jumlah'}, inplace=True)
x = df['nama']
y = df['matakuliah']

plt.barh(x, y)
plt.show()
df