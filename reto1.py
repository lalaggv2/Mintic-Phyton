#se le pide al empleado que ingrese su salario, horas extras y bonus del mes
salarioMes = (float(input('Cual es su salario mensual?')))

salarioHora = salarioMes/192

print(salarioHora)

horaExtra = (int(input('Cuantas horas extras?')))
if horaExtra >= 0.1:
  horaExtras = (horaExtra * (salarioHora * 1.25))
else:
  horaExtras = (salarioHora * 0)

print(horaExtras)

bonoMes = input('Gano bono durante el mes? Responda S o N ')
if bonoMes == "s" or bonoMes == "S":
  bono = (salarioMes * 0.05)
else:
  bono = (salarioMes * 0)

print(bono)

salarioBruto = (salarioMes + horaExtras + bono)
print(salarioBruto)

#Ahora vamos a calcular las deducciones

pos = (salarioBruto * 0.035)
print(pos)

pension = (salarioBruto * 0.04)
print(pension)
cajacom = (salarioBruto * 0.01)
print(cajacom)
salarioNeto = (salarioBruto - (pos + pension + cajacom))
print(salarioNeto)

#se le pide al empleado que ingrese su salario, horas extras y bonus del mes

'''print("Digite su salario base mensual")
salarioMes = int(input())

salarioHora = salarioMes/192

print(salarioHora)

print("Cuantas horas extras hizo?")
horaExtra = int(input())
if horaExtra >= 1:
  horaExtras = (horaExtra * (salarioHora * 1.25))
else:
  horaExtras = (salarioHora * 0)

print(horaExtras)

print("Recibio bono el mes pasado? ingrese 0 para no y 1 para si")
bonoMes = input()
if bonoMes == 1:
  bono = (salarioMes * 0.05)
else:
  bono = (salarioMes * 0)

print(bono)

salarioBruto = (salarioMes + horaExtras + bono)
print(salarioBruto)

salarioBase, horasEx, bonificacion = input().split()

#Ahora vamos a calcular las deducciones

pos = (salarioBruto * 0.035)
print(pos)

pension = (salarioBruto * 0.04)
print(pension)
cajacom = (salarioBruto * 0.01)
print(cajacom)
salarioNeto = (salarioBruto - (pos + pension + cajacom))
print(salarioNeto)'''