users = {
    "Alejandro": "2007",
    "Natalia": "0404",
    "Iván": "2000",
}
remaining_attempts = 3
authenticated = False
current_user = ""

while remaining_attempts > 0:
    user = input("Ingresa tu usuario: ")
    password = input("Ingresa tu contraseña: ")

    if user in users and users[user] == password:
        print(f"\n¡Bienvenido, {user}!\n")
        authenticated = True
        current_user = user
        break
    else:
        remaining_attempts -= 1
        print(f"Usuario o contraseña incorrectos. Intentos restantes {remaining_attempts}")
if not authenticated:
    print("\n ¡ACCESO BLOQUEADO! ")
    exit()

while True:
    print("Menú")
    print("1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")

    option = input("Selecciona una opción: ")

    if option == "1":
        print(f"\nPerfil de usuario: {current_user}\n")
    elif option == "2":
        newpass = input("Ingresa una nueva contraseña: ")
        users[current_user] = newpass
        print("¡Contraseña actualizada exitosamente!")
    elif option == "3":
        print("\n Sesión cerrada. ¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Inténtalo nuevamente.\n")