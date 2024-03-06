
def fibonacci(limite):
  sequencia = [0, 1]
  while sequencia[-1] < limite:
    sequencia.append(sequencia[-1] + sequencia[-2])
  return sequencia

numero = int(input("Digite um número: "))
1
seq = fibonacci(numero)

if numero in seq:
  print(f"O número {numero} pertence a sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence a sequência de Fibonacci.")