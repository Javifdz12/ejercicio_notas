import pandas as pd
import numpy
import seaborn as sns

def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        derecha = lista[i]
        for j in range(i - 1, -1, -1):
            izquierda = lista[j]
            if derecha < izquierda:
                lista[j + 1] = izquierda
                lista[j] = derecha
                derecha = lista[j]
    return lista

list1=[3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]


def analizar(list):
    list=ordenar_lista(list)
    dataframe=pd.DataFrame(list1,columns=["notas"])
    x=dataframe["notas"].mean()
    print(f"la media es {x}")
    y=dataframe["notas"].median()
    print(f"la mediana es {y}")
    z=dataframe["notas"].std()
    print(f"la desviacion estandar es {z}")
    rv=dataframe["notas"].max()-dataframe["notas"].min()
    print(f"el rango de variacion es {rv}")
    cv=(z/x)*100
    print(f"el coeficiente de variacion es {cv} %")
    q1=dataframe["notas"].quantile(q=0.25,interpolation="linear")
    print(f"el primer cuantil(25%) es {q1}")
    q2=dataframe["notas"].quantile(q=0.5,interpolation="linear")
    print(f"el primer cuantil(50%) es {q2}")
    q3=dataframe["notas"].quantile(q=0.75,interpolation="linear")
    print(f"el primer cuantil(75%) es {q3}")
    grafica1=sns.histplot(x="notas",data=dataframe)
    print(grafica1)
    grafica2=sns.boxplot(x="notas",data=dataframe)
    print(grafica2)


analizar(list1)
