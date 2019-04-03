import numpy as np
import matplotlib.pylab as plt
import pandas as pd

datos=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt',sep=";", header = None,names=["a","b","c","d"])
datos2009=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt',sep=";", header = None,names=["a","b","c","d"])
datos2010=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt',sep=";", header = None,names=["a","b","c","d"])

datos["Fechas y hora"]=datos["a"].astype(str).str[:-7]+" "+datos["b"].astype(str).str[-8:]
datos2009["Fechas y hora"]=datos2009["a"].astype(str).str[:-7]+" "+datos2009["b"].astype(str).str[-8:]
datos2010["Fechas y hora"]=datos2010["a"].astype(str).str[:-7]+" "+datos2010["b"].astype(str).str[-8:]
datos

concatenado= pd.concat([datos["Fechas y hora"],datos2009["Fechas y hora"],datos2010["Fechas y hora"]])
concatenado
