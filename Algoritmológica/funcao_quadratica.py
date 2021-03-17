def f_quadratica(a, b, c, x):
    if a == 0:
        i = x**2+b*x+c
        return i
    else:
        i = a*(x**2)+b*x+c
        return i
                    

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
x = float(input("Digite o valor de x: "))

print(f_quadratica(a, b, c, x))
