usuarios = {
    "lucas": {"edad": 30, "email": "lucas@example.com"},
    "ana": {"edad": 25, "email": "ana@example.com"}
}

usuario = input("Ingresá el nombre de usuario: ")

if usuario in usuarios:
    print(f"Usuario encontrado: {usuarios[usuario]}")
else:
    print("Usuario no encontrado.")
