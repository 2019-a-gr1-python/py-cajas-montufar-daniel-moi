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
serie.ciudades = pd.Series(lista_ciudades,
                           index=["4","5","1",
                                  "17"])





























