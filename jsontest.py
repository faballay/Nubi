# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:40:59 2020

@author: Federico
"""

import pandas as pd
import json
from datetime import date


fecha_proceso = date.today()
input_file = 'MPE1004_0000000000.json'


#Lectura de datos
with open(input_file) as f:
  data = json.load(f)
f.close()
  

#Normalizacion de los resultados en un dataframe 
from pandas.io.json import json_normalize

df  = json_normalize(data['results'])


#Validacion de integridad

if df.shape[0] == data['paging']['primary_results']:
    print("La cantidad de filas es correcta")
else:
    print("El archivo generado contiene {} registros faltantes".format(str(data['paging']['primary_results']-df.shape[0])))

#Escritura de archivo 
    
from pathlib import Path

output_file = 'json_aplanado.csv'
output_dir = Path(data['site_id']+'/'+str(fecha_proceso.month)+'/'+str(fecha_proceso.year)+'/'+str(fecha_proceso.day))

output_dir.mkdir(parents=True, exist_ok=True)

df.to_csv(output_dir/output_file)
