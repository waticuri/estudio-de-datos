from db import Datebase, Graficar

if __name__ == '__main__':
    datebase = Datebase(user="pi",password="waticuri",database="mydb")
    df = datebase.dataframe()
    x = df["tiempo"]
    y = df["luz"]
    grafica = Graficar(x,y)
    grafica.linia()
    datebase.save(df, "./csv/example.csv")
    datebase.exit()
