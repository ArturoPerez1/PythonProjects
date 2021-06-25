# -*- coding: utf-8 -*-
"""
Copyright (C) 2021 PythonProjects

This file is part of core.

core is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

core is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
"""


# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones!")


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


def conversacion(mensaje):
    print("Hola")
    print("Como estas")
    print(mensaje)
    print("Adios")


opcion = int(input("Elige una opion (1,2,3): "))

if opcion == 1:
    conversacion("Elegiste la opcion 1")

elif opcion == 2:
    conversacion("Elegiste la opcion 2")

elif opcion == 3:
    conversacion("Elegiste la opcion 3")

else:
    print("Escribe la opcion correcta")
