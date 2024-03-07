# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# importando a funcao sqrt da biblioteca math
from math import sqrt
# variavel número
n=int(input())
print(f"raiz: {int(sqrt(n))}") if n >= 0 else print("ERRO!!! não existe raiz de números negativos somente nos imaginarios")
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# OUTRA FORMA
# Propiedade da radiciação
# raiz quadrada de a == radicando(a) elevado a razao entre o seu expoente(numerador) e o indice da raiz(denominador)
print(f"raiz: {int(n**(1/2))}") if n >= 0 else print("ERRO!!! não existe raiz de números negativos somente nos imaginarios")
 