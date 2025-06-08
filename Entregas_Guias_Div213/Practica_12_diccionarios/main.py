from estudiantes import estudiantes
from paquete.continuar_en_menu import continuar_en_menu
from paquete.validar_ingreso import validar_ingreso_de_datos
from paquete.listar_por_apellido import listar_por_apellido_o_nombre
from paquete.mostrar_promedio_de_notas import mostrar_promedio_de_notas
from paquete.mostrar_alumnos_ingenieria_informatica import mostrar_alumnos_ingenieria_informatica
from paquete.mostrar_promedio_edad import mostrar_promedio_edad
from paquete.mejor_promedio_de_notas import mostrar_alumno_con_mayor_promedio_de_notas
from paquete.mostrar_alumnos_del_club import mostrar_alumnos_del_grupo
from paquete.mostrar_que_cursan_los_jovenes import mostrar_que_cursan_los_mas_jovenes


seguir = True

while seguir:
    # Muestro el menu
    print("✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹✹")
    print("⫷⫷⫷⫷⫷⫷⫷⫷⫷⫷ MENU DE OPCIONES ⫸⫸⫸⫸⫸⫸⫸⫸⫸⫸\n")
    print("☰ 1. Listado de alumnos por apellido (asc) \n" \
          "☰ 2. Promedio de notas de cada estudiante \n" 
          "☰ 3. Estudiantes de Ing. Informatica \n" 
          "☰ 4. Promedio de dedad de los estudiantes \n" 
          "☰ 5. Alumno con mejor promedio \n"
          "☰ 6. Alumnos del grupo 'Club de informatica' \n"
          "☰ 7. Ver que cursan los alumnos mas jovenes \n"
          "☰ 8. Salir \n")
    
    # Pido el numero
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    opcion = input("● Menu al que desea ingresar (1-8): ")

    

    # Vuelvo a pedir que se ingrese un numero en caso de que no se encuentre entre 1 y 5
    opcion = validar_ingreso_de_datos('❌ La opcion ingresada es invalida ❌', "● Menu al que desea ingresar", 1, 8, opcion)
    
    
    # Camino segun opcion validada elegida 
    if opcion == '1':
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        listar_por_apellido_o_nombre(estudiantes)
    
    elif opcion == '2':
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        mostrar_promedio_de_notas(estudiantes)

    elif opcion == '3':
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        mostrar_alumnos_ingenieria_informatica(estudiantes)

    elif opcion == '4':
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        mostrar_promedio_edad(estudiantes)

    elif opcion == '5':
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        mostrar_alumno_con_mayor_promedio_de_notas(estudiantes)
    
    elif opcion == '6':
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        mostrar_alumnos_del_grupo(estudiantes, "Club de Informatica")
    
    elif opcion == '7':
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        mostrar_que_cursan_los_mas_jovenes(estudiantes)
    
    else:
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n" \
              "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(" ʜᴀsᴛᴀ ʟᴜᴇɢᴏ !!! 😁 👋")
        break


    # Seguir en el menu
    seguir = continuar_en_menu()