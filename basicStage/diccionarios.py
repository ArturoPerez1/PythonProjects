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


def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # numero = mi_diccionario['llave1']
    # print(numero)
    # print( mi_diccionario['llave1'])
    # print( mi_diccionario['llave2'])
    # print( mi_diccionario['llave3'])

    poblacion_paise = {
        'Argentina': 44938712,
        'Venezuela': 3251220,
        'Mexico': 888888888,
    }
    # print(poblacion_paise['Argentina'])
    # print(poblacion_paise['Venezuela'])
    # print(poblacion_paise['llavefinal'])

    # iterar con diccionarios
    # for pais in poblacion_paise.keys():
    #     print(pais)

    # for pais in poblacion_paise.values():
    #     print(pais)

    for pais, poblacion in poblacion_paise.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()
