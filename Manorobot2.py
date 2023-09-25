import numpy as np
import matplotlib.pyplot as plt

# Definir las longitudes de los eslabones
a1 = 2
a2 = 1.5

# Configurar la figura y el eje
fig, ax = plt.subplots()
ax.axis('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

# Definir la función de transformación homogénea
def transformation_matrix(theta, a):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, a * np.cos(theta)],
        [np.sin(theta), np.cos(theta), 0, a * np.sin(theta)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# Animar el manipulador
for angle1 in np.linspace(0, 2*np.pi, 100):
    for angle2 in np.linspace(0, 2*np.pi, 100):
        # Calcular las matrices de transformación con los ángulos actuales
        T1 = transformation_matrix(angle1, a1)
        T2 = transformation_matrix(angle2, a2)
        
        # Calcular la matriz de transformación homogénea total
        T = np.dot(T1, T2)

        # Extraer las posiciones de las articulaciones y del extremo efectuador
        joint1 = T1[:2, 3]
        joint2 = T[:2, 3]
        origin = np.array([0, 0])

        # Actualizar la posición de los eslabones en la gráfica
        ax.plot([origin[0], joint1[0]], [origin[1], joint1[1]], 'r-')
        ax.plot([joint1[0], joint2[0]], [joint1[1], joint2[1]], 'b-')
        plt.draw()
        plt.pause(0.01)
        ax.clear()
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)