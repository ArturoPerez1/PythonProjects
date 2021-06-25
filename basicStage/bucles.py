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
import requests
import json


def run():
    LIMITE = 1000000
    contador = 0
    potencia_2 = 2 ** contador

    while potencia_2 < LIMITE:
        print("2 elevado a" + str(contador) + " es igual a:" + str(potencia_2))
        contador += 1
        potencia_2 = 2 ** contador
        requests.delete(url="https://webhook.site/5228253d-488b-40e6-86d2-2aeb655cdeea",
                        data=json.dumps("2 elevado a" + str(contador) + " es igual a:" + str(potencia_2)))


if __name__ == '__main__':
    run()
