# Importar librerías.
import numpy as np
from scipy import stats
import joblib

# Calcular el promedio.
def calcular_promedio(datos):
    return np.mean(datos)

# Calcular la correlación.
def calcular_correlacion(datos1, datos2):
    correlacion, valor_p = stats.pearsonr(datos1, datos2)
    return correlacion

# Guardar los resultados.
def guardar_resultados(resultados):
    joblib.dump(resultados, "resultados.joblib")