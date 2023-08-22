fecha = str(input("Ingresar fecha: ").lower())
if fecha=="lunes" or fecha=="martes" or fecha=="miercoles" or fecha=="jueves" or fecha=="viernes":
    dia = int(input("Ingresar el numero del dia: "))
    if dia>0 and dia<32:
        mes = int(input("Ingresar el mes: "))
        if mes>0 and mes<13:

            if fecha=="lunes" or fecha=="martes" or fecha=="miercoles":
                examen = input('Hubo examen? (s/n): ').lower().strip() == 's'
                if examen == True:
                    aprobados = int(input("Ingresar el numero de aprobados: "))
                    desaprobados = int(input("Ingresar el numero de desaprobados: "))
                    total=aprobados + desaprobados
                    por_ap= int(aprobados / total * 100)
                    por_des=  int(desaprobados / total * 100)
                    print("Porcentaje de aprobados:",por_ap,"%")
                    print("Porcentaje de desaprobados:",por_des,"%")
            else:
                if fecha=="jueves":
                    asistencia = int(input("Ingresar el porcentajede asistencia: "))
                    if asistencia > 50:
                        print("Asistió la mayoría")
                    else:
                        print("No asistió la mayoría")
                else:
                    if fecha=="viernes":
                        if dia==1 and (mes==1 or mes==7):
                            print("Comienzo de nuevo ciclo")
                            cant_alum = int(input("Ingresar la cantidad de alumnos: "))
                            arancel = float(input("Arancel por alumno $ "))
                            print("El ingrso total es de $",cant_alum * arancel)

        else:
            print("Ingrese un mes valida")
    else:
        print("Ingrese un dia valido")
else:
    print("Ingrese una fecha valida")