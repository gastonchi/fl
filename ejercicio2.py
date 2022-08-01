x = int(input("Elige un número cualquiera "))
opcion = int(input("Elige una opción: 1, 2, 3 o 4"))

if opcion == 1:
    print(abs(x))
elif opcion == 2:
    print(x**2)
elif opcion == 3:
    print(x**3)
elif opcion == 4:
    print(x,"!")
else:
    print("No es una opción válida")
