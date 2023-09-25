import pygame
import numpy as np

# Inicializar Pygame
pygame.init()

# Configurar la ventana de visualización
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Kalman Filter Mouse Estimation')

# Configuración del Filtro de Kalman
dt = 1  # Tiempo de muestreo
A = np.array([[1, 0, dt, 0],
              [0, 1, 0, dt],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0]])  # Matriz de medición
Q = 0.1 * np.eye(4)  # Covarianza del ruido del proceso
R = 500 * np.eye(2)  # Covarianza del ruido de medición
x = np.zeros((4, 1))  # Estado inicial
P = 1000 * np.eye(4)  # Covarianza inicial del estado

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Obtener la posición real del mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    z = np.array([[mouse_x], [mouse_y]])  # Medición
    
    # Filtro de Kalman: Predicción
    x = np.dot(A, x)
    P = np.dot(np.dot(A, P), A.T) + Q
    
    # Filtro de Kalman: Corrección (Actualización)
    S = np.dot(np.dot(H, P), H.T) + R
    K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
    y = z - np.dot(H, x)
    x = x + np.dot(K, y)
    P = P - np.dot(np.dot(K, H), P)
    
    # Dibujar
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (int(mouse_x), int(mouse_y)), 10)  # Posición real del mouse
    pygame.draw.circle(screen, (255, 0, 0), (int(x[0]), int(x[1])), 10)  # Estimación del Filtro de Kalman
    pygame.display.flip()
    
    pygame.time.delay(10)

pygame.quit()