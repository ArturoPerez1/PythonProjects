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
import random


def generar_password():
    mayusculas = ['A', 'B', 'C', 'D', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'f', 'g']
    simbolos = ['!', '#', '%', '&', '/', '*']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password


def run():
    password = generar_password()
    print("Tu nuevo password es: " + password)


if __name__ == '__main__':
    run()
