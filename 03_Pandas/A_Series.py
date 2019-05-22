# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:13:40 2019

@author: pasante_dgip3
"""

print("Hola")
nombre = "Daniel"
edad = 26 

import numpy as np
import pandas as pd

lista_numeros =[1,2,3,4]
tupla_numeros =(1,2,3,4)
np_numeros = np.array((1,2,3,4))
numeros_series_a = pd.Series(lista_numeros)
numeros_series_b = pd.Series(tupla_numeros)
numeros_series_c = pd.Series(np_numeros)
numeros_series_d = pd.Series([
        True,
        False,
        12,
        12.21,
        "Asad",
        None,
        (),
        [],
        {"nombre":"Daniel"}])

numeros_series_a[0]

lista_ciudades = ["Ambato","Cuenca","Loja",
                  "Quito"]
serie_ciudades = pd.Series(lista_ciudades,
                           index=["A","C","L",
                                  "Q"])

serie_ciudades["Q"]
serie_ciudades[0]
serie_ciudades[1]
serie_ciudades[2]
serie_ciudades[3]

print(type(serie_ciudades))

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }
serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[0]

ciudades_menores_5000 = serie_valor_ciudad < 5000

serie_menor_5000 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"]= 8750

print("Lima" in serie_valor_ciudad)# False
print("Loja" in serie_valor_ciudad)# True

np.square(serie_valor_ciudad)
np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
            "Quito":1500,
            "Loja":4000
        })

ciudades_dos = pd.Series({
            "Montañita":300,
            "Guayaquil":10000,
            "Quito":2000
        })

print(ciudades_uno * ciudades_dos)

randomico = np.random.rand(3)
series_tres_rand = pd.Series(randomico)

ciudades_uno.index

# Concatenar series
#Añadir un índice valor a una serie
#Maximo
#Minimo
#Estadísticas(Avg,Mean...)




























