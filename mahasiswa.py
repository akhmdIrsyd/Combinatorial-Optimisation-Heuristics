import pandas as pd
import pyodbc as db
#Create connection string to connect DBTest database with windows authentication
con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=db_final')
cursor = con.cursor()
#daftar mahasiswa
cursor.execute("SELECT distinct mahasiswa,fakultas FROM [db_final].[dbo].[hasil2] group by mahasiswa, fakultas order by fakultas")
rows = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'nama', 1: 'fakultas', 2: 'Jumlah'}, inplace=True)
df
