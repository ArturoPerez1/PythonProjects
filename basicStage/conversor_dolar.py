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
print("     CONVERSOR DE MONEDAS      ")
dolares = input("Ingrese la cantidad de Dolares tienes: ")
dolares = float(dolares)
valor_dolar = 3125000
bolivares = dolares * valor_dolar
bolivares = round(bolivares, 2)
bolivares = str(bolivares)
print("Tienes: " + bolivares + "bs")
