from db import Datebase
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

database = Datebase(user="pi",password="waticuri",database="mydb")
db = database.dataframe()

df = pd.DataFrame(db)
y = df["luz"]
x = df["tiempo"]

plt.plot(x,y)
plt.show()
