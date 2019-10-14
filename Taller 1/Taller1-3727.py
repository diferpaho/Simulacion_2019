#!/usr/bin/env python
# coding: utf-8

# # T1 - Taller 1.Implementación de generadores de números pseudoaleatorios

# Diego Fernando Palacios Hoyos
# 160003727
# 

# 1. Implementar el generador de números pseudoaleatorios con el método de MidSquare
# 
# Semilla= 3708
# Numeros aleatorios= 10

# In[3]:


dato = input("Ingresa un semilla: ")
N = input("¿Cuantos numeros?  ")
i=0
final=[]
l=int(len(dato))

while i<int(N):
    cuadrado=str(int(dato)*int(dato))
    n=len(cuadrado)
    if l==4:
        uno=int(cuadrado[n-3])
        dos=int(cuadrado[n-4])*10
        tres=int(cuadrado[n-5])*100
        cuatro=int(cuadrado[n-6])*1000
        numero=(uno+dos+tres+cuatro)
        print(numero/10000)
        final.append(numero/10000)
            
        
        if l==6:
            uno=int(cuadrado[n-4])
            dos=int(cuadrado[n-5])*10
            tres=int(cuadrado[n-6])*100
            cuatro=int(cuadrado[n-7])*1000
            cinco=int(cuadrado[n-8])*10000
            seis=int(cuadrado[n-9])*100000
            numero=(uno+dos+tres+cuatro+cinco+seis)
            print(numero/1000000)
            final.append(numero/1000000)
    i=i+1
    dato=numero
    


# 2. Implementar el generador congruencial mixto
# 
# Semilla=7
# a=5
# c=3
# m=16
# Numeros aleatorios= 10

# In[4]:


x = input("Ingresa un semilla: ")
a = input("Ingresa a: ")
c = input("Ingresa c: ")
m = input("Ingresa m: ")
N = input("¿Cuantos numeros? ")
i=1
final=[]

while i<=int(N): 
    xn=int(a)*int(x)
    xi=(xn+int(c))%int(m)
    ui=xi/int(m)
    print(ui)
    i=i+1
    x=xi
    final.append(ui)


# 3. Implementar una función para calcular el ciclo de cualquier generador de números pseudoaleatorios
# 
# Ejemplo1:

# In[12]:


def ciclo(numeros,N):
    i=0
    final=[]
    r1=0
    r2=0
    while i<int(N):
        j=i+1
        while j<int(N):
            if numeros[i]==numeros[j]:
                r1=i
                r2=j
                j=int(N)-1
                i=int(N)-1
                
            j=j+1
        i=i+1
    N=int(N)-r2
    tamaño=0    
    if r1 !=0:
        
        x=0
        while x < N:
            #print(x,r1,r2)
            if numeros[r1]==numeros[r2]:
                final.append(numeros[r1])
                tamaño=tamaño+1
            x=x+1
            r1=r1+1
            r2=r2+1
                
        print("El ciclo que se repite es: ",final,"El tamaño del ciclo es: ",tamaño)
    if r1 == 0:
        print("No hay ciclo")
                
        
  
        
        
dato = input("Ingresa un semilla: ")
N = input("¿Cuantos numeros?  ")
i=0
final=[]
l=int(len(dato))

while i<int(N):
    cuadrado=str(int(dato)*int(dato))
    n=len(cuadrado)
    if l==4:
        uno=int(cuadrado[n-3])
        dos=int(cuadrado[n-4])*10
        tres=int(cuadrado[n-5])*100
        cuatro=int(cuadrado[n-6])*1000
        numero=(uno+dos+tres+cuatro)
        print(numero/10000)
        final.append(numero/10000)
            
        
        if l==6:
            uno=int(cuadrado[n-4])
            dos=int(cuadrado[n-5])*10
            tres=int(cuadrado[n-6])*100
            cuatro=int(cuadrado[n-7])*1000
            cinco=int(cuadrado[n-8])*10000
            seis=int(cuadrado[n-9])*100000
            numero=(uno+dos+tres+cuatro+cinco+seis)
            print(numero/1000000)
            final.append(numero/1000000)
    i=i+1
    dato=numero
    

ciclo(final,N)


# Ejemplo 2:
# 

# In[13]:


def ciclo(numeros,N):
    i=0
    final=[]
    r1=0
    r2=0
    while i<int(N):
        j=i+1
        while j<int(N):
            if numeros[i]==numeros[j]:
                r1=i
                r2=j
                j=int(N)-1
                i=int(N)-1
                
            j=j+1
        i=i+1
    N=int(N)-r2
    tamaño=0    
    if r1 !=0:
        
        x=0
        while x < N:
            #print(x,r1,r2)
            if numeros[r1]==numeros[r2]:
                final.append(numeros[r1])
                tamaño=tamaño+1
            x=x+1
            r1=r1+1
            r2=r2+1
                
        print("El ciclo que se repite es: ",final,"El tamaño del ciclo es: ",tamaño)
    if r1 == 0:
        print("No hay ciclo")
          

x = input("Ingresa un semilla: ")
a = input("Ingresa a: ")
c = input("Ingresa c: ")
m = input("Ingresa m: ")
N = input("¿Cuantos numeros? ")
i=1
final=[]

while i<=int(N): 
    xn=int(a)*int(x)
    xi=(xn+int(c))%int(m)
    ui=xi/int(m)
    print(ui)
    i=i+1
    x=xi
    final.append(ui)
    
ciclo(final,N)


# # resultados
# 
# En el ejemplo 1:
# El ciclo que se repite es:  [0.61, 0.21, 0.41] El tamaño del ciclo es:  3
# 
# En el ejemplo 2:
# No hay ciclo
