# CÓDIGO PARA EJECUTAR EL MODELO 4

import numpy as np
import matplotlib.pyplot as plt
from amplpy import AMPL

# Debemos abrir nuestro archivo en .mod
ampl = AMPL()
ampl.read("modelo4.mod")

# Ingresar datos
datos = np.array([
    [1, 3],
    [2, 4],
    [3, 9],
    [4, 10],
    [5, 11]
])

# Vamos a generar una lista : [P1=1,P2=2,P3=3,P4=4,P5=5]
posicion = list(range(1, len(datos) + 1)) 

# De nuestro conjunto "PUNTOS" del modelo4.mod le vamos asignar la lista anterior
ampl.get_set("PUNTOS").set_values(posicion)
# A partir de un diccionario {1:1, 2:2, 3:3, 4:4, 5:5}, le vamos asignar los PUNTOS
# a la variable x: 
# x[1] = 1, x[2] = 2, ...
ampl.get_parameter("x").set_values(dict(zip(posicion, datos[:, 0])))
# Lo mismo que el paso anterior pero ahora con el diccionario 
#                     {1:3, 2:4, 3:9, 4:10, 5:11}
# se lo asignamos a la variable y:
# y[1] = 3, y[2] = 4, ...
ampl.get_parameter("y").set_values(dict(zip(posicion, datos[:, 1])))
# Resolvemos nuestro modelo4.mod usando el solver HIGHS
ampl.set_option("solver", "highs")
ampl.solve()

# Recuperar los resultados del modelo4.mod
m = ampl.get_variable("m").value()
b = ampl.get_variable("b").value()
error = ampl.get_variable("e").get_values().to_dict()

E = max(error.values())

print("\n--- RESULTADOS ---")
print(f"m: {m:.4f}")
print(f"b: {b:.4f}")
print(f"y = {m:.4f}x + {b:.4f}")
print(f"E: {E:.4f}")

'''
    Gráfica del ajuste de la recta (estilo modelo 4)
'''

x = datos[:, 0]  # x = [1,2,3,4,5]
y = datos[:, 1]  # y = [3,4,9,10,11]

# Genera 200 valores distribuidos uniformemente entre 0.5 y 5.5
x_line = np.linspace(x.min() - 0.5, x.max() + 0.5, 200)
# Aplicarlo a la ecuación de la recta con valores de x_line
y_line = m * x_line + b

fig, ax = plt.subplots(figsize=(9, 6))

# Recta ajustada
ax.plot(x_line, y_line, color='red', linewidth=2.5,
        label=f'y = {m:.2f}x + {b:.2f}')

# Puntos originales
ax.scatter(x, y, color='blue', s=120, zorder=5,
           edgecolors='black', linewidth=1.2, label='Puntos')

# Candidatos a puntos con error máximo
candidatos = [i for i, e in error.items() if abs(e - E) < 1e-6]

# Elegir el candidato que tenga error positivo
candidatos_pos = [i for i in candidatos if (m * x[i-1] + b - y[i-1]) > 0]

# Elegir el primero positivo, sino el primero de todos
if candidatos_pos:
    i_critico = candidatos_pos[0]
else:
    i_critico = candidatos[0]

# Posición del error máximo
xi = x[i_critico - 1]
yi = y[i_critico - 1]
yi_recta = m * xi + b

# Resaltar el error máximo con un círculo
ax.scatter([xi], [yi], s=400, facecolors='none',
           edgecolors='#8B0000', linewidth=3.5, zorder=6)

# Línea punteada del error máximo (en rojo)
ax.plot([xi, xi], [yi_recta, yi], color='#8B0000',
        linestyle=(0, (4, 3)), linewidth=2.2, zorder=2)

# Punto medio de la línea punteada
y_medio = (yi + yi_recta) / 2

# Marcar el error máximo
ax.annotate(f'E = {E:.3f}',
            xy=(xi, y_medio),
            xytext=(xi + 0.45, y_medio),
            fontsize=13,
            color='white',
            fontweight='bold',
            va='center',
            ha='left',
            bbox=dict(boxstyle='round,pad=0.5',
                      facecolor='#8B0000',
                      edgecolor='#5C0000',
                      linewidth=1.5,
                      alpha=1.0),
            arrowprops=dict(arrowstyle='-|>',
                            color='#8B0000',
                            linewidth=2.5,
                            shrinkA=0,
                            shrinkB=8,
                            mutation_scale=20))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Ajuste de recta por modelo 4')

ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('grafica_mod4.png', dpi=300, bbox_inches='tight')
print("Imagen guardada exitosamente como 'grafica_mod4.png'")