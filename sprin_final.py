import random #Se importa libreria random para crear contraseña aleatoria
import string # se importa libreria string para la creacion de contraseña random con minusculas, mayusculas y numeros.

#Lista de usuarios

usuarios = ["Andres", "Juan", "Maria", "Pedro", "Ana", "Luis", "Carlos", "Jose", "Luisa", "Lorena"]



#funcio0n para crear cuenta automatica por usuario

def cuenta_automatica(usuarios):
    cuentas = {}
    for usuario in usuarios:
        cuenta = usuario.lower() + ".cuenta_automatica"
        contraseña = generar_contrasena()
        numero_contacto = solicitar_numero_contacto(usuario)
        cuentas[usuario] = {"cuenta": cuenta, "contraseña": contraseña, "numero_contacto": numero_contacto}
    return cuentas


#Funcion para generar contraseña aleatoria

def generar_contrasena():
    caracteres = string.ascii_letters + string.digits
    contrasena =  ''.join(random.choice(caracteres) for _ in range(8))
    return contrasena

#Funcion para solicitar numero de contacto
def solicitar_numero_contacto(usuario):
    numero_contacto = input(f"Ingrese el numero de contacto para {usuario}: ")
    if len(numero_contacto) == 8 and numero_contacto.isdigit():
        return numero_contacto
    else:
        print("Error: El numero de contacto debe ser de 8 digitos numericos")

cuentas_usuarios = cuenta_automatica(usuarios)

#Imprimir las cuentas creadas por cada usuario
for usuario, cuenta_info in cuentas_usuarios.items():
    print("Usuario: ", usuario)
    print("Cuenta: ", cuenta_info["cuenta"])
    print("Contraseña: ", cuenta_info["contraseña"])
    print("Numero de contacto: ", cuenta_info["numero_contacto"])
    print()