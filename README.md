# Cliente de API de Terremotos por USGS.

El presente proyecto consume una API de terremotos y coloca la información en una interfaz. Elaborado en Python para la materia de Laboratorio para el Despliegue de Aplicaciones. 

## Funcionamiento

Se le da la oportunidad al usuario de agregar parámetros como:
- Fecha de inicio.
- Fecha final.
- Magnitud mínima.
- Límite de resultados a desplegar (1 a 20,000)
- Orden de resultados (por fecha, por fecha ascedente, por magnitud, por magnitud ascendente).

## Instalaciones

Para poder realizar la ejecución de este proyecto es importante contar con la siguiente instalación:
``` bash
  pip install tkcalendar
```
Esta nos ayudará a otorgar al usuario una interfaz intuitiva permitiéndole escoger fechas.

## Pruebas de ejecución
- Consumo de API con resultados.

- Consumo de API sin resultados.