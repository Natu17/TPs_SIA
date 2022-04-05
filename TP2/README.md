# TP2: Algoritmos Genéticos

## Instalación y Ejecución
Instalación de todos los requerimientos previos: ./init.sh

Ejecución: python3 main.py *(archivo.json)
el parametro del archivo.json es opcional, si no se coloca nada se utiliza el config.json por default

## Guia de uso
En el config.json se pueden observar todos los parametros que pueden ser cambiados por el usuario

```
{
    "parents_selection": "random",
    "selection": "truncated",
    "TRUNC_N": 100,
    "Tc": 1.0,
    "To":20,
    "k":0.004,
    "breeding": "multiple_breed",
    "parents_replacement":true,
    "population": 100,
    "mutation":0.1,
    "deviation":1,
    "seed":1,
    "stop_condition": "generation",
    "range": [0, 1],
    "max_generations":10000,
    "error":0.001,
    "mutations" : "mutation"
}
```

"parents_selection" y "selection" define como va a ser la seleccion de padres y de hijos:
- "roulette": seleccion de ruleta
- "direct": seleccion elite
- "rank": seleccion rank
- tournament": seleccion tournament
- "truncated": seleccion truncated. Podria agregar el parametro "TRUNC_N" oara definir el valor del truncamiento
- "boltzmann": seleccion boltzmann. Se podria agregar el parametro "Tc", "To", "k" igualmente todos tienen valores por default.
- "random": seleccion totalmente random

"parents_replacement": define si hay o no remplazo.

"population": define la cantidad de individuos que va a haber en la población.

"mutation": define la posibilidad de que mute el alelo individuo

"deviation": desviación 

"stop_condition": 
- "error":Se detiene cuando se llega a x error
- "generation":Se detiene cuando se llega a unn numero maximo de generaciones
- "fitness": Se detiene cuando la mayoria de la población llega a un fitness. Se puede agregar el  "limit_fitness" como parametro que indica cuantas generaciones tienen que pasar sin cambio para que pare.

"range":
    
"max_generations":maxima generaciones
    
"error":maximo error

"mutations" : 
- mutation_one: puede mutar solo un alelo
- mutation: puede mutar todos los alelos 

"seed":
Sirve para repetir el esperimento

## Ejemplo de configuración
```
{
    "parents_selection": "random",
    "selection": "direct",
    "breeding": "uniform_breed",
    "parents_replacement":true,
    "population": 100,
    "mutation":0,
    "deviation":1,
    "seed":1,
    "stop_condition": "fitness",
    "range": [0, 1],
    "mutations" : "mutation",
    "limit_fitness": 10
}
```
