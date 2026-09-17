# CÓDIGO PARA EJECUTAR EL MODELO 3

import numpy as np
import matplotlib.pyplot as plt
from amplpy import AMPL

ampl = AMPL()  # Inicializar AMPL

ampl.read("modelo3.mod")  #Leer el modelo 3 desde .mod

datos = np.array([   #Datos
    [1,3],
    [2,4],
    [3,9],
    [4,10],
    [5,11]
])

posicion = list(range(1, len(datos) + 1))    # Índices de los puntos

# Pasar los datos de Python a AMPL
ampl.get_set("PUNTOS").set_values(posicion)
ampl.get_parameter("x").set_values(dict(zip(posicion, datos[:, 0])))
ampl.get_parameter("y").set_values(dict(zip(posicion, datos[:, 1])))

ampl.set_option("solver", "highs")  # Solver para problemas de optimizacion
ampl.solve()

# Recuperar resultados
m = ampl.get_variable("m").value()
b = ampl.get_variable("b").value()
error = ampl.get_variable("e").get_values().to_dict()

print("\n--- RESULTADOS ---")
print(f"m: {m:.4f}")
print(f"b: {b:.4f}")
print(f"y = {m:.4f}x + {b:.4f}")

print("\n--- Errores y su suma ---")
for i in posicion:
    print(f"P{i}: e[{i}] = {error[i]:.4f}")

print(f"\nSuma de errores: {sum(error.values()):.4f}")

'''
    Gráfica del ajuste de la recta
'''

x = datos[:, 0]
y = datos[:, 1]

# Generar 200 valores de x distribuidos uniformemente
x_line = np.linspace(x.min() - 0.5, x.max() + 0.5, 200)
y_line = m * x_line + b

fig, ax = plt.subplots(figsize=(9, 6))

# Recta ajustada
ax.plot(x_line, y_line, color='red', linewidth=2,
        label=f'y = {m:.2f}x + {b:.2f}')

# Puntos originales
ax.scatter(x, y, color='blue', s=100, zorder=5,
           edgecolors='black', label='Puntos')


# Líneas verticales que muestran el error de cada punto 
for i, (xi, yi) in enumerate(zip(x, y), start=1):
    yi_recta = m * xi + b
    error_i = error[i] 
    ax.plot([xi, xi], [yi_recta, yi], color='gray',
            linestyle=':', linewidth=1.2, zorder=1)
    
    # Punto medio de la línea punteada (donde va la etiqueta)
    y_medio = (yi + yi_recta) / 2

    # Desplazamiento horizontal para que no choque con la línea
    offset_x = 0.08

    ax.annotate(f'e{i} = {error_i:.3f}',
                xy=(xi, y_medio),
                xytext=(xi + offset_x, y_medio),
                fontsize=9,
                color='darkred',
                fontweight='bold',
                va='center',
                ha='left',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='lightyellow',
                          edgecolor='orange',
                          alpha=0.9))

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.set_title('Ajuste de recta por modelo 3')

ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig('grafica_mod3.png', dpi=300, bbox_inches='tight')
print("Imagen guardada exitosamente como 'grafica_mod3.png'")