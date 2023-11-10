import pandas as pd

# Ruta del archivo .dat
archivo_dat = "C:\python\scraping\prueba2\SADC_2021_National.dat"

with open (archivo_dat,"r") as archivo:
    for linea in archivo:
        print(linea)
        for i,l in enumerate(linea):
            print(f"{i}     {l}")
        break
print(archivo.closed)
