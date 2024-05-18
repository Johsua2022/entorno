import pandas as pd
# importar archivo csv
df=pd.read_csv("Activity.csv")
print(df)
df.info()
print(df.head(15))
print(df.tail(20))

# imprimir info de columnas específicas
print(df['Logged_Activities_Distance'])



# acceder a numero especifico de datos(segmentos de datos)

print(df['Very_Active_Distance'][500:510])



# accede a un dato especifico en una columna
print(df['Very_Active_Distance'][500])

# loc, iloc

# UserID     ,Date      ,Total_Distance, de los indices desde 100 al 120

print(df.loc[100:120,['UserID','Date','Total_Distance']])

print(df.iloc[100:120,[0,1,2]])

print(df.iloc[100:120,0:3])

# filtrar los que se realizaron actividad fisica el 6 de abril de 2016

print(df.loc[df['Date'] == '5/5/2016'])

print(df.loc[df['Date'] == '5/5/2016', 'Total_Distance'])

print(df.loc[df['Date'] == '5/5/2016', 'Total_Distance'].sum())


# sumar cuantos realizaron actividad fisica entre primero de enero al 18 de mayo de 2016
