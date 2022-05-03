usuariosdef = {"usuario1":"admin","clave1":"MisionTic2021"}

ingreso = False
intentos = 0
while (ingreso == False) and (intentos <4): 
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    
    if(usuario == usuariosdef["usuario1"]) and (clave == usuariosdef["clave1"]):
        ingreso = True 
    else:
            print("Credenciales incorrectas")
    intentos += 1

if not ingreso :
    print("Has agotado la cantidad de intentos, por favor inicie de nuevo el programa ")
elif ingreso:
    bandera1 = True
    lista_empleados, lista_visitantes ="",""
    # Menu
    menu ="\n"
    menu +="------Menú de registro de personal-----\n"
    menu +="1. Registrar ingreso de empleado. \n"
    menu +="2. Ver empleados ingresados.\n"
    menu +="3. Registrar ingreso de visitantes.\n"
    menu +="4. Ver visitantes ingresados.\n"
    menu +="\n"
    menu +="0. Salir"
    menu +="\n"
    while bandera1:           
            print(menu)
            opcion = int(inpnut("Ingresa un número válido de opción del menú: ")) 
            if opcion==1:
                n_empleado=""
                while n_empleado != "SALIR": #No grabar en la lista la palabra SALIR
                    n_empleado =input("Ingresa el nombre del empleado (Si no deseas agregar más, oprime la tecla SALIR): ")
                    if n_empleado!="SALIR":
                        lista_empleados = lista_empleados + n_empleado + ","
            elif opcion==2:
                print("Los empleados registrados son: "+ lista_empleados)
            elif opcion==3:
                n_visitante=""
                while n_visitante != "SALIR": 
                    n_visitante =input("Ingresa el nombre del visitante (Si no deseas agregar más, digite SALIR): ")
                    if n_visitante!="SALIR":
                        lista_visitantes = lista_visitantes + n_visitante + ","
            elif opcion==4:
                print("Los visitantes registrados son: " + lista_visitantes)
            elif opcion==0:
                print("¡Hasta luego!")
                bandera1=False
            else:
                print("Por favor ingresa una opción válida")
 
else:
    print("¡Hasta luego!")


