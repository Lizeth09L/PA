def collatz_sequence(number):
  """
  Calculates the Collatz sequence for a given number and prints the count of iterations.

  Parameters:
  - number (int): The input number for the Collatz sequence.

  Example:
  >>> collatz_sequence(6)
  La cantidad de veces: 8
  """
  iteration_count = 0
  while number != 1:
    if number % 2 == 0:
      number = number // 2  # Use // for integer division
    else:
      number = (3 * number) + 1
    iteration_count += 1

  print("La cantidad de veces:", iteration_count)

# Get input from the user
user_number = int(input("Ingrese un número: "))
collatz_sequence(user_number)

if _name_ == "_main_":
  import doctest
  import sys

  # Verificar si se proporciona un argumento específico en la línea de comandos
  if len(sys.argv) > 1 and sys.argv[1] == "--rundoctest":
    doctest.testmod()