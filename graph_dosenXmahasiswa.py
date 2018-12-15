import pandas as pd
import pyodbc as db
#Create connection string to connect DBTest database with windows authentication
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=db_final')
cursor = con.cursor()

cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'Fakultas Teknologi Industri (FTI)' group by fakultas, tahun order by fakultas ")
rows1 = cursor.fetchall()
cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)' group by fakultas, tahun order by fakultas ")
rows2 = cursor.fetchall()
cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)' group by fakultas, tahun order by fakultas ")
rows3 = cursor.fetchall()
cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'Fakultas Ilmu Alam (FIA)' group by fakultas, tahun order by fakultas ")
rows4 = cursor.fetchall()
cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'Fakultas Teknologi Kelautan (FTK)' group by fakultas, tahun order by fakultas ")
rows5 = cursor.fetchall()
cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'UPMB' group by fakultas, tahun order by fakultas ")
rows6 = cursor.fetchall()
cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'Sistem Pembelajaran Daring (SPADA) Indonesia' group by fakultas, tahun order by fakultas ")
rows7 = cursor.fetchall()
cursor.execute("SELECT distinct fakultas, count(dosen),sum(jumlah),tahun FROM [db_final].[dbo].[hasil1] WHERE fakultas = 'UPT Penyelenggara Mata Kuliah Sosial Humaniora' group by fakultas, tahun order by fakultas ")
rows8 = cursor.fetchall()
df = pd.DataFrame([[ij for ij in i] for i in rows1], columns=['Fakultas', 'Jumlah', 'mahasiswa', 'Tahun'])
df2 = pd.DataFrame([[ij for ij in i] for i in rows2], columns=['Fakultas', 'Jumlah', 'mahasiswa', 'Tahun'])
df3 = pd.DataFrame([[ij for ij in i] for i in rows3], columns=['Fakultas', 'Jumlah',  'mahasiswa','Tahun'])
df4 = pd.DataFrame([[ij for ij in i] for i in rows3], columns=['Fakultas', 'Jumlah',  'mahasiswa','Tahun'])
df5 = pd.DataFrame([[ij for ij in i] for i in rows3], columns=['Fakultas', 'Jumlah',  'mahasiswa','Tahun'])
df6 = pd.DataFrame([[ij for ij in i] for i in rows3], columns=['Fakultas', 'Jumlah',  'mahasiswa','Tahun'])
df7 = pd.DataFrame([[ij for ij in i] for i in rows3], columns=['Fakultas', 'Jumlah',  'mahasiswa','Tahun'])
df8 = pd.DataFrame([[ij for ij in i] for i in rows3], columns=['Fakultas', 'Jumlah',  'mahasiswa','Tahun'])
x = df['mahasiswa']
y = df['Jumlah']
x2 = df2['mahasiswa']
y2 = df2['Jumlah']
x3 = df3['mahasiswa']
y3 = df3['Jumlah']
x4 = df4['mahasiswa']
y4 = df4['Jumlah']
x5 = df5['mahasiswa']
y5 = df5['Jumlah']
x6 = df6['mahasiswa']
y6 = df6['Jumlah']
x7 = df7['mahasiswa']
y7 = df7['Jumlah']
x8 = df8['mahasiswa']
y8 = df8['Jumlah']
area = (df['Jumlah'])  # 0 to 15 point radii
plt.scatter(x, y,s=area, alpha=0.5,  c='blue', label='(FTI)')
plt.scatter(x2, y2,s=area, alpha=0.5,   c='red', label='(FTIK)')
plt.scatter(x3, y3, s=area, alpha=0.5,  c='black', label='(FTSLK)')

#plt.scatter(x4, y4, s=area, alpha=0.5,  c='green', label='(FIA)')
#plt.scatter(x5, y5, s=area, alpha=0.5,  c='yellow', label='(FTK)')
#plt.scatter(x6, y6, s=area, alpha=0.5,  c='green', label='UPMB')
#plt.scatter(x7, y7, s=area, alpha=0.5,  c='brown', label='(SPADA)')
#plt.scatter(x8, y8, s=area, alpha=0.5,  c='purple', label='(UPT)')
plt.legend(framealpha=1, frameon=True)
plt.show()
