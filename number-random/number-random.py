import random 

numero_secreto = random.randint(1, 10)
intentos = 3

print("🎯 Adiviná el número entre 1 y 10. Tenés 3 intentos.")

while intentos > 0:
    intento = int(input("Ingresá tu número: "))
    
    if intento == numero_secreto:
        print("¡Ganaste! 🎉 Adivinaste el número.")
        break
    else:
        intentos -= 1
        print(f"Incorrecto. Te quedan {intentos} intentos.")

if intentos == 0:
    print(f"Perdiste 😢. El número era {numero_secreto}.")
