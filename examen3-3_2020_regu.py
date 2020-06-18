# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:46:40 2020

@author: 
        Garcia Garcia Efrain 15590287
"""
"""

 Fibonacci  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo números de la
	serie fibonaci existentes de 0 hasta n-1 que 
	cumpla con el siguiente prototipo:
	
	def fibo(N):
		pass
	
	
	a = fibo(10)
	z = [e for e in a]
	print(z)
	# [0, 1 ,1 ,2 ]
"""
print(" Fibonacci  <generadores>  30 pts ")
def fibo(N):
    a, b = 0,1
    while a < N:
        print(a, end=' ')
        a, b = b, a+b
		

a = fibo(3)
print()

"""
Patron332 <generadores> 20 pts
	
	Un montón de generos musicales usan el patron 3-3-2
	(Tango, Bachata, Bolero, Milonga, Salsa, Reegueton... )
	que es una manera de simplificar la secuencia de tonos
	1,2,3,1,2,3,1,2.
    332
	
	
	Explicación del patrón ritmico
	https://youtu.be/XU4P_65-OqU?t=186
	Complemento a la explicación
	https://youtu.be/htkI1ZDcOs0?t=58
	
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N, correspondiente al patron
	con las siguientes condiciones:
	
	def p332(N):
		pass
		
	a = p332(10)
	z = [e for e in a]
	print(z)
	#[1,2,3,1,2,3,1,2,1,2]
      1,2,3,4,5,6,7,8,9,10
  1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
  
"""
print("Patron332 <generadores> 20 pts")
def p332(N):
    i = 1
    while i <= N:
        if i % 4 == 0 and i == 4 :
            yield 1 
        elif i % 5 == 0:
            yield 2
        elif i % 6 == 0:
            yield 3
        elif i % 7 == 0:
            yield 1
        elif i % 8 == 0:
            yield 2            
        elif i % 9 == 0:
           yield 1
        elif i % 10 == 0:
            yield 2
        else:
            yield i
        i = i + 1
		
a = p332(10)
z = [e for e in a]
print(z)
#[1,2,3,1,2,3,1,2,1,2]
    
"""


Combinaciones <Comprensión de listas> 30pts

	Una exploradora y arqueologa quiere saber cuantas combinaciones de 
	herramientas de trabajo, supervivencia y comida puede realizar 
	a partir de un grupo de 5 herramientas trabajo (lupa; cepillo; 
	martillo y cincel; camara fotografica; o piqueta),      
	4 herramientas de supervivencia
	(lampara, pedernal, olla y cuchillo) y uno de 4 comidas
	posibles (Atun enlatado, frijoles enlatados, comida militar, carne seca)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
print("Combinaciones 30pts.")
C = ['lupa', 'cepillo', 'martillo', 'cincel', 'piqueta']
P = ['lampara', 'pedernal', 'olla', 'cuchillo']
A = ['Atun enlatado', 'frijoles enlatados', 'comida militar', 'carne seca']
U = [ [a,b,c] for a in C for b in P for c in A]
print(U)
L = len(U)
print('La cantidad de combinaciones es:', L)


"""
    
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos las combinaciones
	que incluyen un atun enlatado y tambien despliegue su longitud
	
	
"""

print("Combinaciones Fedora 15pts.")
def contar(L):
    if not L:
        return[]
    if 'Atun enlatado' in L[0]:
        return [L[0]]+contar(L[1:])
    else:
        return contar(L[1:])
LS= contar(U)
print("Conjuntos con atun enlatado: ", LS)
print("Numero de conjuntos: ", len (LS))


"""
<Monads>   30 pts

--Lacrimosa - Durch Nacht und Flut --   

Die Suche endet jetzt und hier
Gestein kalt und nass
Granit in Deiner Brust
Der Stein der Dich zerdrückt
Der Fels der Dich umgibt
Aus dem gehauen Du doch bist

Despiertate te busco
Mi corazon abreté te libro
Elevate mi luz y prende mi llama
Si a ti, yo se, te encontrare

El fragmento anterior es un canción del duo lacrimosa

Usando Monads obtenga la letra 
que menos se repite por cada linea y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""


"""
<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""


