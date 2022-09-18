#Declaracion de librerias
import random
import time
#Variables a utilizarce
titulo="Trivia de cultura general peruana"

pregunta1="¿Cómo se llamó el último inca?"
alternativas1=["a)Manco Cápac","b)Huascar","c)Atahualpa"]
comentarios1=[". Fue el primero la respuesta era Atahualpa.",".Fue el penúltimo la respuesta era Atahualpa ",". Atahualpa obtiene el incanato luego de vencer a Huascar, su hermano."]
respuesta1="c"

pregunta2="¿Cuál de estas alternativas, es una maravilla del mundo?"
alternativas2=["a)Pollo a la brasa","b)Machupicchu","c)Lineas de nazca"]
comentarios2=[". Pero estamos de acuerdo en que el pollo debería ser una maravilla.",". Esta era sencilla.",". ¿Serán estas lineas mensajes alien? mmm...."]
respuesta2="b"
pregunta3="¿Cómo se llama el nevado más alto del  Perú?"
alternativas3=["a)Huascarán","b)Donofrio","c)Yerupaja"]
comentarios3=[". Su altura es de 6757 m.s.n.m.",". Sin comentarios."," . Yerupaja es el segundo con una altura de 6634 m.s.n.m."]
respuesta3="a"
pregunta4="¿Cómo se llamó primer presidente de Perú?"
alternativas4=["a)José de San Martín Matorras","b) Francisco Javier de Luna Pizarro Pachec","c)José Bernardo de la Torre Tagle y Portocarrero "]
comentarios4=[". De 1821-1822.",". Fue el Segundo.",". Fue el tercero"]
respuesta4="a"

positivo=["¡Muy Bien!","¡Buen Trabajo!","!Excelente¡","¡Estas arrazando!","¡Estas on fire!"]
negativo=["¡Incorrecto!","¡Estabas cerca!","¡Buuuu!","No te desanimes"]
###################Colores###########################
RED='\033[31m'
CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[33m'
RESET='\033[39m'
###################Funciones##########################
def valorAlternativa(alternativa):
  valor=0 
  if alternativa=="a": valor=0
  if alternativa=="b": valor=1
  if alternativa=="c": valor=2
  return valor  
def realizarPregunta(pregunta,alternativas,respuesta,puntaje,comentario):
  print(pregunta)
  for alternativa in alternativas:
    print(alternativa)
  res=input("¿Selecciona una alternativa?: ")
  while res not in ["a","b","c"]:
    res=input("Tu respuesta debe ser a, b o c: ")
  if res==respuesta:
    puntaje+= 5
    print(random.choice(positivo)+", "+nombre+comentario[valorAlternativa(res)]+"\n")
  else:
    puntaje-=2
    print(random.choice(negativo)+", "+nombre+comentario[valorAlternativa(res)]+"\n")
  return puntaje 
  
def realizarPreguntaF(pregunta,alternativas,respuesta,puntaje,comentario):
  print(YELLOW+"PREGUNTA BONUS"+RESET)
  print('Esta pregunta tiene un multiplicador aleatorio maximo de 5, si la respondes correctamente;por ello tiene una dificultad mayor, mucha suerte')
  print(pregunta)
  for alternativa in alternativas:
    print(alternativa)
  res=input("¿Selecciona una alternativa?: ")
  while res not in ["a","b","c"]:
    res=input("Tu respuesta debe ser a, b o c: ")
  if res==respuesta:
    multiplicador= random.randint(2,5)
    if puntaje > 0:
      puntaje*=multiplicador
      print(random.choice(positivo)+", "+nombre+comentario[valorAlternativa(res)]+"\n"+YELLOW+ "Ganaste un multiplicador de "+RESET+str(multiplicador)+"\n")
    else:
      puntaje=0
      print(random.choice(positivo)+", "+nombre+comentario[valorAlternativa(res)]+"\n"+YELLOW+ "Tu puntuacion era negativa por lo que ahora es 0\n")
  else:
    print(random.choice(negativo)+", "+nombre+comentario[valorAlternativa(res)] +", pero no te preocupes no pierdes puntos \n")
  return puntaje 
def mostrarscore(SCORE):
  print(YELLOW+"          SCORE"+RESET+"\n")
  for score in SCORE:
    print("     "+score)
  print("\n")  
  time.sleep(2)
################Codigo principal###########################  
SCORE=[]  
nombre="none"
continuar=True
while continuar==True : 
  print(GREEN+'Bienvenido a mi trivia sobre cultura general peruana'+RESET)
  print('Pondremos a prueba tus conocimientos y el de tus amigos.')
  print("Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'enter' para enviar tu respuesta.\n")
  print('Ganaras 5 puntos por respuesta correcta y perderas 2 puntos por respuesta incorrecta.')
  nombre=input("¿Cual es tu nombre?: \n")
  print("Cargando...")
  time.sleep(2)
  print("\n")
  nombre=CYAN+nombre+RESET
  puntaje=0
  puntaje = realizarPregunta(pregunta1,alternativas1,respuesta1,puntaje,comentarios1) 
  time.sleep(1)
  puntaje = realizarPregunta(pregunta2,alternativas2,respuesta2,puntaje,comentarios2)
  time.sleep(1)
  puntaje = realizarPregunta(pregunta3,alternativas3,respuesta3,puntaje,comentarios3)
  time.sleep(1)
  puntaje = realizarPreguntaF(pregunta4,alternativas4,respuesta4,puntaje,comentarios4)
  print("Calculando...")
  time.sleep(2)
  print("\n Gracias por jugar "+nombre+ ",tu puntaje es "+RED+str(puntaje)+RESET +"\n")  
  print("\n") 
  SCORE.append(nombre+"................"+str(puntaje))
  #mostrarscore(SCORE)
  accion=input("¿Desea intertar de nuevo? Escriba 's' si desea continuar o 'n'para terminar.\n")
  while accion not in ["s","n"] :
    accion=input("Ingrese un valor valido s o n: ")
  if accion!="s":
    continuar=False
  print("\n")  
print("\n Mostrando resultados finales...\n")
time.sleep(2)
mostrarscore(SCORE)
print("\n Gracias por participar "+CYAN+nombre+RESET+ " espero verte de nuevo.") 
#############################################