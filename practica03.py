#ejercicio01
#crear un programa que calcule el area de un triangulo
def calcularArea(a,b):
    area=(b*a)/2
    return area

print("ingresar altura")
a= float(input())
print("Ingresar Base")
b= float(input())
print("El area es"   + "  "+  str(calcularArea(a,b)))

