# 1)
# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre
# será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule
# a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.

def is_fibonacci(n):
    if n < 0:
        return False

    def fibonacci_until(max_value):
        a, b = 0, 1
        while a <= max_value:
            yield a
            a, b = b, a + b

    for num in fibonacci_until(n):
        if num == n:
            return True
    return False

number = int(input("Insira um valor: "))

if is_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")