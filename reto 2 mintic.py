distancia, velocidad, tiempo = input().split()

distancia = int(distancia)
velocidad = float(velocidad)
tiempo = float(tiempo)
#print(distancia, velocidad, tiempo)

velUsuario = (distancia / tiempo)

veloLimetroseg = (velocidad / 3.6)

velCurso = (veloLimetroseg * 1.2)

def controlVelocidad():
  if veloLimetroseg <= 0 or velUsuario <= 0:
    print("ERROR")
  elif (velUsuario <= veloLimetroseg):
    print("OK")
  elif (veloLimetroseg < velUsuario < velCurso): 
    print("MULTA")
  else:
    print("CURSO SENSIBILIZACION")
   
controlVelocidad() 