obtener el schudule del torneo por medio de schedule.py, tenemos los juego con boxscore y los preview para los que no se han efectuado
se tiene que chequear el id del div en el schedule pues cambia entre dias

analizar los details y colocar esta info en columnas (iniciando con los HR)
agregar las anotacioiones de batting
buscar el id de los jugadores en batting
agregar en el json
agregar el pitching
agrear las anotaciones de pitching
agregar el playtoplay

TODO
listar los ficheros del directorio
20240529
    error al ejecutar en script schedule.py
        error
            Traceback (most recent call last):
            File "c:\GitHub\yfsDataBase\MLB2023\baseball-reference\schedule.py", line 5, in <module>  
                import pandas as pd
            File "C:\Python310\lib\site-packages\pandas\__init__.py", line 22, in <module>
                from pandas.compat import is_numpy_dev as _is_numpy_dev  # pyright: ignore # noqa:F401  
            File "C:\Python310\lib\site-packages\pandas\compat\__init__.py", line 25, in <module>     
                from pandas.compat.numpy import (
        agrego entorno virtual en visual studio code
            python -m venv mlb_2023
            mlb_2023\Scripts\activate
    error
        test
            File "c:\GitHub\yfsDataBase\MLB2023\baseball-reference\schedule.py", line 1, in <module>
                from bs4 import BeautifulSoup
            ModuleNotFoundError: No module named 'bs4'       
        install
            pip install beautifulsoup4


