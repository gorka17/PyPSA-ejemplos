# PyPSA-ejemplos

Ejemplos de uso de PyPSA tomados de su documentación junto con un ejemplo de cómo utilizar Snakemake como gestor de workflows en este contexto.

---

## Contenido principal

- El script **minimal_example.ipynb** contiene un ejemplo de cómo crear y optimizar una red sencilla utilizando PyPSA, incluyendo la definición de buses, generadores, cargas y la resolución del flujo de potencia.

- En **acdc_example.ipynb** se parte de un ejemplo tomado de la propia librería PyPSA que incluye una red más compleja con varios buses, generadores y configuraciones tanto de redes AC como DC.

---

## Carpeta `mi_red`

Esta carpeta contiene la estructura de ficheros necesaria para lanzar una tarea mediante Snakemake, usando un Snakefile.

En este caso, el workflow crea una red sencilla, la optimiza y guarda el resultado en el archivo `red_resuelta.nc` dentro de la subcarpeta `outputs`.

El código que se ejecuta está dentro de la carpeta `scripts`.

---

## Uso básico

Para ejecutar el workflow con Snakemake desde la carpeta `mi_red`, basta con ejecutar:

```bash
snakemake
