import maths
loop = True

while loop == True:

    print("-----------------------------------------------------------------")
    print("OPCIONES: \n1-Suma\n2-Resta\n3-Multiplicar\n4-Dividir\n5-Restante")
    try:

        opcion = int(input("Inserte opcion deseada: "))
        valor1 = int(input("Inserte primer valor: "))
        valor2 = int(input("Inserte segundo valor: "))
    except:
        print("Valuer Error")

    try:
        if opcion == 1:
            resultado = maths.sumar(valor1,valor2)
            print("La suma de %d + %d es %d" % (valor1, valor2, resultado))  
        elif opcion == 2:
            resultado = maths.restar(valor1,valor2)
            print("La resta de %d - %d es %d" % (valor1, valor2, resultado))
        elif opcion == 3:
            resultado = maths.multiplicacion(valor1,valor2)
            print("La multiplicacion de %d * %d es %d" % (valor1, valor2, resultado))
        elif opcion == 4:
            resultado = maths.division(valor1,valor2)
            print("La division de %d / %d es %d" % (valor1, valor2, float(resultado)))
        elif opcion == 5:
            resultado = maths.restante(valor1,valor2)
            print("El restante de %d y %d es %d" % (valor1, valor2, resultado))
        else:
            print("Error en las entradas, Bye")
    except ZeroDivisionError:
        print( "Error, no se puede dividir entre 0")
    except ValueError:
        print( "Value Error")       
    except NameError:
        print( "Name Error")

