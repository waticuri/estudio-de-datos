import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Datebase:
    def __init__(self, user, password, database, host="localhost"):
        self.conexion = mysql.connector.connect(host=host,user=user,passwd=password, database=database)

    def extraer(self):
        db = []
        cursor = self.conexion.cursor()
        cursor.execute("select * from lecturas where id = (select max(id) from lecturas)")
        for i in cursor:
            db.append(i)
        return db
    def dataframe(self):
        temp = []
        humA = []
        hum = []
        luz = []
        tiempo= []
        cursor = self.conexion.cursor()
        cursor.execute("select temperatura from lecturas")
        for i in cursor:
            temp.append(i[0])
        cursor.execute("select humedad_ambiente from lecturas")
        for i in cursor:
            humA.append(i[0])
        cursor.execute("select humedad from lecturas")
        for i in cursor:
            hum.append([0])
        cursor.execute("select luz from lecturas")
        for i in cursor:
            luz.append(i[0])
        cursor.execute("select updatedAt from lecturas")
        for i in cursor:
            tiempo.append(i[0])
        dataframe = {
            "temp":temp,
            "humA":humA,
            "hum":hum,
            "luz":luz,
            "tiempo":tiempo,
            }
        df = pd.DataFrame(dataframe)
        return df
    
    def save(self, archivo, path):
        try:
            archivo.to_csv(path)
        finally:
            print("No se ha podido guardar, porfavor revise si la ruta es correcta")

    def exit(self):
        self.conexion.commit()
        self.conexion.close() 
        
class Graficar:
    def __init__(self, x, y):
        '''Indique la variable X y Y de la grafica'''
        self.x = x
        self.y = y
        
    def linia(self):
        plt.plot(self.x, self.y)
        plt.show()
        
    def dispersion(self):
        plt.scatter(self.x, self.y)
        plt.show()       
