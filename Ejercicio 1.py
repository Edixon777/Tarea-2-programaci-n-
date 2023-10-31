#primero definimos la funcion que calcule la suma de los cuadrados de las cifras de un numero 
def suma_de_cuadrados(n):
   total = 0
   while n > 0:
    var = n % 10
    total += var ** 2
    n //= 10
   return total
#ahora pedimos al usuario que ingrese su numero 
numero = int(input("Ingrese un numero positivo y mayor a 0:"))
var_2 = numero
if numero <= 0:
        print("Ingrese un numero positivo y mayor a 0:")
else:
#ahora creamos una funcion que indique que si la suma de cuadrados nos dio en el total 1 el numero es feliz y si llega a 4 no es un numero feliz, porque cuando sumamos los cuadrados de las cifras de un numero no feliz al llegar a 4 entra en bucle sin llegar nunca a ser 1 el resultado final 
     while True:
       var_2 = suma_de_cuadrados(var_2)
       if var_2 == 1:
          print(f" {numero} es un número feliz.")
          break
       elif var_2 == 4:
          print(f" {numero} no es un número feliz")
          break