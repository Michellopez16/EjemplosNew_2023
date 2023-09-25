import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Definir el ángulo de la articulación como una variable simbólica
theta = sp.symbols('theta')

# Definir la longitud del eslabón
l = 1  # Puedes cambiar esto a cualquier valor positivo

# Definir las coordenadas del punto objetivo
x_target = 2
y_target = 2

# Calcular las coordenadas del extremo del manipulador
x_end = l * sp.cos(theta)
y_end = l * sp.sin(theta)

# Definir la función de costo como la distancia cuadrada entre el extremo del manipulador y el punto objetivo
cost_function = (x_end - x_target)**2 + (y_end - y_target)**2

# Encontrar el valor de theta que minimiza la función de costo
optimal_theta_solution = sp.solve(sp.diff(cost_function, theta), theta)

# Evaluar la solución y convertirla a un valor numérico (float)
optimal_theta = float(optimal_theta_solution[0].evalf())

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-l-1, l+3)
ax.set_ylim(-l-1, l+3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)

# Graficar el punto objetivo
ax.plot(x_target, y_target, 'ro')

# Inicializar la línea que representará el manipulador
line, = ax.plot([], [], 'b-')

# Función de inicialización para la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización para la animación
def update(frame):
    angle = frame * optimal_theta / 30  # Dividir el ángulo óptimo en 30 pasos
    x = l * np.cos(angle)
    y = l * np.sin(angle)
    line.set_data([0, x], [0, y])
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=31, init_func=init, blit=True)

plt.show()