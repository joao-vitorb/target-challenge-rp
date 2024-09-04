# 2)
# Escreva um programa que verifique, em uma string, a existência da
# letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade
# de vezes em que ela ocorre.

def count_a_in_string(s):
    count = s.lower().count('a')
    
    if count > 0:
        return True, count
    else:
        return False, 0

input_string = input("Digite uma string: ")

found, count = count_a_in_string(input_string)

if found:
    print(f"A letra 'A' está presente {count} vez(es) na string.")
else:
    print("A letra 'A' não está presente na string.")