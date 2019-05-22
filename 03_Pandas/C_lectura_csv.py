# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:52:07 2019

@author: pasante_dgip3
"""

import numpy as p
import pandas as pd
import os

#Archivos texto -> JSON, CSV, HTML, XML, ...
#Binary Files ->(asdasdasdasdasdasdasd)
#Relational DataBases
path = 'C:/Users/pasante_dgip3/Documents/GitHub/py-cajas-montufar-daniel-moi/03_Pandas/data/artwork_data.csv'
df = pd.read_csv(
        path,
        nrows=5,
        usecols=['id','artist'], #Para leer estas columnas 
        index_col ='id'
        
        )

columnas_a_usar = ['id','artist','title',
                   'medium','year','acquisitionYear',
                   'height','width','units']

df_completo = pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col='id')

path_guardado = 'C:/Users/pasante_dgip3/Documents/GitHub/py-cajas-montufar-daniel-moi/03_Pandas/data/artwork_data.pickle'

df_completo.to_pickle(path_guardado)
df_completo_pickle = pd.read_pickle(path_guardado)





























