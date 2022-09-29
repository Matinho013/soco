def calcularpago(horas, tarifa):
  MAX_HORAS_SEMANALES = 40
  horas_extras = 0
  if (int(horas) > MAX_HORAS_SEMANALES):
    horas_extras = int(horas) - MAX_HORAS_SEMANALES
    horas = MAX_HORAS_SEMANALES
    calculo = (horas * tarifa) + (horas_extras * (tarifa * 1.5))
    return calculo
try:
    horas = int(input("Ingrese el número de horas: "))
    tarifa = int(input("Ingrese tarifa: "))
    pago = calcularpago(horas, tarifa)
    print(pago)
except:
    print("Error, debe ingresar un valor numérico")
