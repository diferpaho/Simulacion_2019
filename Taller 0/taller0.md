
# Taller 0
Diego Fernando Palacios Hoyos
160003727

Taller 0. Comparar Simulación de Monte Carlo y método numérico del Trapecio

## Metodo Monte carlo




```python
import random

import math


n=0
suma=0

while n<10000:
    x=2 * random.random()
    y=2 * math.exp(x*x*(-1))
    suma=suma+y
    n=n+1
    
print ('Resultado ', (suma/n))
```

    Resultado  0.8816953258362659
    

## Metodo numérico del Trapecio


```python
import math

paso= 0.1
x1= 0
x2= paso
suma= 0

while x2 <= 2:
     fx2= math.exp(x2*x2*(-1))
     tria= (math.exp(x1*x1*(-1))-fx2)*paso/2
     suma=suma+tria+(fx2*paso)
     x1= x2
     x2= x2+paso
     
print ('Resultado: ', suma)
```

    Resultado:  0.8797520661078067
    

## Por wolframalpha de comprueba el resultado:


![image.png](attachment:image.png)


## Resultados

Por Monte carlo: 0.8816953258362659
    
Por numérico del Trapecio: 0.8797520661078067
    
Por wolframalpha: 0.882081
