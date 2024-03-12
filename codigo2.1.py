import math
import numpy as np  # Importar NumPy para la multiplicación de matrices

def matriz_rotacion(theta_x, theta_y, theta_z, orden="ZYX"):
  """
  Calcula la matriz de rotación para un brazo robótico.

  Args:
    theta_x: Ángulo de rotación alrededor del eje X (en grados).
    theta_y: Ángulo de rotación alrededor del eje Y (en grados).
    theta_z: Ángulo de rotación alrededor del eje Z (en grados).
    orden: Orden de las rotaciones (ZYX, ZXY, etc.).

  Returns:
    Matriz de rotación de 3x3 como un array de NumPy.
  """

  # Convertir ángulos a radianes
  theta_x = math.radians(theta_x)
  theta_y = math.radians(theta_y)
  theta_z = math.radians(theta_z)

  # Diccionario con las matrices de rotación individuales
  rotaciones = {
      "X": np.array([[1, 0, 0], [0, math.cos(theta_x), -math.sin(theta_x)], [0, math.sin(theta_x), math.cos(theta_x)]]),
      "Y": np.array([[math.cos(theta_y), 0, math.sin(theta_y)], [0, 1, 0], [-math.sin(theta_y), 0, math.cos(theta_y)]]),
      "Z": np.array([[math.cos(theta_z), -math.sin(theta_z), 0], [math.sin(theta_z), math.cos(theta_z), 0], [0, 0, 1]]),
  }

  # Calcular la matriz de rotación final
  R = np.eye(3)  # Matriz identidad
  for eje in orden:
    R = R @ rotaciones[eje]

  return R

# Ejemplo de uso
theta_x = 45
theta_y = 60
theta_z = 75

# Cambiar el orden de las rotaciones
orden = "ZXY"

R = matriz_rotacion(theta_x, theta_y, theta_z, orden)

print("Matriz de rotación:")
print(R)