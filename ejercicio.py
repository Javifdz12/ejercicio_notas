import pandas as pd
import matplotlib.pyplot as plt

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


def analizar_notas(list):
    list=ordenar_lista(list)
    dataframe1=pd.DataFrame(list,columns=["notas"])
    x=dataframe1["notas"].mean()
    y=dataframe1["notas"].median()
    z=dataframe1["notas"].std()
    rv=dataframe1["notas"].max()-dataframe1["notas"].min()
    cv=(z/x)*100
    q1=dataframe1["notas"].quantile(q=0.25,interpolation="linear")
    q2=dataframe1["notas"].quantile(q=0.5,interpolation="linear")
    q3=dataframe1["notas"].quantile(q=0.75,interpolation="linear")
    dict1={"notas":[list],"media":[x],"mediana":[y],"desviacion_estandar":[z],"rango_variacion":[rv],"coeficiente_variacion":[cv],"q1":[q1],"q2":[q2],"q3":[q3]}
    dataframe2=pd.DataFrame(dict1).transpose()
    print(dataframe2)
    plt.boxplot(x="notas",data=dataframe1)
    plt.show()


analizar_notas(list1)
