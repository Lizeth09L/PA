def tree_n_plus1(numero):
  """
  Esta función implementa el algoritmo 3n+1 para un número dado.

  Parámetros:
    numero: El número inicial para el algoritmo.

  Retorno:
    La cantidad de pasos necesarios para llegar a 1.
  """

  numero_iteraciones = 0
  numero_actual = numero

  while (numero_actual != 1):
    """
    Bucle que itera hasta que el número actual llegue a 1.
    """
    if numero_actual % 2 == 0:
      """
      Si el número actual es par, se divide por 2.
      """
      numero_actual = numero_actual / 2
    else:
      """
      Si el número actual es impar, se multiplica por 3 y se le suma 1.
      """
      numero_actual = (3 * numero_actual) + 1
    numero_iteraciones = numero_iteraciones + 1

  if numero_actual == 1:
    print("La cantidad de veces es", numero_iteraciones)
  else:
    print(numero_actual)

numero = float(input("Número: "))
tree_n_plus1(numero)
#lizeth londoño 1027400993