from ast import Try


print("1: Calculatrice \n2: Convertisseur d’unités")
option = input("Chose an option: ")

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
        print(f"Le quotient de {num1} / {num2}: {Division(num1, num2)}")
    else:
        print("Ce n'est pas une option")

elif option == "2":
    temperature_celsius = float(input("Entrez la température en °C : "))
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    temperature_kevin = (temperature_celsius + 273.15)
    print(f"La température {temperature_celsius}°C  est {temperature_fahrenheit}°F(Fahrenheit)")
    print(f"La température {temperature_celsius}°C  est {temperature_kevin}°K(Kelvin)")
else:
    print("Ce n'est pas une option")
