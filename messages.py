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

def bye_msg():
    print("\n" + "=" * 50)
    print("Gracias por completar la session \U0001F601".center(50, " "))
    print("Sus respuestas han sigo guardadas \U0001F510".center(50, " "))
    print("\U0001F9EC Hasta pronto \U0000270C".center(50, " "))
    print("\n" + "=" * 50)

def error_msg():
    print("\n" + "=" * 50)
    print("La accion a arrojado un error \U0001F615 \U0001F914 ".center(50, " "))
    print("Tenga en cuenta que debe responder".center(50, " "))
    print("las opciones 1 y 2 del menu principal".center(50, " "))
    print("luego puedes unificar las repuestas".center(50, " "))
    print("\U0001F91F Intentalo de nuevo \U0001F91F ".center(50, " "))

def successfull_msg():
    print("\n" + "=" * 50)
    print("")
    print("Accion realizada exitosamente \U0001F510".center(50, " "))

def menu():
    print("\n" + "=" * 50)
    print("¿Que accion deseas realizar? \U0001F914".center(50, " "))
    print("\n\t1. preguntas al despertar \U0001F31E")
    print("\t2. preguntas al acostarse \U0001F31C	")
    print("\t3. administracion de medicamentos \U0001F48A")
    print("\t4. Unificar preguntas por dia \U0001F48A")
    print("\t5. Salir\n")
    print("\n" + "=" * 50)
