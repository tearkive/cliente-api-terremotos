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

![{20175A4D-C399-4C2D-B5F0-1193F763E21F}](https://github.com/user-attachments/assets/08196354-b28c-4d20-802c-ba7eceed7c96)
![{6F7A76B9-A68B-4D46-9250-5D7B0397D870}](https://github.com/user-attachments/assets/9c1cbdbb-0935-4621-8af8-d8ffb6a085e1)
![{50D37B79-7DC9-42BA-8AEF-C7BB3F26D684}](https://github.com/user-attachments/assets/e0ffd876-0a3d-49f2-8a79-534c2bba84fa)
![{08DAFFB7-07AF-41CD-BF25-B640D7246280}](https://github.com/user-attachments/assets/8fcbbb88-3bf1-49fa-8848-c62c92aab7fc)

- Consumo de API sin resultados.

![{C1C4044C-A5F7-45B2-A047-6C7134D06F00}](https://github.com/user-attachments/assets/31b7635f-6f23-434d-9e4a-9dfe6da71a4d)
