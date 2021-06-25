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


def es_primo(numero):
    contador = 0
    if numero == 1:
        return False
    else:
        for i in range(1, numero + 1):
            if i == 1 or i == numero:
                continue
            if numero % i == 0:
                contador += 1
        if contador == 0:
            return True
        else:
            return False


def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()
