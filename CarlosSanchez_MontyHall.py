import numpy as np
from random import shuffle

#Crea una funcion que se encarga de desordenar una lista dada para las opciones de cada puerta y devuelve dicha lista alterada
def sort_doors():
	lista=['goat','goat','car']
	np.random.shuffle(lista)
	return lista



#Crea una funcion que escoge y retorna un numero al azar entre 0 y 2 
def choose_door():
	numeros=[0,1,2]
	escoge=np.random.choice(numeros)
	return escoge


#Se revisa si en la lista dada hay un 
def reveal_door(lista,choice):
	for i in range(len(lista)):
		if(i!=choice and lista[i]=='goat'):
				lista[i]='GOAT_MONTY'
				return lista

#Asignamos cada una de las funciones a una variable distinta con el fin de que pueda imprimir para estos valores y no volver a hacer el sorteo
#puerta=sort_doors()
#print puerta
#numero=choose_door()
#print numero

#print reveal_door(puerta,numero)

#Crea la funcion que arrojara los resultados para el sorteo 
def finish_game(lista, choice, change):
	if(change==False):
		return lista[choice]
	else:
		for i in range(len(lista)):
			if(i!=choice and lista[i]!='GOAT_MONTY'):
				return lista[i]

#Asignamos cada una de las funciones a una variable distinta con el fin de que pueda imprimir para estos valores y no volver a hacer el sorteo

#puerta=sort_doors()
#print puerta
#numero=choose_door()
#print numero
#print reveal_door(puerta,numero)

#Prueba de la funcion finish_game /Correcto
#print finish_game(puerta,numero, True)

#Hacemos el sorteo 100 veces para definir las probabilidades de cada uno de ellos

lista_true=[]
lista_false=[]

for i in range (100):
	puerta=sort_doors()
	#print puerta
	numero=choose_door()
	#print numero
	b= reveal_door(puerta,numero)

	a=finish_game(b, numero, True)
	lista_true.append(a)

for i in range (100):
	puerta=sort_doors()
	#print puerta
	numero=choose_door()
	#print numero
	b= reveal_door(puerta,numero)
	a=finish_game(b, numero, False)
	lista_false.append(a)


#print lista_false
#print lista_true

#Calculamos las veces ganadoras para ver su probabilidad con cada uno de los casos de True y False

wint=0.0
winf=0.0
for i in range (len(lista_true)):
	if(lista_true[i]=='car'):
		wint+=1.0
		
for i in range (len(lista_false)):
	if(lista_false[i]=='car'):
		winf+=1.0

probt=wint/len(lista_true)
probf=winf/len(lista_false)

print "Las probabilidades de ganar cuando me cambio de puerta son de",  probt
print "Las probabilidades de ganar cuando no me cambio de puerta son de", probf
























