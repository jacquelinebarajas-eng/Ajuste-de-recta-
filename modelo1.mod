# ------------------------------------------------
# Problema de optimización : Ajuste de recta por modelo 1
# Varibles de decisión: 
#     m : pendiente de la recta
#     b : ordenada al origen 
#     e : valor del error
# NOTA : m y b deben ser números reales, y e debe ser un número real positivo.
# ------------------------------------------------

set PUNTOS;    # índice de los puntos i = 1,...,n

param x {PUNTOS};   # x_i
param y {PUNTOS};   # y_i

# ------------------------------------------------
# Variables de decisión
# ------------------------------------------------
var m;                    # m,b están en R (o son libres)   
var b;                       
var e >= 0; 

# ------------------------------------------------
# Función objetivo
# ------------------------------------------------
minimize Error: e;

# ------------------------------------------------
# Restricciones
# ------------------------------------------------
subject to Cota_Sup {i in PUNTOS}:  m * x[i] + b - y[i] <= e;
subject to Cota_Inf {i in PUNTOS}:  m * x[i] + b - y[i] >= -e;
