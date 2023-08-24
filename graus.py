def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_kelvin(celsius):
    kelvin = (celsius + 273,15) 
    return kelvin

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9 
    return celsius

def fahrenheit_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273,15 
    return kelvin

def kelvin_celsius(kelvin):
    celsius = (kelvin - 273,15) 
    return celsius

def kelvin_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273,15) * 9/5 + 32 
    return fahrenheit 


print("Escolha uma operação:")
print("1. Celsius > Fahrenheit")
print("2. Celsius > Kelvin")
print("3. Fahrenheit > Celsius")
print("4. Fahrenheit > Kelvin")
print("5. Kelvin > Celsius")
print("6. Kelvin > Fahrenheit")

escolha = input("Insira o número da opção desejada.")

if escolha == "1":
    temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
    temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)
    print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)

elif escolha == "2":
    temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
    temperatura_kelvin = celsius_kelvin(temperatura_celsius)
    print("A temperatura em Kelvin é:", temperatura_kelvin)

elif escolha == "3":
    temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    temperatura_celsius = fahrenheit_celsius(temperatura_fahrenheit)
    print("A temperatura em Celsius é:", temperatura_celsius)

elif escolha == "4":
    temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    temperatura_kelvin = fahrenheit_kelvin(temperatura_fahrenheit)
    print("A temperatura em Kelvin é:", temperatura_kelvin)

elif escolha == "5":
    temperatura_kelvin = float(input("Digite a temperatura em Kelvin: "))
    temperatura_celsius = kelvin_celsius(temperatura_kelvin)
    print("A temperatura em Celsius é:", temperatura_celsius)

elif escolha == "6":
    temperatura_kelvin = float(input("Digite a temperatura em Kelvin: "))
    temperatura_fahrenheit = kelvin_fahrenheit(temperatura_kelvin)
    print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)
