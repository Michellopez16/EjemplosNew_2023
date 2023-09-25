import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, cos, sin, pi, atan2, sqrt
from sympy.matrices import Matrix

# Definir las variables simbólicas
theta1, theta2 = symbols('theta1 theta2')
a1, a2 = symbols('a1 a2')

# Matriz de transformación homogénea para la primera articulación
T1 = Matrix([[cos(theta1), -sin(theta1), 0, a1*cos(theta1)],
             [sin(theta1), cos(theta1), 0, a1*sin(theta1)],
             [0, 0, 1, 0],
             [0, 0, 0, 1]])

# Matriz de transformación homogénea para la segunda articulación
T2 = Matrix([[cos(theta2), -sin(theta2), 0, a2*cos(theta2)],
             [sin(theta2), cos(theta2), 0, a2*sin(theta2)],
             [0, 0, 1, 0],
             [0, 0, 0, 1]])

# Calcular la matriz de transformación homogénea total
T = T1 * T2

# Definir las longitudes de los eslabones
link_lengths = {a1: 2, a2: 1.5}

# Configurar la figura y el eje
fig, ax = plt.subplots()
ax.axis('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

# Animar el manipulador
for angle1 in np.linspace(0, 2*np.pi, 100):
    for angle2 in np.linspace(0, 2*np.pi, 100):
        # Evaluar las matrices de transformación con los ángulos actuales
        T1_eval = T1.subs({theta1: angle1, **link_lengths})
        T2_eval = T2.subs({theta2: angle2, **link_lengths})
        T_eval = T.subs({theta1: angle1, theta2: angle2, **link_lengths})

        # Extraer las posiciones de las articulaciones y del extremo efectuador
        joint1 = [T1_eval[0, 3], T1_eval[1, 3]]
        joint2 = [T_eval[0, 3], T_eval[1, 3]]
        origin = [0, 0]

        # Actualizar la posición de los eslabones en la gráfica
        ax.plot([origin[0], joint1[0]], [origin[1], joint1[1]], 'r-')
        ax.plot([joint1[0], joint2[0]], [joint1[1], joint2[1]], 'b-')
        plt.draw()
        plt.pause(0.01)
        ax.clear()
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)