while True:
    print("\n--- Menu ---")
    print("1: Calculatrice")
    print("2: Convertisseur d’unités")
    print("3: Distance")
    print("4: Poids")
    print("5: Quitter")

    option = input("Choisis une option: ")
    if option == "1":
        num1 = int(input("What is the first number : "))
        num2 = int(input("What is the seconde number: "))
        opérateur = input("+, -, *, / : ")
        
        def addition(a, b):
            return a + b
        
        def soustraction(a, b):
            return a - b
        
        def Multiplication(a, b):
            return a * b
        
        def Division(a, b):
            return a / b
        
        if opérateur == "+":    
            print(f"La somme de {num1} + {num2}: {addition(num1, num2)}")
        elif opérateur == "-":
            print(f"La différence de {num1} - {num2}: {soustraction(num1, num2)}")
        elif opérateur == "*":
            print(f"Les produits de {num1} * {num2}: {Multiplication(num1, num2)}")
        elif opérateur == "/":
            try:
                print(f"Le quotient de {num1} / {num2} = {Division(num1, num2)}")
            except ZeroDivisionError:
                print("Erreur ❌ : division par zéro interdite.")
        else:
            print("Ce n'est pas une option")

    elif option == "2":
        temperature_celsius = float(input("Entrez la température en °C : "))
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32
        temperature_kevin = (temperature_celsius + 273.15)

        print(f"La température {temperature_celsius}°C  est {temperature_fahrenheit}°F(Fahrenheit)")
        print(f"La température {temperature_celsius}°C  est {temperature_kevin}°K(Kelvin)")
    
    elif option == "3":
        valeur1 = float(input("Entré la premiére valeur: "))

    elif option == "4":
        pass


