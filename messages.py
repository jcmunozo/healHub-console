from utilities import is_valid_number

def welcome_msg():
    print("\n" + "=" * 50)
    print("BIENVENIDO A \U0001F9E0".center(50, " "))
    print("=" * 50)
    print("      __ __              __   __ __         __ ")
    print("     / // / ___  ___ _  / /  / // / __ __  / / ")
    print("    / _  / / -_)/ _ `/ / /  / _  / / // / / _ \\")
    print("   /_//_/  \\__/ \\_,_/ /_/  /_//_/  \\_,_/ /_.__/\n")
    print(" consola ".center(50, "*"))
    print("\n","Tu salud importa! Empecemos ... \U0001F680".center(50, " "), "\n")
    print("=" * 50, "\n")

def bye_msg():
    print("\nGracias por completar la session \U0001F601 . Sus respuestas han sido guardadas \U0001F37B.")
    print("\nSesion terminada \U0001F389. Esperamos volverte a ver para continuar con el seguimiento \U0001F510")
    print("\nHasta pronto \U0000270C  \U0001F9EC \n")

def menu():
    while True:
        print("\n¿Que accion deseas realizar? \U0001F914")
        print("\n1. preguntas al despertar \U0001F3DC")
        print("2. preguntas al acostarse \U0001F303")
        print("3. administracion de medicamentos \U0001F48A")
        print("4. Salir\n")
        response = input("\U0001F48A Ingrese la opcion deseada por favor: \n\t")
        result = is_valid_number(response,1,4)
        if result == "Ok":
            return response
        else:
            print(result)
