# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# # # variavel numero
n = int(input())
bit = []
while n >= 2:
     bit.append(n%2)
     n = int(n/2)
     #condicao ultimo quociente
     if n<2:
         bit.append(n)
# printar da direita para a esquerda
for i in range(1, len(bit)+1):
    print(bit[-i],end="")

    
