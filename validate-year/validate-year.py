nombre = input("¿como te llamar?.")
edad = int(input("¿Que edad tenes?."))

print(f"Hola, {nombre}. Tenes {edad} años.")

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("No eres mayor de edad.")