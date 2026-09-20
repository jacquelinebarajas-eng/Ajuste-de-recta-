import numpy as np
import matplotlib.pyplot as plt

# Ingresamos los datos 
datos = np.array([
    [1,3],
    [2,4],
    [3,9],
    [4,10],
    [5,11]
])

x = datos[:, 0]  # Solo nos interesa el primer elemento 
y = datos[:, 1]  # Solo nos interesa el segundo elemento

# --- Mínimos cuadrados (recta y = mx + b) ---
n = len(x)   # tamaño de x
sum_x  = np.sum(x)   
sum_y  = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x ** 2)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

# Predicción
y_pred = m * x + b

# Error por cada punto
error = np.abs(y - y_pred  ) ** 2     
i_max = np.argmax(error)  # índice del error máximo

print(f"\nEcuación ajustada: y = {m:.4f}x + {b:.4f}")

fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(x, y, color='blue', s=100, zorder=3, label='Puntos')

# Línea de ajuste
x_line = np.linspace(x.min() - 0.5, x.max() + 0.5, 100)
y_line = m * x_line + b
ax.plot(x_line, y_line, color='red', linewidth=2,
        label=f'y = {m:.2f}x + {b:.2f}')

# Etiquetar cada punto y su error
for i in range(n):
    color = '#8B0000' if i == i_max else 'gray'
    ax.plot([x[i], x[i]], [y_pred[i], y[i]], color=color,
            linestyle='--', linewidth=1.5, zorder=2)
    ax.annotate(f'P{i+1}\ne = {error[i]:.2f}', (x[i], y[i]),
                textcoords="offset points", xytext=(8, 5), fontsize=9)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Mínimos Cuadrados')
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('prueba.png', dpi=300, bbox_inches='tight')
print("Imagen guardada exitosamente como 'grafica_min.png'")