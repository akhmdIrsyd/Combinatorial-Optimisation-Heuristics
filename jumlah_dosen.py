import pandas as pd
import pyodbc as db
#Create connection string to connect DBTest database with windows authentication
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=db_final')
cursor = con.cursor()

cursor.execute("SELECT fakultas,count(jurusan) FROM [db_final].[dbo].[hasil4] group by fakultas order by count(jurusan) desc")
rows = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Fakultas', 1: 'Jumlah'}, inplace=True)
y = df['Jumlah']
x = df['Fakultas']

plt.barh(x, y)
plt.show()
df