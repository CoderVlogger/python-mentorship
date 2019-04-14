def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

def restante(a,b):
    return a % b  


while True:

    print ("-----------------------------------------------------------------")
    print ("OPCIONES: \n1-Suma\n2-Resta\n3-Multiplicar\n4-Dividir\n5-Restante\n6-Exit")
    try:

        opcion = int(input("Inserte opcion deseada: "))
    except:
        print("Valuer Error")


    if opcion == 6:
        print ("Exitting...")
        break


    try:
        valor1 = int(input("Inserte primer valor: "))
        valor2 = int(input("Inserte segundo valor: "))

        if opcion == 1:
            resultado = sumar(valor1,valor2)
            print ("La suma de %d + %d es %d" % (valor1, valor2, resultado))  
        elif opcion == 2:
            resultado = restar(valor1,valor2)
            print ("La resta de %d - %d es %d" % (valor1, valor2, resultado))
        elif opcion == 3:
            resultado = multiplicacion(valor1,valor2)
            print ("La multiplicacion de %d * %d es %d" % (valor1, valor2, resultado))
        elif opcion == 4:
            resultado = division(valor1,valor2)
            print ("La division de %d / %d es %d" % (valor1, valor2, float(resultado)))
        elif opcion == 5:
            resultado = restante(valor1,valor2)
            print ("El restante de %d y %d es %d" % (valor1, valor2, resultado))
        else:
            print("Error en las entradas, Bye")
    except ZeroDivisionError:
        print( "Eror, no se puede dividir entre 0")
    except ValueError:
        print( "Value Error")       
    except NameError:
        print( "Name Error")

