import pandas as pd
import pyodbc as db
#Create connection string to connect DBTest database with windows authentication
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=db_final')
cursor = con.cursor()

cursor.execute("SELECT fakultas, count(dosen),tahun FROM [db_final].[dbo].[hasil1] where fakultas= 'Fakultas Teknologi Industri (FTI)' group by fakultas,tahun order by tahun desc")
rows1 = cursor.fetchall()
cursor.execute("SELECT fakultas, count(dosen),tahun FROM [db_final].[dbo].[hasil1] where fakultas= 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)' group by fakultas,tahun order by tahun desc")
rows2 = cursor.fetchall()
cursor.execute("SELECT fakultas, count(dosen),tahun FROM [db_final].[dbo].[hasil1] where fakultas= 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)' group by fakultas,tahun order by tahun desc")
rows3 = cursor.fetchall()
df = pd.DataFrame([[ij for ij in i] for i in rows1], columns=['Fakultas', 'Jumlah', 'Tahun'])
df2 = pd.DataFrame([[ij for ij in i] for i in rows2], columns=['Fakultas', 'Jumlah', 'Tahun'])
df3 = pd.DataFrame([[ij for ij in i] for i in rows3], columns=['Fakultas', 'Jumlah', 'Tahun'])

x = df['Tahun']
y = df['Jumlah']
x2 = df2['Tahun']
y2 = df2['Jumlah']
x3 = df3['Tahun']
y3 = df3['Jumlah']

plt.plot(x, y,  c='blue', label='Fakultas Teknologi Industri (FTI)')
plt.plot(x2, y2,  c='red', label='Fakultas Teknologi Informasi dan Komunikasi (FTIK)')
plt.plot(x3, y3,  c='black', label='Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)')
plt.legend(framealpha=1, frameon=True)
plt.show()