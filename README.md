# Nubi

Desafío 3: Data Engineer Jr.

Nos interesa que puedas hacer lo siguiente:
Ingreses al link de la carpeta: inputEjemplos
Deserializá el alguno de los archivos. Nuestro preferido es: MPE1004_0000000000.json.gz
Lee la información en un DataFrame.
Guardá la información deserializada en un archivo CSV con el siguiente patrón:
Sitio/Mes/Año/dia/(archivo).csv. Por Ejemplo MPE/2020/08/28/[NoNosImporta].csv
Bonus: Usar Spark Scala + IntelliJ - También puede ser Pyspark + Pycharm


Solución Propuesta al desafío 

La solución se compone de un script en lenguaje python, utilicé Spyder como IDE y las librerías: Pandas, Json, Date y Path. 

El script comienza importando librerías y asignando valor a los parametros de input file y fecha proceso. 
Abro el json y lo leo en una variable llamada data. 
Utilizo la funcion json_normalize para aplanar el json. Link a la documentacion: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html
Una vez generado el dataframe normalizado, realizo una pequeña validación de cantidad de registros y mostrando un mensaje de datos ok o datos faltantes.
Genero dinamicamente la ruta donde se guarda el archivo usando las variables fecha_proceso y site_id. 
Escribo el dataframe en un csv. 
