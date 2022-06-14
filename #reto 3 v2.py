#reto 3

#funcion para validar que las bicicletas cumplan con los requisitos de ciclas legales segun la UCI y si cumple, entrega los precios de las mismas. Si no cumple, entrega un mensaje de que no esta disponible.

def calcular():
  precios = []
  for i in bicicletas:
    bicis = i.split(" ")
    if 239<int(bicis[0]) and int(bicis[0])<301 and int(bicis[1])>161 and int(bicis[1])<181 and int(bicis[2])>239 and int(bicis[2])<276 and int(bicis[3])<51: 
      precios.append(int(bicis[4]))
    else:
      continue
  if len(precios) == 0:
    print("NO DISPONIBLE")
    return "NO DISPONIBLE"
  else:
    print(precios)
    return precios
  
# aqui pregunto la longitud de la lista de bicicletas y creo una lista vacia para guardar los precios y caracteristicas de las bicicletas
bicicletas = []
num_bicicletas = int(input())
cont = 0
while cont < num_bicicletas:
  bicicletas.append(input())
  cont += 1

calcular()

