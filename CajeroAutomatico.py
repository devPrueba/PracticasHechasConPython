usuarioNoa = "noa"
claveNoa = "123456"
saldo = 1000

def validaUsuario(u, c):
    if u == usuarioNoa and c == claveNoa:
        return True
    return False

def login():
    print("Bienvenido")
    usuario = input("digite su usuario: ")
    clave = input("digite a contraseña: ")
    return validaUsuario(usuario, clave)

def retirar(valor):
    if valor > saldo:
        return False, saldo
    return True, saldo - valor

def depositar(valor):
    return True, saldo + valor

def accion(opcion):
    if opcion == 1:
        valor = int(input("Digite el valor a Depositar: "))
        return depositar(valor)

    if opcion == 2:
        valor = int(input("Digite el valor a retirar: "))
        return retirar(valor)

    return False, saldo

def ejecutar():
    if not login():
        print("Usuario o contraseña invalido...")
        return

    print("Que desea hacer?")
    opcion = int (input("1.-->Depositar o 2.-->retirar: "))

    ok, saldo = accion(opcion)

    if not ok:
        print("no se realizo la accion, saldo:", saldo)
    else:
        print("accion realizada correctamente, saldo:",saldo)


ejecutar()





