# ------------------------------------------------
# Problema de optimización : Ajuste de recta por modelo 4
# Varibles de decisión: 
#     m : pendiente de la recta
#     b : ordenada al origen 
#     e_i : valor del error del punto i
#     E : valor del error máximo entre todos los puntos
# NOTA : m y b deben ser números reales, y e_i debe ser un número real 
# positivo.
# ------------------------------------------------

set PUNTOS;    # índice de los puntos i = 1,...,n

param x {PUNTOS};   # x_i
param y {PUNTOS};   # y_i

# ------------------------------------------------
# Variables de decisión
# ------------------------------------------------
var m;                    # m,b están en R (o son libres)   
var b;                       
var e {PUNTOS} >= 0; 
var E >=0;  # min{max e_i}
# ------------------------------------------------
# Función objetivo
# ------------------------------------------------
minimize Error: E;

# ------------------------------------------------
# Restricciones
# ------------------------------------------------
subject to Cota_Sup {i in PUNTOS}:  m * x[i] + b - y[i] <= e[i];
subject to Cota_Inf {i in PUNTOS}:  m * x[i] + b - y[i] >= -e[i];
subject to Max_Error {i in PUNTOS}: E >= e[i];