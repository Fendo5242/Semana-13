from datetime import date


hoy = date.today()
dia_proximo = date(2020, 7, 28)
faltan = dia_proximo - hoy


print ("Hoy:", hoy)
print ("Día de nuestra independencia", dia_proximo)
print ("Faltan", faltan.days, "días")

