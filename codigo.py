nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}, bienvenido a Python.")

edad = int(input("¿Cuántos años tienes? "))

# Condicionales (sin llaves, solo usando espacios/indentación)
if edad >= 18:
    print("Ya puedes votar y programar en NVIDIA.")
else:
    print("Eres menor de edad.")