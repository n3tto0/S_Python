def r_funcao(a, b, x):
    if b == -b:
        i = b/a
        return i
    else:
        i = -b/a
        return i
    
    

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
x = float(input("Digite o valor de x: "))

print(r_funcao(a, b, x))
